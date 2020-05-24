#user defined function
def gamble(y,z):
	return round((y*(z-1)),ndigits=2)


#bet1 and bet2 input

b1s = float(42)
b1t = ("o")
b1o = float(1.67)
b1r = float(55)
b1r_t1 = b1r



b2s = float(44)
b2t = ("u")
b2o = float(1.76)
b2r = float(50)
b2r_t1 = b2r


#define combination variable
if b1t == 'o' and b2t == 'u':
	comb = 'ou'
elif b1t == 'u' and b2t == 'o':
	comb = 'uo'

b1w = round(gamble(b1r,b1o),ndigits=2)
b1L = -b1r
b2w = round(gamble(b2r,b2o),ndigits=2)
b2L = -b2r



#describe bets
print()
print("Total Points Bets")
if comb == 'ou':
	print("Bet 1 | Over:",b1s,"pts - Risks: $",b1r,"Nets: $",b1w)
	print("Bet 2 | Under:",b2s,"pts - Risks: $",b2r,"Nets : $",b2w)

elif comb == 'uo':
	print("Bet 1 | Under:",b1s,"pts - Risks $",b1r,"Nets: $",b1w)
	print("Bet 2 | Over:",b2s,"pts - Risks: $",b2r,"Nets: $",b2w)



#bet1 and bet2 input



fb1s = float(-1)
fb1t = ("f")
fb1o = float(1.67)
fb1r = float(30)




db2s = float(4)
db2t = ("d")
db2o = float(1.76)
db2r = float(40)





fb1w = round(gamble(fb1r,fb1o),ndigits=2)
db2w = round(gamble(db2r,db2o),ndigits=2)

#define combination variable
if fb1t == 'f' and db2t == 'd':
	comb = 'fd'
elif fb1t == 'd' and db2t == 'f':
	comb = 'df'

#describe bets
print()
print("Spread Bets")

if comb == 'fd':
	print("Bet 1 | fav:",fb1s,"pt - Risks: $",fb1r,"Net: $",fb1w)
	print("Bet 2 | dog:",db2s,"pt - Risks $",db2w,"Net: $",db2w)
elif comb == 'df':
	print("Bet 1 | dog:",fb1s,"pt - Risks: $",fb1r,"Net: $",fb1w)
	print("Bet 2 | fav:",db2s,"pt - Risks: $",db2r,"Net : $",db2w)

