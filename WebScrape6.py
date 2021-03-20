import re
import urllib.request
from bs4 import BeautifulSoup as bs
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
from datetime import datetime
#site = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
site = 'https://finviz.com//screener.ashx'
page = urllib.request.urlopen(site)

soup = bs(page.read(), features="lxml")

#print(soup.prettify())
#table = soup.find('table',{'class':'container'})
#table = soup.find('table',{'class':'screener-view-table'}
table = soup.findAll('table')
#table = soup.find('div',{'id':'screener-content'})
# print(type(table))
SD = dict()
print(table)
#td = table.findAll()

#td = table.findAll('td',{'class':'screener-body-table-nw'})

#print(table.child)
#soup = bs.BeautifulSoup(table)
#td = table.findAll('td')
#tr = table.findAll('tr')
#print(td)
#for row in table.findall('td'):
#    print(row)
#for row in tr[1:]: # table.findall('tr'):

#news_tooltip-tab
#nn-tab-link
'''
for row in tr: # table.findall('tr'):
    col = row.findAll('td')

    #print(len(col))
    #print(col)
    #print(col[0])
    now = datetime.now()
    #dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = now.strftime("%m/%d/%Y")
    print("date =", dt_string)

    #print("now =", now)
    print(col[1].text.replace('<td align="center" class="nn-date" width="40">', ''))
    ##print(col[1].contents)
    #print(col[2])
    #print(col[1].find('td', {'class': 'nn-date'}))

   # print(col[2].find('table', {'class':'news_tooltip-tab'}))
    print(col[2].text.replace('<td title="cssbody=[news_tooltip-bdy] cssheader=[news_tooltip-hdr] body=[&lt;table width=400&gt;&lt;tr&gt;&lt;td class=', ''))
    #print(col[2].find('td', {'class': 'news_tooltip-tab'}).contents)

    print(col[2].findAll('class')) # problem
   ## print(col[2].find('a', {'class': 'nn-tab-link'}).contents)
    print(col[2].find('a', {'class': 'nn-tab-link'}).get('href'))
    print(col[2])
'''
   # if len(col)>0:
   #     print("length > 0")
        # print(col)
       # print(str(col[0].string.strip()))
       # print(str(col[1].string.strip()))
       # print(str(col[2].string.strip()))
       # print(str(col[3].string.strip()))
       # print(str(col[4].string.strip()))

       # ticker = str(col[0].string.strip())
       # sector = str(col[3].string.strip()).lower()
    # SD[ticker] = sector
#print(SD)
#————————————————
#版权声明：本文为CSDN博主「weixin_43876023」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/weixin_43876023/article/details/84643182