import requests
from bs4 import BeautifulSoup

while True:
    try:
        url = raw_input('Enter a url: ')
        r = requests.get(url)
        break
    except Exception:
        print 'Please enter a valid url.'
soup = BeautifulSoup(r.text)

links = [link for link in soup.find_all('a')]
images = [image for image in soup.find_all('img')]
for link in links:
    print link
for image in images:
    print image
