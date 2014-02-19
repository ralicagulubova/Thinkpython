 # If he walks from A to B and then from B to A whit the same tempo, he has to walk 10 miles 
... timeAB=2*495+3*432
>>> timeAB
2286
>>> timeBA=timeAB
>>> timeBA
2286
>>> totaltimesec=timeAB+timeBA
>>> totaltimesec
4572
>>> totaltimemin=totaltimesec/60
>>> totaltimemin
76
# He will be at home after 76min (8:08)
 #If he walks in a circle(from A to A), he has to walk only 5 miles
... timesec=2*495+3*432
>>> timesec
2286
>>> timemin=timesec/60
>>> timemin
38
>>> #He will be at home after 38 min ( at 7:30)
