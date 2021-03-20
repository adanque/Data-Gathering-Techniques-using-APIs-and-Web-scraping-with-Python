"""
Author: Alan Danque
Date:   20200127

"""

import re
import urllib.request
import time
import re
from bs4 import BeautifulSoup as bs
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date =", dt_string)
dt_string = now.strftime("%m/%d/%Y")
#print("date =", dt_string)

#site = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
basesite = 'https://finviz.com/'
page = 'screener.ashx'
site = basesite + page
page = urllib.request.urlopen(site)
soup = bs(page.read(), features="lxml")

print("header")
table = soup.find('table',{'class':'screener-view-table'})
tr0 = table.findAll('tr')
for row in tr0:
    col1 = row.findAll('td')
    header = (
    str(col1[0].get_text())
    ,str(col1[1].get_text())
    ,str(col1[2].get_text())
    ,str(col1[3].get_text())
    ,str(col1[4].get_text())
    ,str(col1[5].get_text())
    ,str(col1[6].get_text())
    ,str(col1[7].get_text())
    ,str(col1[8].get_text())
    ,str(col1[9].get_text())
    ,str(col1[10].get_text())
    ,str(col1[11].get_text())
    ,str(col1[12].get_text())
    ,str(col1[13].get_text())
    )
    print(header)

###########table-top
print("table-top")
table = soup.find('div',{'id':'screener-content'})
#tr1 = table.findAll('td',{'class' : lambda L: L and L.startswith('table-top')})
tr1 = table.find_all('td', class_=re.compile('^table-top'))
tabletop = ()
for row in tr1:
    tabletop+=(row.get_text(),)
print(tabletop)


detail=[]
count = 2
# LOOP THROUGH ALL 8000 PAGES
while (count < 8): #790
  #print('The count is:', count)
  site = 'https://finviz.com/screener.ashx?v=111&r='+str(count)+'1'
  time.sleep(5)
  #site = 'https://finviz.com/screener.ashx?v=111&r=21'
  page = urllib.request.urlopen(site)
  soup = bs(page.read(), features="lxml")
  table = soup.find('div', {'id': 'screener-content'})
  tr1 = table.findAll('tr',{'class':'table-dark-row-cp'})
  tr2 = table.findAll('tr',{'class':'table-light-row-cp'})

  SD = dict()
  for row in tr1:
      new_row = {}
      col1 = row.findAll('td')
      #print(col1)
      detail_row = (
      str(col1[0].get_text())
      ,str(col1[1].get_text())
      ,str(col1[2].get_text())
      ,str(col1[3].get_text())
      ,str(col1[4].get_text())
      ,str(col1[5].get_text())
      ,str(col1[6].get_text())
      ,str(col1[7].get_text())
      ,str(col1[8].get_text())
      ,str(col1[9].get_text())
      ,str(col1[10].get_text())
      )
      new_row=dict(zip(tabletop, detail_row))
      detail.append(new_row)

  for row in tr2:
      new_row = {}
      col2 = row.findAll('td')
      #print(col2)
      detail_row = (
      str(col1[0].get_text())
      ,str(col1[1].get_text())
      ,str(col1[2].get_text())
      ,str(col1[3].get_text())
      ,str(col1[4].get_text())
      ,str(col1[5].get_text())
      ,str(col1[6].get_text())
      ,str(col1[7].get_text())
      ,str(col1[8].get_text())
      ,str(col1[9].get_text())
      ,str(col1[10].get_text())
      )
      new_row=dict(zip(tabletop, detail_row))
      detail.append(new_row)
  count = count + 2

print(detail)
