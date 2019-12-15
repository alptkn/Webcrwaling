import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re


my_url = "https://www.hepsiburada.com/ara?q=asus+8gb+notebook"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

container = page_soup.findAll("li",{"class" : "search-item col lg-1 md-1 sm-1 custom-hover not-fashion-flex"})


lenght = len(container)

for i in range(0,lenght):
	contain = container[i].find("div",{"class" : "box product hb-placeholder"})
	link = contain.a["href"]
	print(link)

	contain = container[i].find("div",{"class" : "carousel-lazy-item"})
	img = contain.img["src"]
	attr = contain.img["alt"]
	print(img)
	print(attr)

	contain = container[i].find("div",{"class" : "price-value"})
	
	if contain:
		price = contain.text
		price = re.sub(r"\s+",'',price)
	else:
		contain = container[i].find("span",{"class" : "price product-price"})		
	print(price)
	