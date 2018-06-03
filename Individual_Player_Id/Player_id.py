import requests
import csv
from bs4 import BeautifulSoup
#from sets import Set
import pandas as pd
country_code = [("England",1),("Australia",2),("South Africa",3),("West Indies",4),("New Zealand",5),("India",6),("Pakistan",7),("Sri Lanka",8),("Zimbabwe",9)] 
Test_code = 1
Odi_code = 2
for i in country_code:
	dest = i[0] + "_Player_id.csv"
	url = "http://www.espncricinfo.com/ci/content/player/index.html?country=" + str(i[1])
	souce_code = requests.get(url).text
	soup = BeautifulSoup(souce_code,"html.parser")
	h_set = []
	r_set = []
	role = []
	for name in range(10):
		for p_id in soup.findAll('a',href=lambda value: value and value.startswith('/ci/content/player/{0}'.format(name))):
			h = 'http://www.espncricinfo.com' + p_id.get('href')
			r = p_id.string 
			if h not in h_set and r not in r_set:
				#f.write(p_id.string + '\t' + h + '\n')
				h_set.append(h)
				r_set.append(r)
				purl = h
				souce_code_player = requests.get(purl).text
				soup_player = BeautifulSoup(souce_code_player,"html.parser")
				for pr in soup_player.findAll('p',{'class':'ciPlayerinformationtxt'}):
					if pr.b.string == 'Playing role':
						role.append(pr.span.string)
					
	DataSet = list(zip(r_set,h_set,role))
	df = pd.DataFrame(data = DataSet, columns=['NAMES', 'ID','PLAYING_ROLE'])
	df.to_csv(dest,index=True,names=['NAMES','ID','PLAYING _ROLE'])

	