import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
from dictionary import *

my_url = 'https://www.hepsiburada.com/ara?q='

chose = input("Enter what are looking for ")

words = chose.split()

for word in words:
	my_url = my_url + word
	my_url = my_url + "+"	



uClient = uReq(my_url)
page_html = uClient.read()

page_soup = soup(page_html,"html.parser")


container = page_soup.findAll("li",{"class" : "search-item col lg-1 md-1 sm-1 custom-hover not-fashion-flex"})



len = len(container)

for count in range (0,len):
	contain = container[count].find("noscript")
	(brand,rest) = (contain.img["alt"]).split(maxsplit = 1)
	print(brand)
	#print(rest)
	price  = container[count].findAll("div",{"class" : "price-value"})
	price1 = container[count].findAll("span",{"class" : "old product-old-price"})
	price2 = container[count].findAll("span",{"class" : "price product-price"})
	if price:
		price_print = (price[0].text).split()
		print(price_print[0])
	

	elif price2:
		price_print = (price2[0].text).split()
		print(price_print[0])	


