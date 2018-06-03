import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
country_code = [("England",1),("Australia",2),("South Africa",3),("West Indies",4),("New Zealand",5),("India",6),("Pakistan",7),("Sri Lanka",8),("Zimbabwe",9)]
for opp in country_code:
	if not opp[0] == 'India':

		Location = '/home/akshay/Desktop/Cricket Data Analysis/Team_Versus/India/' + opp[0] +'/Match.csv'
		Location1 = '/home/akshay/Desktop/Cricket Data Analysis/Individual_Player_Id/India_Player_id.csv'
		df = pd.read_csv(Location)
		df1 = pd.read_csv(Location1)
		for index,j in df1.iterrows():
			m = []
			e = []
			w = []
			bat = []
			pr = j['PLAYING_ROLE']
			d = 0
			if pr == "Bowler" or pr[:7] == "Bowling":
				for index,i in df.iterrows():
					c=0
					n =  []
					a = []
					url = i['MATCH_ID']
					print (url)
					souce_code = requests.get(url).text
					soup = BeautifulSoup(souce_code,"html.parser")
					for tables in soup.findAll('table',{'class': 'bowling-table'}):
						for rows in tables.findAll('tr',{'class':None}):
							for col in rows.findAll('td',{'class': 'bowler-name'}):
								if col.string == j['NAMES']:
									print(col.string)
									for col in rows.findAll('td',{'class':None}):
										if col.string != '\xa0':
											n.append(col.string)
											c = 1
				
					if c == 1:
						d = 1
						print (n)
						m.append(n[3])
						e.append(n[4])
						w.append(i['WINNER'])
						bat.append(i['BAT'])
						print (url)
						
				if d == 1:
					DataSet = list(zip(m,e,w,bat))
					df2 = pd.DataFrame(data = DataSet, columns=['WICKETS','ECONOMY','WINNER','BAT'])
					df2.to_csv('/home/akshay/Desktop/Cricket Data Analysis/Player_Versus/India/' + opp[0] + '/'+ j['NAMES']+'_Wicket_Versus.csv',index=True,names=['WICKETS','ECONOMY','WINNER','BAT'])


