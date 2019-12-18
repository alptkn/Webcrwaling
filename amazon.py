import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re  


def insert_dash(string,index,input):
	return string[:index] + input + string[index:]

class Product(object):

	def __init__(self,attr,price,link,img,price_int):
		self.attr = attr
		self.price = price
		self.link = link
		self.image = img 
		self.price_int = price_int


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
	
	contain = container[i].find("span",{"data-component-type" : "s-product-image"})

	link = contain.a["href"]
	#print(link)
	

	contain = container[i].find("div",{"class" : "a-section aok-relative s-image-square-aspect"})
	img = contain.img["src"]
	
	

	contain = container[i].find("span",{"class" : "a-size-base-plus a-color-base a-text-normal"})
	attr = contain.text
	
	if container[i].find("span",{"class" : "a-price-whole"}):
		price = container[i].find("span",{"class" : "a-price-whole"}).text
		price_new = price.replace(",","")
		price_int = price_new.replace(".","")
	#price_new = price_new(".","")
	else:
		contain = container[i].find("div",{"class" : "a-row a-size-base a-color-secondary"})
		price = contain.find("span",{"class" : "a-color-base"}).text
		price = price[1:]
		new_price = price.split(",")[0]
		price_int = new_price.replace(".","")


	Products.append(Product(attr,price,link,img,int(price_int)))
	print(Products[i].attr)
	print(Products[i].price)
	print(Products[i].link)
	print(Products[i].image)
	print(Products[i].price_int)
#https://www.amazon.com.tr/s?k=&rh=n%3A12601898031&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss
	
