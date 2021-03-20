# Name: Alan Danque
# Date: 20191223
# Course: DSC 540
# Desc: Final Term Project
# Review Stock Data
# Checks for duplicates and counts them
# Checks the data types of the ticker field

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=192.168.1.28;'
                      'Database=DSC540_STOCK_METRICS;'
                      ';UID=usrDSC540;PWD=Password1')
                      #'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('''  
SELECT * FROM DSC540_STOCK_METRICS..STOCK_DATA
          ''')
desc = cursor.description
# Get the column names
column_names = [col[0] for col in desc]

# Create dictionary from sql table
data = [dict(zip(column_names, row))
        for row in cursor.fetchall()]


print(type(data))
print(data[0:2])

print(type(desc))
print(desc)


# Get Multiple duplicate counts of unique Ticker and Company
uniqueticker = {}
# loop through the list named data_rows
for row in data:
    # loop through the current dictionary
    for k, v in row.items():
        # if the combination of Make and Model does not exist in the uniquecar dictionary add it else increment the count value
        if (row.get('Ticker')+row.get('Company')) in uniqueticker:
            #print("yes")
            uniqueticker[row.get('Ticker') + row.get('Company')] += 1
        else:
            #print("no")
            uniqueticker[row.get('Ticker')+row.get('Company')] = 1

# print the unique list of Make and Models and the counts of them
print(uniqueticker)



# Outliers and Bad Data
# Review the values of the Ticker field and
# create a target dictionary to save the results of the types of contained data
datatypes = {}
# initialize a new dictionary named start_dict with keys and initial value of 0
start_dict = {'digit':0, 'boolean': 0, 'empty':0, 'time_related': 0, 'text': 0, 'unknown': 0 }

# loop through the list named data_rows passing the values for the Make and Model keys per each iteration
for row in data:
    Ticker = row.get('Ticker')
    Company = row.get('Company')
    TickerCompany = row.get('Ticker')+" "+row.get('Company')
    key = 'unknown'

  # test if the value of model is a number - if it is then set the variable key value to digit
    if Ticker.isdigit():
        key = 'digit'
    # test if model is equal to any of the following values then set the key to boolean
    elif Ticker in ['Yes', 'No', 'True', 'False']:
        key = 'boolean'
    # test if the model is equal to white space characters then would set key to value empty
    elif Ticker.isspace():
        key = 'empty'
    # test if can find the first occurence of the values / or : if so then set key to time_related
    elif Ticker.find('/') > 0 or Ticker.find(':') > 0:
        key = 'time_related'
    # test if the model value is all alpha characters - if so then true then set key to text
    elif Ticker.isalpha():
        key = 'text'
    # test if the value of question is not in the keys of the datatypes dictionary
    if Ticker not in datatypes.keys():
        # if it is not in the datatypes dictionary keys then creates a copy of the start_dict with the MakeModel as the key
        datatypes[Ticker] = start_dict.copy()
        # increment the copied start_dict key (data type count per the key value determined above)
        datatypes[Ticker][key] += 1

# print the dictionary of Ticker key'd datatypes
print(datatypes)



