import pandas as pd
import csv
#from sets import Set

def Win_Loss(second):
	Location = "/home/akshay/Desktop/Cricket Data Analysis/Team_Versus/India/" + second + "/Match.csv"
	df = pd.read_csv(Location)
	
	count_opp = 0
	count_ind = 0
	count_noresult = 0
	total = 0
	for i in df['WINNER']:
		if  i == 'India':
			count_ind += 1
			total += 1
		elif i == 'England':
			count_opp += 1
			total += 1
		else :
			count_noresult +=1
			total += 1

	print ("India head to head vs " + second + " :" + str(count_ind) + " Wins out of " + str(total))
	 

