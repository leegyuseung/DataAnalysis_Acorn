import urllib.request
from bs4 import BeautifulSoup

try:
    url = "http://www.naver.com"
    page = urllib.request.urlopen(url)
           
    soup = BeautifulSoup(page.read(), "lxml") 
    title = soup.find('ol').find_all('li')
    for i in range(0, 10):
        print(str(i + 1) + ") " + title[i].a['title'])
except Exception as e:
    print('에러:', e)