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


my_url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?q="

Products = []
choice = input("Enter the attr:")

choice = re.sub(r"\s+",'+',choice)

my_url = insert_dash(my_url,52,choice)

print(my_url)

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

container = page_soup.findAll("div",{"class" : "listView"})
contain = container[0].findAll("li",{"class" : "column"})

print(len(contain))
lenght = len(contain)

print(lenght)

print(contain[1])
	
for i in range (0,lenght):
	
	temp = contain[i].find("div",{"class" : "pro"})
	link = temp.a["href"]
	print(link) 

	temp = contain[i].find("a",{"class" : "plink"})
	attr = temp.img["alt"]
	img = temp.img["src"]

	temp = contain[i].find("div",{"class" : "proDetail"} )
	price = temp.ins.text
	price = re.sub(r"\s+",'',price)
	price_new = price.split(",")[0]
	price_int = price_new.replace(".","")
	print(price)

