import re
import urllib.request
from bs4 import BeautifulSoup as bs
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

#site = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
site = 'https://finviz.com/'
page = urllib.request.urlopen(site)

soup = bs(page.read(), features="lxml")

# print(soup.prettify())

table = soup.find('table',{'class':'t-home-table'})
# print(type(table))
SD = dict()
# print(table)

#soup = bs.BeautifulSoup(table)
tr = table.findAll('tr')

# for row in table.findall('tr'):
# print(tr)
for row in tr: # table.findall('tr'):
    col = row.findAll('td')
    # print(col)
    if len(col)>0:
        # print(col)
        print(str(col[0].string.strip()))
        print(str(col[1].string.strip()))
        print(str(col[2].string.strip()))
        print(str(col[3].string.strip()))
       # print(str(col[4].string.strip()))

        ticker = str(col[0].string.strip())
        sector = str(col[1].string.strip()).lower()
    SD[ticker] = sector
print(SD)
#————————————————
#版权声明：本文为CSDN博主「weixin_43876023」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/weixin_43876023/article/details/84643182