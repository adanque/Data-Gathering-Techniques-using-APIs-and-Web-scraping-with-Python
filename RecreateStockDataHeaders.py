# Name: Alan Danque
# Date: 20191223
# Course: DSC 540
# Desc: Final Term Project
# Replace Headers
import csv
from csv import DictReader
from sqlalchemy import create_engine
from pandas import DataFrame
import {Password Removed}
import urllib
# Credentials for reading from the database table
conn = {Password Removed}.connect('Driver={SQL Server};'
                      'Server=192.168.1.28;'
                      'Database=DSC540_STOCK_METRICS;'
                      ';UID=usrDSC540;PWD=Password1')
                      #'Trusted_Connection=yes;')
# Credentials for writing to the database table
quoted = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=192.168.1.28;DATABASE=DSC540_STOCK_METRICS;UID=usrDSC540;PWD=Password1")
engine = create_engine('mssql+{Password Removed}:///?odbc_connect={}'.format(quoted))
cursor = conn.cursor()
cursor.execute('''  
SELECT [EntryDt], [index], [No.], [Ticker], [Company], [Sector], [Industry], [Country], [Market Cap], [P/E], [Price], [Change], [Volume], [Date], [Time], [WeekDay], [ChangeNPCT] FROM DSC540_STOCK_METRICS..STOCK_DATA
          ''')
desc = cursor.description
# Get the column names
column_names = [col[0] for col in desc]
print(column_names)
# Create dictionary from sql table
data = [dict(zip(column_names, row))
        for row in cursor.fetchall()]

# FORMAT & RELACE HEADERS
header_rdr = DictReader(open('NewHeaders.csv', 'rt'))
header_rows = [h for h in header_rdr]

print(header_rows)
# Create a new list named new_rows to rewrite the new renamed headers list of dictionaries.
new_rows=[]

# Loop through list of dictionaries to walk through each row of data
for data_dict in data:
    new_row = {}
    # At each list iteration walk through the current dictionary
    for dkey, dval in data_dict.items():
        # While looping through the current dictionary loop through the header dictionary
        # print(dkey, dval)
        for header_dict in header_rows:
            # print(header_dict.values())
            # if the name of the "dkey" field/column header matches "Name" within the header csv then get the "Label" keyed value for that Name.
            if dkey in header_dict.values():
                new_row[header_dict.get('Label')] = dval
                # print(new_row)
    new_rows.append(new_row)

print(new_rows[0:2])

# Write a new csv using the renamed headers list of dictionaries
keys = new_rows[0].keys()
with open('RenamedHeadersWithData.csv', 'wt') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(new_rows)


# Convert dictionary to pandas dataframe
df = DataFrame(data[0:])
# Load to SQL
df.to_sql('STOCK_DATA_TEST', schema='dbo', con=engine, if_exists='append', chunksize=1000, index=False)

