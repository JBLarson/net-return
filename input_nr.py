#user defined function
def gamble(y,z):
	return y*(z-1)

#tp/spr input variables
o1s, o1o, o1r = float(40), float(1.952), float(40)

u1s, u1o, u1r = float(44), float(1.76), float(50)

f1s, f1o, f1r = float(-3), float(1.67), float(55)

d1s, d1o, d1r = float(5), float(1.87), float(45)

#variables defining pts covered by visual
exp_spr = -4
spr_pts = range(exp_spr-6, exp_spr+6)

avg_tp = (o1s + u1s)/2
lo_tp = int(avg_tp - 6)
hi_tp = int(avg_tp + 6)
tp_pts = range(lo_tp, hi_tp)


#tp/spr win variables
o1w = round(gamble(o1r,o1o),ndigits=2)
u1w = round(gamble(u1r,u1o),ndigits=2)
f1w = round(gamble(f1r,f1o),ndigits=2)
d1w = round(gamble(d1r,d1o),ndigits=2)

#describe bets

print("Over:",o1s,"pts - Risks: $",o1r,"Net: $",o1w)
print("Under:",u1s,"pts - Risks: $",u1r,"Net: $",u1w)
print()
print("Fav:",f1s,"pt - Risks: $",f1r,"Net: $",f1w)
print("Dog:",d1s,"pt - Risks: $",d1r,"Net: $",d1w)
print()

