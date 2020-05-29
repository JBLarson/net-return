from pandas import DataFrame
import pandas as pd


import input_nr as inp

#Localize input variabLes
o1s = inp.o1s
u1s = inp.u1s
o1r = inp.o1r
u1r = inp.u1r
o1w = inp.o1w
u1w = inp.u1w

f1s = inp.f1s
d1s = inp.d1s
f1r = inp.f1r
d1r = inp.d1r
f1w = inp.f1w
d1w = inp.d1w


o1_rez = [o1w if n >= o1s else -o1r for n in inp.tp_pts]

u1_rez = [-u1r if n >= u1s else u1w for n in inp.tp_pts]

f1_rez = [-f1r if n >= f1s else f1w for n in inp.spr_pts]

#struggled with nested if function in list comprehension for dog

d1_rez = []

for pt in inp.spr_pts:
	if pt < 0:	
		if abs(pt) >= d1s:
			d1_rez.append(-d1r)
		elif abs(pt) < d1s:
			d1_rez.append(d1w)
	elif pt >= 0:
		if d1s >= 0:	
			d1_rez.append(d1w)


#assign (t)otal point and (s)pread scenario variables

tww = o1w + u1w
twL = o1w - u1r
tLw = u1w - o1r

sww = f1w + d1w
swL = f1w - d1r
sLw = d1w - f1r

#scenario variables are named in the order of over / under / fav / dog

wLwL = twL + swL #u40 u44 f < -3 | d > 5
wLww = twL + sww #u40 u44 f < -3 | d < 5
wLLw = twL + sLw #u40 u44 f > -3 | d < 5

wwwL = tww + swL #o40 u44 f < -3 | d > 5
wwww = tww + sww #o40 u44 f < -3 | d < 5
wwLw = tww + sLw #o40 u44 f > -3 | d < 5

LwwL = tLw + swL #o40 o44 f < -3 | d > 5
Lwww = tLw + sww #o40 o44 f < -3 | d < 5
LwLw = tLw + sLw #o40 o44 f > -3 | d < 5

scenarioL = []

scenarios = {1: wLwL, 2: wLww, 3: wLLw, 4: wwwL, 5: wwww, 6: wwLw, 7: LwwL, 8: Lwww, 9: LwLw}

for scn in scenarios:
	scenarioL.append(scenarios[scn])

#create lists by spread scenario of all scenarios
sscwL = [wLwL, wwwL, LwwL]
sscww = [wLww, wwww, Lwww]
sscLw = [wLLw, wwLw, LwLw]
sscwL_avg = (sum(sscwL)/ 3)
sscww_avg = (sum(sscww)/ 3)
sscLw_avg = (sum(sscLw)/ 3)

avgsc = round((sum(scenarioL)/9), ndigits=4)




print("Average scenario: $", (avgsc))

#lists w/ 3 total pt scenarios of all scenarios
tscwL = [wLwL, wLww, wLLw]
tscww = [wwwL, wwww, wwLw]
tscLw = [LwwL, Lwww, LwLw]

key = ['wLwL', 'wwwL', 'LwwL', 'wLww', 'wwww', 'Lwww', 'wLLw', 'wwLw', 'LwLw']


twLd = []
twwd = []
tLwd = []

tdm0 = []
sdm0 = []

tscwL_avg = (sum(tscwL)/ 3)
tscww_avg = (sum(tscww)/ 3)
tscLw_avg = (sum(tscLw)/ 3)


for n in [0]:
	for s in [f'((tscwL[0]-tscwL_avg)/tscwL_avg)', f'((tscww[0]-tscww_avg)/tscww_avg)', f'((tscLw[0]-tscLw_avg)/tscLw_avg)', f'((tscwL[1]-tscwL_avg)/tscwL_avg)', f'((tscww[1]-tscww_avg)/tscww_avg)', f'((tscLw[1]-tscLw_avg)/tscLw_avg)', f'((tscwL[2]-tscwL_avg)/tscwL_avg)', f'((tscww[2]-tscww_avg)/tscww_avg)', f'((tscLw[2]-tscLw_avg)/tscLw_avg)']:
		eval(f'tdm{n}').append(round(eval(s), ndigits=1))




for n in [0]:
	for s in [f'((sscwL[0]-sscwL_avg)/sscwL_avg)', f'((sscww[0]-sscww_avg)/sscww_avg)', f'((sscLw[0]-sscLw_avg)/sscLw_avg)', f'((sscwL[1]-sscwL_avg)/sscwL_avg)', f'((sscww[1]-sscww_avg)/sscww_avg)', f'((sscLw[1]-sscLw_avg)/sscLw_avg)', f'((sscwL[2]-sscwL_avg)/sscwL_avg)', f'((sscww[2]-sscww_avg)/sscww_avg)', f'((sscLw[2]-sscLw_avg)/sscLw_avg)']:
		eval(f'sdm{n}').append(round(eval(s), ndigits=1))




#key = ['wLwL', '']

netdf = pd.DataFrame({'key': key, 'tp': tdm0, 'spr': sdm0})

netdf_nokey = pd.DataFrame({'tp': tdm0, 'spr': sdm0})


for scn in tscwL:
	twLd.append((scn - tscwL_avg)/tscwL_avg)

tsc_avgs = [tscwL_avg, tscww_avg, tscLw_avg]

ssc_avgs = [sscwL_avg, sscww_avg, sscLw_avg]

scnstr = ['wL', 'ww', 'Lw']


tdf = pd.DataFrame({'tpsc': scnstr, 'wL': tscwL, 'ww': tscww, 'Lw': tscLw})

print()
print("tp_scenario (columns) x spr_scenario matrix")
print(tdf)


print()
print(tdf.describe())



print()
print("Deviation from mean (i - µ)/µ DataFrame")

print(netdf)





print()
