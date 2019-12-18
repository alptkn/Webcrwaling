import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import re

def insert_dash(string,index,input):
	return string[:index] + "+" + input + "+" + string[index:]


class Product(object):


	def __init__(self,attr,price,link,img,int_price):
		self.attr = attr
		self.price = price
		self.link = link
		self.img = img
		self.int_price = int_price

	


def teknosa(Products = []):

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

	lenght = len(container)


	for count in range (0,lenght):
		contain = container[count].find("div",{"class" : "product-name"})
		attribute = contain.a.span.text
		
		contain = container[count].find("span",{"class" : "price-tag new-price font-size-tertiary"})
		price = contain.text
		price_new = price[:-2]
		price_new = price_new.split(',')[0]
		price_new = price_new.replace(".","")

		link = container_link[count].a["href"]
			
		photo = container_link[count].img["src"]
		
		Products.append(Product(attribute,price,link,photo,int(price_new)))


def hepsiburada(Products = []):
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
		#print(link)

		contain = container[i].find("div",{"class" : "carousel-lazy-item"})
		img = contain.img["src"]
		attr = contain.img["alt"]
		#print(img)
		#print(attr)

		contain = container[i].find("div",{"class" : "price-value"})
		
		if contain:
			price = contain.text
			price = re.sub(r"\s+",'',price)
		else:
			contain = container[i].find("span",{"class" : "price product-price"})		

		price_new = price[:-5]
		price_new = re.sub(r"\s+",'',price_new)

		price_new = price_new.replace(".","")

		price_int = int(price_new)
		Products.append(Product(attr,price,link,img,price_int))

def amazon(Products = []):
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
		

		price = container[i].find("span",{"class" : "a-price-whole"}).text
		price_new = price.replace(",","")
		price_int = price_new.replace(".","")
		#price_new = price_new(".","")
		Products.append(Product(attr,price,link,img,int(price_int)))
		
def IstBil(Products = []):
	my_url = "https://www.istanbulbilisim.com/notebook-kategorileri-1.html?f=9_8&dpIDs=1621"

	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	page_soup = soup(page_html,"html.parser")

	container = page_soup.findAll("div",{"class" : "col-xs-6 col-sm-6 col-md-4"})
	link_container = page_soup.findAll("div",{"class" : "info"})


	lenght = len(container)

	for i in range (0,lenght):
		contain = container[i].find("div",{"class" : "image"})
		img = contain.img["src"]
		attr = contain.img["alt"]
		contain = link_container[i].find("p",{"class" : "title"})
		link = contain.a["href"]
		contain = link_container[i].find("p",{"class" : "try price-act pull-left clear-left"})
		price = contain.text
		price_new = price.split(",")[0]
		price_int = price_new.replace(".","")
		Products.append(Product(attr,price,link,img,int(price_int)))


def N11(Products =[]):
	my_url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?q="

	choice = input("Enter the attr:")

	choice = re.sub(r"\s+",'+',choice)

	my_url = insert_dash(my_url,52,choice)

	print(my_url)

	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	page_soup = soup(page_html,"html.parser")

	container = page_soup.findAll("li",{"class" : "column"})

	lenght = len(container)

	print(lenght)

	for i in range (0,lenght):
		contain = container[i].find("div",{"class" : "pro"})
		link = contain.a["href"]
		contain = container[i].find("a",{"class" : "plink"})
		img = contain.img
		attr = contain.img["alt"]
		contain = container[i].find("div",{"class" : "proDetail"})
		price = contain.ins.text
		price = re.sub(r"\s+",'',price)
		price_new = price.split(",")[0]
		price_int = price_new.replace(".","")
		Products.append(Product(attr,price,link,img,int(price_int)))
