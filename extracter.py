import requests
from pathlib import Path
from bs4 import BeautifulSoup as BS
from identifier import know_index

'''
this header section is necessary for some websites..... not for all
'''
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "http://www.nepalstock.com/todaysprice/export"
page = requests.get(url, headers=headers)
input = page.content
output = BS(input, "html.parser")

# checking if the soup is ready!!

table_rows = output.find_all("tr")

def listing_today():
	return len(table_rows)
# check sucessful
# num_rows = len(table_rows)

'''
****
****
each table row varies from 0 to 157
0 is the labelling for the columns in the table.....
1 contains Agricultural Development Bank
..
..
..
157 contains Womi Microfinance
****
****
'''

#table_row_lone = table_rows[157]
# print(len(table_row_lone))
# table_data = table_row_lone.find_all("td")
# print(table_data[0].text)

'''
****
check looping to get individual members.....
made a function that can get you all the individual data!!
****
'''

def get_today():
  for i in range(1,listing_today()):
    table_row = table_rows[i]
    table_data = table_row.find_all("td")
    print(table_data[0].text+"|"+table_data[4].text)

# function check....

# get_today()
'''
***
file check .... not particular to program..
***
filename = "apple"
pathname = 'data/'+filename+'.txt'
file = open(pathname,'a')
file.write("Hello Hello\n")
file.close()
'''

def update():
  for j in range(1,listing_today()):
    table_row = table_rows[j]
    table_data = table_row.find_all("td")
    stuff = table_data[2].text

    file = 'data/'+str(table_data[0].text)+'.txt'
    myfile = Path(file)
    if myfile.is_file():
      data = open(file, 'a')
    else:
      data = open(file, 'w')

    data.write(str(stuff)+"\n")

'''
****
sucessful check updater!!!!
****
'''


# the function below gets the name of the company when the use enters the symbol of the company
'''
****
****
'''
def name(symbol):
	index = know_index(symbol)
	if index != 0:
		table_row = table_rows[index]
		table_data = table_row.find_all("td")
		return table_data[0].text
	else:
		return "UNKNOWN SYMBOL"

update()
