import requests
import csv
from bs4 import BeautifulSoup
from sets import Set
import pandas as pd
country_code = [("England",1),("Australia",2),("South Africa",3),("West Indies",4),("New Zealand",5),("India",6),("Pakistan",7),("Sri Lanka",8),("Zimbabwe",9)] 
Test_code = 1
Odi_code = 2
for i in country_code:
	if not (i[0] == 'India'):
		url = 'http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id=6;id='+str(i[1])+';type=headtohead'
		souce_code = requests.get(url).text
		soup = BeautifulSoup(souce_code,"html.parser")
		margin=[]
		Bat=[]	
		venue=[]
		winner = []
		match_id = []
		Score = []
		for row in soup.findAll('tr',{'class':'data1'}):
			n_id=[]
			 
			for m_id in row.findAll('td'):
				bat = 0
				p = m_id.string
				n_id.append(p)
			q = n_id[5][-4:]
			if q > str(2009) and n_id[2] != '-':
				for link in row.findAll('a',href=lambda value: value and value.startswith('/ci/engine/match/')):
					a = 'http://www.espncricinfo.com' + link.get('href')
					match_id.append(a)
				venue.append(n_id[4])
				winner.append(n_id[2])
				margin.append(n_id[3])
				abond = 0
				
				if n_id[2] == 'India':
					if n_id[3][-4:] == 'runs':
						Bat.append('1')
						bat = 0
					if n_id[3][-7:] == 'wickets':
						Bat.append('2')
						bat = 1
				if n_id[2] == i[0]:
					if n_id[3][-4:] == 'runs':
						Bat.append('2')
						bat = 1
					if n_id[3][-7:] == 'wickets':
						Bat.append('1')
						bat = 0
				if n_id[2] == 'tied' or n_id[2] == 'no result' or n_id[2] == 'abandoned' or n_id[2] == 'cancelled':
					abond = 1
					Bat.append('0')
					Score.append(0)
				print a		
				if abond == 0:
					souce_code_total = requests.get(a).text
					soupt = BeautifulSoup(souce_code_total,"html.parser")
					tables = soupt.findAll('tr',{'class':'total-wrap'})
					#print tables[1]
					for total in tables[bat].findAll('td',{'class':'bold'}):
						Score.append(total.string)
				


		DataSet = list(zip(winner,Bat,margin,venue,match_id,Score))
		df = pd.DataFrame(data = DataSet, columns=['WINNER','BAT','MARGIN','VENUE','MATCH_ID','SCORE'])
		df.to_csv('/home/akshay/Desktop/Cricket Data Analysis/Team_Versus/India/'+i[0]+'/Match.csv',index=True,names=['WINNER','BAT','MARGIN','VENUE','MATCH_ID','SCORE'])


#right_table = soup.findAll('tr',{'class':'data1'})
#m_id = []
#for row in soup.findAll('tr',{'class':'data1'}):
#	for link in row.findAll('a',href=lambda value: value and value.startswith('/ci/engine/match/')):
#		h = link.get('href')
#		w = 'http://www.espncricinfo.com/' + h
#		souce_code1 = requests.get(w).text
#		soup1 = BeautifulSoup(souce_code1,"html.parser")
#		for date in soup1.findAll('div',{'class':'match-information-strip'}):
#			q=date.string[-9:-5]
#			print q
#		m_id.append(h)	


