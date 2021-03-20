# Name: Alan Danque
# Date: 20191223
# Course: DSC 540
# Desc: Final Term Project
# Scrapes Stock Information from the FINVIZ.com web site and loads to DB
import datetime
from sqlalchemy import create_engine
import re
import urllib.request
import urllib
import time
import re
from bs4 import BeautifulSoup as bs
from pandas import DataFrame

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=192.168.1.28;'
                      'Database=DSC540_STOCK_METRICS;'
                      ';UID=usrDSC540;PWD=Password1')
                      #'Trusted_Connection=yes;')

quoted = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=192.168.1.28;DATABASE=DSC540_STOCK_METRICS;UID=usrDSC540;PWD=Password1")
engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

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

tabletop+=('Date',)
tabletop+=('Time',)
tabletop+=('WeekDay',)
tabletop+=('ChangeNPCT',)
print(tabletop)


todaydt = str(datetime.today().date())
#detail=[]
count = 2
# LOOP THROUGH ALL 8000 PAGES
while (count < 790): #790
  detail = []
  #print('The count is:', count)
  site = 'https://finviz.com/screener.ashx?v=111&r='+str(count)+'1'
  time.sleep(5)
  #site = 'https://finviz.com/screener.ashx?v=111&r=21'
  page = urllib.request.urlopen(site)
  soup = bs(page.read(), features="lxml")
  table = soup.find('div', {'id': 'screener-content'})
  tr1 = table.findAll('tr',{'class':'table-dark-row-cp'})
  tr2 = table.findAll('tr',{'class':'table-light-row-cp'})

  #SD = dict()
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
      ,datetime.today().date()
      ,datetime.today().strftime('%H:%M') #datetime.strptime(todaydt, '%H:%M:%S.%f')   #datetime.today().time()
      ,datetime.today().weekday()
      ,str(col1[9].get_text()).replace("%", "")
      )
      new_row=dict(zip(tabletop, detail_row))
      detail.append(new_row)

  for row in tr2:
      new_row = {}
      col2 = row.findAll('td')
      #print(col2)
      detail_row = (
      str(col2[0].get_text())
      ,str(col2[1].get_text())
      ,str(col2[2].get_text())
      ,str(col2[3].get_text())
      ,str(col2[4].get_text())
      ,str(col2[5].get_text())
      ,str(col2[6].get_text())
      ,str(col2[7].get_text())
      ,str(col2[8].get_text())
      ,str(col2[9].get_text())
      ,str(col2[10].get_text())
      ,datetime.today().date()
      ,datetime.today().strftime('%H:%M') #datetime.strptime(todaydt, '%H:%M:%S.%f')   #datetime.today().time()
      ,datetime.today().weekday()
      ,str(col2[9].get_text()).replace("%", "")
      )
      new_row=dict(zip(tabletop, detail_row))
      detail.append(new_row)

  # Convert dictionary to pandas dataframe
  df = DataFrame(detail)
  # Load to SQL
  df.to_sql('STOCK_DATA', schema='dbo', con=engine, if_exists='append', chunksize=1000)

  count = count + 2





# print(detail)





#cursor.execute('SELECT * FROM DSC540_STOCK_METRICS..POC')

#for row in cursor:
#    print(row)

#cursor.execute('''
#                INSERT INTO DSC540_STOCK_METRICS..POC (col1)
#                VALUES
#                (2),
#                (3)
#                ''')
#conn.commit()

#df.to_sql('STOCK_DATA', conn, if_exists='replace', index = False)

# Convert dictionary to pandas dataframe
#df = DataFrame(detail)
# Load to SQL
#df.to_sql('STOCK_DATA', schema='dbo', con = engine, if_exists='append', chunksize=1000, index = False)
#df.to_sql('STOCK_DATA', schema='dbo', con = engine, if_exists='append', chunksize=1000)

# Review after insert
"""
cursor = conn.cursor()
cursor.execute('''  
SELECT * FROM DSC540_STOCK_METRICS..STOCK_DATA
          ''')
for row in cursor.fetchall():
    print (row)
"""