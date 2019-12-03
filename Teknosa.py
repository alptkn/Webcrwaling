import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 


def insert_dash(string,index,input):
	return string[:index] + input + string[index:]

url = input("Enter the brand of laptop")
my_url = 'https://www.teknosa.com/arama?q=%3Arelevance%3Acategory%3A1020101&text=#'

my_url = insert_dash(my_url,32,url)



#Open connection, grapping the web page 
uClient = uReq(my_url)                   
page_html = uClient.read()
uClient.close()

#parse HTML code 
page_soup = soup(page_html,"html.parser")#
#print(page_soup.h1)

#grabs all divs which has class product-item
container = page_soup.findAll("div",{"class" : "product-item"})
#print(len(container)),
#print(container[0])

#taking brand of the devie 
len = len(container)

for count in range (0,len):
	contain = container[count].find("div",{"class" : "product-image"})
	(brand,rest) = (contain.div.img["alt"]).split(maxsplit=1) 
	print(brand)

	context = container[count].find("div",{"class" : "product-name"}).a.text
	print(context)
	#attributes = context.findAll("a",{"class" : "product-name"})
	#print(attributes.text)

	price = container[count].findAll("span",{"class" : "price-tag new-price font-size-tertiary"})
	print(price[0].text)





print(my_url)