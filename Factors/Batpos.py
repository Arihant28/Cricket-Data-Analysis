import pandas as pd
import csv

def VENUE(second,venue,pos):
	Location = "/home/akshay/Desktop/Cricket Data Analysis/Team_Versus/India/" + second + "/Match.csv"
	df = pd.read_csv(Location)
	
	count_opp = 0
	count_ind = 0
	count_noresult = 0
	total = 0
	c=0
	batfirst_Venue_win=0
	batfirst_Venue_loss=0
	batfirst_NVenue_win=0
	batfirst_NVenue_loss=0
	Last = []

	batSecond_Venue_win=0
	batSecond_Venue_loss=0
	batSecond_NVenue_win=0
	batSecond_NVenue_loss=0
	

	v = 0
	bat_first=0
	bat_second=0
	
	for index,i in df.iterrows():
		#print (pos)
		if i['BAT'] == 1 :
			c=1
			f = 1
			bat_first += 1
			if i['VENUE'] == venue:
				#v =1
				if i['WINNER'] == 'India':
					batfirst_Venue_win += 1
					total += 1
					Last.append("W")
				elif i['WINNER'] == second :
					batfirst_Venue_loss += 1
					total += 1
					Last.append("L")
				else :
					count_noresult +=1
					total += 1
					Last.append("T/D")
			else :
				
				if i['WINNER'] == 'India':
					
					batfirst_NVenue_win += 1
					total += 1
					Last.append("W")
				elif i['WINNER'] == second :
					batfirst_NVenue_loss += 1
					total += 1
					Last.append("L")
				else :
					count_noresult +=1
					total += 1
					Last.append("T/D")
		elif i['BAT'] == 2 :
			bat_second += 1 
			c=1
			f = 2
			if i['VENUE'] == venue:
				v = 1
				if i['WINNER'] == 'India':
					batSecond_Venue_win += 1
					total += 1
					Last.append("W")
				elif i['WINNER'] == second:
					batSecond_Venue_loss += 1
					total += 1
					Last.append("L")
				else :
					count_noresult +=1
					total += 1
					Last.append("T/D")
			else :
				if i['WINNER'] == 'India':
					batSecond_NVenue_win += 1
					total += 1
					Last.append("W")
				elif i['WINNER'] == second:
					batSecond_NVenue_loss += 1
					total += 1
					Last.append("L")
				else :
					count_noresult +=1
					total += 1
					Last.append("T/D")
		else :
			
			count_noresult +=1
			total += 1
			Last.append("T/D")

		

	if pos == 1 :
		print("Performance of India batting first at " + venue + " vs " + second + " : "  + str(batfirst_Venue_win) + " Wins out of " + str(batfirst_Venue_win + batfirst_Venue_loss) )
		print("Performance of India batting first vs " + second + " : " + str(batfirst_Venue_win + batfirst_NVenue_win) + " Wins out of " + str(bat_first))
	
	elif pos == 2 :
		print("Performance of India batting second vs " + second + " : " + str(batSecond_Venue_win + batSecond_NVenue_win) + " Wins out of " + str(bat_second))
		print("Performance of India batting second at " + venue + " vs " + second + " : "  + str(batSecond_Venue_win) + " Wins out of " + str(batSecond_Venue_win + batSecond_Venue_loss) )
	
	