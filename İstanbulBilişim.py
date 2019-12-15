import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 


class Product(object):

	def __init__(self,attr,price,link,img):
		self.attr = attr
		self.price = price
		self.link = link
		self.img = img



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
	

