import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re 
from All_Website import *
import operator

Products = []

teknosa(Products)

lenght = len(Products)
print(lenght)

hepsiburada(Products)
lenght = len(Products)
print(lenght)
amazon(Products)
lenght = len(Products)
print(lenght)
IstBil(Products)
lenght = len(Products)
print(lenght)
N11(Products)
lenght = len(Products)
print(lenght)

Products.sort(key=operator.attrgetter('int_price'))

for elem in Products:
	print(elem.price)