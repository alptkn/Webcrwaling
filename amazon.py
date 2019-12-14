import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re  


def insert_dash(string,index,input):
	return string[:index] + input + string[index:]

class Product(object):

	def __init__(self,attr,price,link,img):
		self.attr = attr
		self.price = price
		self.link = link
		self.image = img 



Products = []



choice = input("Eter criteria:")

my_url = "https://www.amazon.com.tr/s?k=&rh=n%3A12601898031&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"

	
choice = re.sub(r"\s+",'+',choice)
my_url = insert_dash(my_url,30,choice)
	

print(my_url)

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

container = page_soup.findAll("div",{"class" : "sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"})

lenght = len(container)
for i in range (0,lenght-2):
	
	contain = container[i].find("span",{"class" : "rush-component"})

	link = contain.a["href"]
	

	contain = container[i].find("div",{"class" : "a-section aok-relative s-image-square-aspect"})
	img = contain.img["src"]
	
	

	contain = container[i].find("span",{"class" : "a-size-base-plus a-color-base a-text-normal"})
	attr = contain
	

	price = container[i].find("span",{"class" : "a-price-whole"})

	Products.append(Product(attr.text,price.text,link,img))
	
	print(Products[i].attr)	
	print("***********************************************************************") 
