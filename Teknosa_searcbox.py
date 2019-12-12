import bs4
from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup 
import ctypes 
import re

def insert_dash(string,index,input):
	return string[:index] + "+" + input + "+" + string[index:]



class Product(object):

	def __init__(self,attr,price,link,img): 
		self.attr = attr
		self.price = price
		self.link = link
		self.image = img


Products = []

url = input("Search:")
url = (re.sub("[ ]","+",url))
print(url)

my_url = "https://www.teknosa.com/arama?q=%3Arelevance%3Acategory%3A1020101&text=#"

my_url = insert_dash(my_url,32,url)

print(my_url)

#Open connection, grapping the web page 
uClinet = uReq(my_url)
page_html = uClinet.read()
uClinet.close()

#parse HTML
page_soup = soup(page_html,"html.parser")

container = page_soup.findAll("div",{"class" : "product-text"})
container_link = page_soup.findAll("div",{"class" : "product-image-item"})

len = len(container)


for count in range (0,len):
	contain = container[count].find("div",{"class" : "product-name"})
	attribute = contain.a.span.text
	
	contain = container[count].find("span",{"class" : "price-tag new-price font-size-tertiary"})
	price = contain.text

	link = container_link[count].a["href"]
		
	photo = container_link[count].img["src"]
	
	Products.append(Product(attribute,price,link,photo))

	print(Products[0].attr)

	