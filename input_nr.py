#user defined function
def gamble(y,z):
	return round((y*(z-1)),ndigits=2)

#over and under inputs
o1s = float(45)
o1t = ("o")
o1o = float(1.67)
o1r = float(30)

u1s = float(47)
u1t = ("u")
u1o = float(1.76)
u1r = float(50)

#favorite and dog inputs
f1s = float(-7)
f1t = ("f")
f1o = float(1.67)
f1r = float(80)

d1s = float(9)
d1t = ("d")
d1o = float(1.76)
d1r = float(60)


exp_spr = -8
spr_pts = range(exp_spr-6, exp_spr+6)

avg_tp = (o1s + u1s)/2
lo_tp = int(avg_tp - 6)
hi_tp = int(avg_tp + 6)
tp_pts = range(lo_tp, hi_tp)







o1w = round(gamble(o1r,o1o),ndigits=2)
u1w = round(gamble(u1r,u1o),ndigits=2)

f1w = round(gamble(f1r,f1o),ndigits=2)
d1w = round(gamble(d1r,d1o),ndigits=2)

#define combination variables

if o1t == 'o' and u1t == 'u':
	tpcomb = 'ou'
elif o1t == 'u' and u1t == 'o':
	tpcomb = 'uo'

if f1t == 'f' and d1t == 'd':
	comb = 'fd'
elif f1t == 'd' and d1t == 'f':
	comb = 'df'


#describe bets

print()
print("Total Points Bets")

if tpcomb == 'ou':
	print("Bet 1 | Over:",o1s,"pts - Risks: $",o1r,"Nets: $",o1w)
	print("Bet 2 | Under:",u1s,"pts - Risks: $",u1r,"Nets : $",u1w)

elif tpcomb == 'uo':
	print("Bet 1 | Under:",o1s,"pts - Risks $",o1r,"Nets: $",u1w)
	print("Bet 2 | Over:",u1s,"pts - Risks: $",u1r,"Nets: $",o1w)

print()
print("Spread Bets")

if comb == 'fd':
	print("Bet 1 | fav:",f1s,"pt - Risks: $",f1r,"Net: $",f1w)
	print("Bet 2 | dog:",d1s,"pt - Risks $",d1r,"Net: $",d1w)
elif comb == 'df':
	print("Bet 1 | dog:",d1s,"pt - Risks: $",d1r,"Net: $",d1w)
	print("Bet 2 | fav:",f1s,"pt - Risks: $",f1r,"Net : $",f1w)

