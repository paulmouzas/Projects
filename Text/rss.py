import requests
from bs4 import BeautifulSoup

url = "http://feeds2.feedburner.com/MarksDailyApple/"
r = requests.get(url)
soup = BeautifulSoup(r.text)
links = []
titles = []
for link in soup.find_all('link'):
    links.append(link.get('href'))
for title in soup.find_all('title'):
    titles.append(title.text)
    
for title, link in zip(titles, links):
    print "Title: %s" % title
    print "Link: %s" % link
    print
    