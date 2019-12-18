import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import re


def insert_dash(string,index,input):
	return string[:index] + input + string[index:]


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""        	


class Product(object):

	def __init__(self,attr,price,link,img):
		self.attr = attr
		self.price = price
		self.link = link
		self.img = img

my_url = "https://www.mediamarkt.com.tr/tr/search.html?query=notebook&searchProfile=onlineshop&channel=mmtrtr&searchParams=%2FSearch.ff%3Fquery%3Dasus%2Bnotebook%26filterCategoriesROOT%3DBilgisayar%25C2%25A7MediaTRtrc504925%26channel%3Dmmtrtr"

choice = input("Enter the attribute")

choice = re.sub(r"\s+",'+',choice)

my_url = insert_dash(my_url,51,choice)

print(my_url)

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

container = page_soup.findAll("div",{"class" : "product-wrapper"})
price_container = page_soup.findAll("ul",{"class" : "products-list"})
price_contain = price_container[0].findAll("script")
attr_container = page_soup.findAll("div",{"class" : "content"})

lenght = len(container)

print(lenght)
lenght2 = len(price_contain)


j = 0
for i in range (0,lenght):
	link = container[i].span["data-clickable-href"]
	print(link)
	img = container[i].img["data-original"]
	print(img)	
	attr = attr_container[i].a.text
	attr = re.sub(r"\s+",'',attr)
	print(attr)
	sub = price_contain[j].text
	price = find_between(sub,'price":"','","brand')
	print(price)
	if j == len(price_contain)-1:
		break
	j = j + 2
#https://www.mediamarkt.com.tr/tr/search.html?query=asus&searchProfile=onlineshop&channel=mmtrtr&searchParams=%2FSearch.ff%3Fquery%3Dasus%2Bnotebook%26filterCategoriesROOT%3DBilgisayar%25C2%25A7MediaTRtrc504925%26channel%3Dmmtrtr



