import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

#broken_df = pd.read_csv('/home/akshay/Desktop/Cricket Data Analysis/Individual_Player_Id/India_Player_id.csv') 
#df = pd.DataFrame(data = broken_df, columns=['Names', 'Births'])  
#df = pd.read_csv('/home/akshay/Desktop/Cricket Data Analysis/Individual_Player_Id/'+'India'+'_Player_id.csv')
#print df['NAMES']
#http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id=1;id=2;type=headtohead
country_code = [("England",1),("Australia",2),("South Africa",3),("West Indies",4),("New Zealand",5),("India",6),("Pakistan",7),("Sri Lanka",8),("Zimbabwe",9)]
for opp in country_code:
	print (opp)
	if not opp[0] == 'India':

		Location = '/home/akshay/Desktop/Cricket Data Analysis/Team_Versus/India/' + opp[0] +'/Match.csv'
		Location1 = '/home/akshay/Desktop/Cricket Data Analysis/Individual_Player_Id/India_Player_id.csv'
		df = pd.read_csv(Location)
		df1 = pd.read_csv(Location1)
		#print df1.NAMES
		for index,j in df1.iterrows():
			#print j
			runs = []
			bat = []
			winner = []
			c=0
			pr = j['PLAYING_ROLE']
			print(pr)
			if pr[-4:] == 'sman' or pr == 'Allrounder': 	# itterrows() help to iterate over a row , index wise
				for index,i in df.iterrows():
					url = i['MATCH_ID']
					#print url
					souce_code = requests.get(url).text
					soup = BeautifulSoup(souce_code,"html.parser")
					for tables in soup.findAll('table',{'class':'batting-table innings'}):
						for row in tables.findAll("tr"):
							for cells in row.findAll('a',{'class':'playerName'}):
								if cells.string == j['NAMES']:
									for ce in row.find('td',{'class':'bold'}):
										runs.append(ce)
										c=1
										winner.append(i['WINNER'])
										bat.append(i['BAT'])

				if c==1:
					DataSet = list(zip(runs,winner,bat))
					df2 = pd.DataFrame(data = DataSet, columns=['RUNS','WINNER','BAT'])
					df2.to_csv('/home/akshay/Desktop/Cricket Data Analysis/Player_Versus/India/' + opp[0] + '/'+ j['NAMES']+'_Versus.csv',index=True,names=['RUNS','WINNER','BAT'])
	




#for cells in element.findAll('td',class_=lambda y: (y != 'td-icon-expand-collapse' and y != 'bowler-name')): 
# class_=lambda x: (x != 'tr-heading' and  x != 'dismissal-detail')