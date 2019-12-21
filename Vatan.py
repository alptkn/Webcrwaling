import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def insert_dash(string,index,input):
	return string[:index] + input + string[index:]


choice = input("Attribute")

site= "https://www.vatanbilgisayar.com/notebook/"
choice = choice.replace(" ","-")

my_url = insert_dash(site,len(site),choice)


hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(my_url,headers=hdr)
uClient = uReq(req)



print(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html,"html.parser")

container = page_soup.findAll("div",{"class" : "ems-prd-image"})

container_price = page_soup.findAll("div",{"class" : "urunListe_satisFiyat"})

lenght2 = len(container_price)
print(lenght2)

lenght = len(container)
print(lenght)

if lenght > lenght2:
	size = lenght2
else:
	size = lenght		

for i in range (0,size):
	link = container[i].a["href"]
	print(link)

	img = container[i].img["data-original"]
	print(img)

	attr = container[i].img["alt"]
	print(attr)

	price = container_price[i].text
	
	price_new = price.split(",")[0]
	print(price_new)
	price_int = price_new.replace(".","")
	print(price_int)