import Winloss as wl 
import Batpos as bp
import Venue as v 
import score as s
import secondbat as bs
import Viratfirstbat as vf
import viratsecondbat as vs 
import ashwinsecond as ashs
import ashwinfirst as af 

country_code = ["England","Australia","South Africa","West Indies","New Zealand","India","Pakistan","Sri Lanka","Zimbabwe"]
opp = raw_input("Enter the opponent team : ")
if opp in country_code:
	ven = raw_input("Enter the venue of match : ")
	inni = raw_input("India batting first or second : ")
	print ('Enter the key players')
	batsman = raw_input("Batsman: ")
	bowler = raw_input("Bowler: ")

	if inni == 'first':
		wl.Win_Loss(opp)
		v.VENUE(opp,ven)
		bp.VENUE(opp,ven,1)
		s.SCORE(opp)
		vf.viratruns(opp,batsman)
		ashs.ashsecond(opp,bowler)

	elif inni == 'second' :
		wl.Win_Loss(opp)
		v.VENUE(opp,ven)
		bp.VENUE(opp,ven,2)
		bs.SECONDBAT(opp)
		vs.viratruns(opp,batsman)
		af.ashfirst(opp,bowler)
		

	else :
		print ("----- Please provide the valid input -----")

else:
	print ("----- Please provide the valid input -----")
