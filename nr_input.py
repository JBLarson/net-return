#1a create lambda to find win
g = lambda r, o : r * (o-1)

#1b tp/spr input variables
o1s, o1o, o1r = float(40), float(1.9), float(40)
u1s, u1o, u1r = float(44), float(1.7), float(50)
f1s, f1o, f1r = float(-3), float(1.67), float(60)
d1s, d1o, d1r = float(5), float(1.87), float(50)

#1c variables defining pts covered by visual
exp_spr = -4
spr_pts = range(exp_spr-6, exp_spr+6)
avg_tp = (o1s + u1s)/2
lo_tp = int(avg_tp - 6)
hi_tp = int(avg_tp + 6)
tp_pts = range(lo_tp, hi_tp)
 
#1d tp/spr win variables
o1w, u1w, f1w, d1w = g(o1r, o1o), g(u1r,u1o), g(f1r,f1o), g(d1r,d1o)

#1e describe bets (toggle on/off with variable)
desc = False
#desc = True
if desc == True:

	print("Over:",o1s,"pts - Risks: $",o1r,"Net: $",round(o1w, ndigits=2))
	print("Under:",u1s,"pts - Risks: $",u1r,"Net: $",round(u1w, ndigits=2))
	print()
	print("Fav:",f1s,"pt - Risks: $",f1r,"Net: $",round(f1w, ndigits=2))
	print("Dog:",d1s,"pt - Risks: $",d1r,"Net: $",round(d1w, ndigits=2))
	print()
