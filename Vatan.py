import urllib.parse
import urllib.request
import bs4
from bs4 import BeautifulSoup as soup

url = 'https://www.vatanbilgisayar.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read()

page_soup = soup(the_page,"html.parser")

container = page_soup.findAll("div",{"class" : "site-wrapper"})

lenght = len(container)
print(lenght)

print(container)