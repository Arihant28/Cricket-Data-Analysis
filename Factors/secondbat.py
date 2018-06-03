import pandas as pd
import csv


def SECONDBAT(second):
	Location = "/home/akshay/Desktop/Cricket Data Analysis/Team_Versus/India/" + second + "/Match.csv"
	df = pd.read_csv(Location)
	tot = 0
	score = 0
	for index,j in df.iterrows():
		if j['BAT'] == 2:
			if j['WINNER'] == second:
				a = j['MARGIN']
				score = score + j['SCORE'] + int(a[:-4])
				tot += 1
			elif j['WINNER'] == 'India':
				score += j['SCORE']
				tot += 1

	a = int (score) / tot
	More_win = 0
	More_loss = 0
	Less_win = 0
	Less_loss = 0
	total = 0
	v = 0
	for index,i in df.iterrows():
		if i['BAT'] == 2:

			if i['SCORE'] <= a :
				v = 1
				if i['WINNER'] == "India":
					More_win += 1
					total += 1
				elif i['WINNER'] == second :
					More_loss += 1
					total += 1
				else :
					total += 1

			elif i['WINNER'] != 'no result' or i['WINNER'] != 'abandoned' or i['WINNER'] != 'cancelled':
				v = 1
				if i['WINNER'] == "India":
					Less_win += 1
					total += 1
				elif i['WINNER'] == second :
					Less_loss += 1
					total += 1
			else :
				total += 1
	
	if v == 1 :
		print("Performace of India chasing less than " + str("{0:.0f}".format(a)) + " vs " + second + " : " +  str(More_win) + " Wins out of " + str(More_win + More_loss))


				
