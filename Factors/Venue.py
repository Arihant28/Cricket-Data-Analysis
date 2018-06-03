import pandas as pd
import csv

def VENUE(second,venue):
	Location = "/home/akshay/Desktop/Cricket Data Analysis/Team_Versus/India/" + second + "/Match.csv"
	df = pd.read_csv(Location)
	
	count_opp = 0
	count_ind = 0
	count_noresult = 0
	total = 0
	c=0
	Last = []
	for index,i in df.iterrows():
		if i['VENUE'] == venue:
			c=1
			if  i['WINNER'] == 'India':
				count_ind += 1
				total += 1
				Last.append("W")
			elif i['WINNER'] == second:
				count_opp += 1
				total += 1
				Last.append("L")
			else :
				count_noresult +=1
				total += 1
				Last.append("T/D")

	if c==1:
		print ("Performance of India after 2009 at " + venue + " vs " + second + " : " + str(",".join(Last)))
	else :
		print ("First ever ODI game for India at " + venue + " vs " + second)

