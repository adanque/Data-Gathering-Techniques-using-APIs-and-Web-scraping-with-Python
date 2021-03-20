#from BeautifulSoup import BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
soup = bs(
    urllib.urlopen('kitco.com/kitco-gold-index.html').read())