import requests
from bs4 import BeautifulSoup


URL='https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser') # creating Html parser using bs4
    needed_data= soup.find_all('a',title="Wikipedia:Citation needed") #Creating a container for needed data 
    return len(needed_data) #returning the count of data

def get_citations_needed_report(URL):
    result=[]
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    needed_data= soup.find_all('a',title="Wikipedia:Citation needed")
    for i in needed_data:
        result.append(i.parent.parent.parent.get_text())

    output="\n".join(result)
    return output

print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))



