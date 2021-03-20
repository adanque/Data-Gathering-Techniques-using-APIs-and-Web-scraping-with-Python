# Name: Alan Danque
# Date: 20200119
# Course: DSC 540
# Desc: Week 7 Exercise - Exploring Table Functions

# Pages 225 - 228



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

# Set the worksheet to the first worksheet
sheet = workbook.sheets()[0]

# Iteratively print the cell values for each row from the worksheet stating datatype then value
for r in range(sheet.nrows):
    print(r, sheet.row(r))

# Get the column headers in rows 5 and 6 and combine them.

title_rows = zip(sheet.row_values(4), sheet.row_values(5))
titles = [t[0] + ' ' + t[1] for t in title_rows]
# Strip leading and trailing spaces
titles = [t.strip() for t in titles]

# Initialize a list of to contain a list for each sheet row.
country_rows = [sheet.row_values(r) for r in range(6, 114)]

# Define agate data types
text_type = agate.Text()
number_type = agate.Number()
boolean_type = agate.Boolean()
date_type = agate.Date()

example_row = sheet.row(6)

# Initialize a list of cleaned types using the function called getTypes.
types = []
types = getTypes(example_row)

# Function to return a cleaned list per a passed in list and function to perform the cleaning.
# cleaned_rows = []
cleaned_rows = get_new_array(country_rows, remove_bad_chars)

# Create a agate table of the cleaned rows, titles and the data types.
table = agate.Table(cleaned_rows, titles, types)
table.print_table(max_columns=7)
table.column_names



print("start new here")


most_egregious = table.order_by('Total (%)', reverse=True).limit(10)
for r in most_egregious.rows:
    print(r)

most_females = table.order_by('Female', reverse=True).limit(10)
for r in most_females.rows:
    print('{}: {}%'.format(r['Countries and areas'], r['Female']))

female_data = table.where(lambda r: r['Female'] is not None)
most_females = female_data.order_by('Female', reverse=True).limit(10)
for r in most_females.rows:
    print('{}: {}%'.format(r['Countries and areas'], r['Female']))


(lambda x: 'Positive' if x >= 1 else 'Zero or Negative')(0)
(lambda x: 'Positive' if x >= 1 else 'Zero or Negative')(4)


# table.columns['Place of residence (%) Urban'].aggregate(agate.Mean())
outputval = table.columns['Place of residence (%) Urban'].aggregates(agate.Mean())
print(outputval)



col = table.columns['Place of residence (%) Urban']
print(col)
print(table.aggregate(agate.Mean('Place of residence (%) Urban')))


has_por = table.where(lambda r: r['Place of residence (%) Urban'] is not None)
print(has_por)
print(has_por.aggregate(agate.Mean('Place of residence (%) Urban')))

first_match = has_por.find(lambda x: x['Rural'] > 50)
first_match['Countries and areas']
print("first_match")
print(first_match)

ranked = table.compute([('Total Child Labor Rank', agate.Rank('Total (%)', reverse=True)),])
for row in ranked.order_by('Total (%)', reverse=True).limit(20).rows:
    print(row['Total (%)'], row['Total Child Labor Rank'])

def reverse_percent(row):
    return 100 - row['Total (%)']
ranked = table.compute([('Children not working (%)',
                             agate.Formula(number_type, reverse_percent)),
                            ])
print(ranked)

ranked = ranked.compute([('Total Child Labor Rank',
                              agate.Rank('Children not working (%)')),
                           ])

print(ranked)

for row in ranked.order_by('Total (%)', reverse=True).limit(20).rows:
    print(row['Total (%)'], row['Total Child Labor Rank'])

