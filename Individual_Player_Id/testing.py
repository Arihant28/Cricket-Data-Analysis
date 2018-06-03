import requests
import csv
from bs4 import BeautifulSoup
from sets import Set
import pandas
#(Player_id.country_code)
url = "http://www.espncricinfo.com/australia-v-india-2015-16/engine/match/895807.html"
souce_code = requests.get(url).text
soup = BeautifulSoup(souce_code,"html.parser")
right_table = soup.find('table',{'class':'batting-table innings'})
for row in right_table.findAll("tr"):
	for cells in row.findAll('a',{'class':'playerName'}):
		if cells.string == 'MS Dhoni':
			for ce in row.find('td',{'class':'bold'}):
				print(ce)

		 

	     
	
	
