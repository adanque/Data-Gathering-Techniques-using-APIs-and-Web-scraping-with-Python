# Name: Alan Danque
# Date: 20200119
# Course: DSC 540
# Desc: Week 7 Exercise - Importing Data

# Pages 219 - 224

import xlrd
from xlrd.sheet import ctype_text
import agate

# Function to return a list of cleaned data types from a passed in list
def getTypes(passedlist):
    types = []
    for v in passedlist:
        value_type = ctype_text[v.ctype]
        if value_type == 'text':
            types.append(text_type)
        elif value_type == 'number':
            types.append(number_type)
        elif value_type == 'xldate':
            types.append(date_type)
        else:
            types.append(text_type)
    return types

# Scalar function to return cleaned value if the value passed is equal to '-' else return the same value passed in.
def remove_bad_chars(val):
    if val == '-':
        return None
    return val


# This function intializes an empty list named cleaned_rows populated by looping through country_rows and
# iteratively cleaning it and appending to the cleaned_rows list
def get_new_array(old_array, function_to_clean):
    new_arr = []
    for row in old_array:
        cleaned_row = [function_to_clean(rv) for rv in row]
        new_arr.append(cleaned_row)
    return new_arr

# Open the xls workbook
workbook = xlrd.open_workbook('unicef_oct_2014.xls')
print(workbook.nsheets)
print(workbook.sheet_names())

# Set the worksheet to the first worksheet
sheet = workbook.sheets()[0]
print(sheet.nrows)
print(sheet.row_values(0))

# Iteratively print the cell values for each row from the worksheet stating datatype then value
for r in range(sheet.nrows):
    print(r, sheet.row(r))

print("zipped rows")
print(sheet.row_values(4))
print(sheet.row_values(5))

# Get the column headers in rows 5 and 6 and combine them.

title_rows = zip(sheet.row_values(4), sheet.row_values(5))
print(title_rows)

# Initialize the titles with format. Note when row header is combined from two rows the first of the set gets the spanned top colum name
titles = [t[0] + ' ' + t[1] for t in title_rows]
# Strip leading and trailing spaces
titles = [t.strip() for t in titles]
print(titles)

# Initialize a list of to contain a list for each sheet row.
country_rows = [sheet.row_values(r) for r in range(6, 114)]
print("Country_rows Type")
print(type(country_rows))
print(country_rows)


# Define agate data types
text_type = agate.Text()
number_type = agate.Number()
boolean_type = agate.Boolean()
date_type = agate.Date()
print(text_type)
print(number_type)
print(boolean_type)
print(date_type)


example_row = sheet.row(6)
print("this row")
#print(sheet.row(6))

print(example_row)
#print(example_row)
#print(example_row[0].ctype)
#print(example_row[0].value)
#print(ctype_text)


# Initialize a list of cleaned types using the function called getTypes.
types = []
types = getTypes(example_row)
#for v in example_row:
#    value_type = ctype_text[v.ctype]
#    if value_type == 'text':
#        types.append(text_type)
#    elif value_type == 'number':
#        types.append(number_type)
#    elif value_type == 'xldate':
#        types.append(date_type)
#    else:
#        types.append(text_type)

print("TYPES HERE")
print(types)
print(titles)


# cleaned_rows = []
#for row in country_rows:
#    cleaned_row = [remove_bad_chars(rv) for rv in row]
#    cleaned_rows.append(cleaned_row)


#table = agate.Table(country_rows, titles, types)


#table = agate.Table(cleaned_rows, titles, types)
#print(type(table))

# Function to return a cleaned list per a passed in list and function to perform the cleaning.
# cleaned_rows = []
cleaned_rows = get_new_array(country_rows, remove_bad_chars)

# Create a agate table of the cleaned rows, titles and the data types.
table = agate.Table(cleaned_rows, titles, types)
table.print_table(max_columns=7)
table.column_names


