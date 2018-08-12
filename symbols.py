import requests
from bs4 import BeautifulSoup as BS

site = "http://merolagani.com/CompanyList.aspx#collapse_0"
load = requests.get(site)
nosoup = load.content

souped = BS(nosoup, "html.parser")

table = souped.find_all("table", class_="table table-striped table-hover")

data = table[0].find_all("tr")
print(len(data))
in_data = data[6].find_all("td")
print(in_data[0].a.text)
symbol = open('symbol_collection.txt','w+')
for i in range(len(table)):
	data = table[i].find_all("tr")
	for j in range(1,len(data)):
		in_data=data[j].find_all("td")
		string = '"'+in_data[0].a.text+'" : '+"'"+str(in_data[1].text)+"'"+',\n'
		symbol.write(string)
