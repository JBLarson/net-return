from pandas import DataFrame
import pandas as pd

import input_nr as inp

#Localize input variabLes
o1s, u1s, o1r, u1r, o1w, u1w = inp.o1s, inp.u1s, inp.o1r, inp.u1r, inp.o1w, inp.u1w
f1s, d1s, f1r, d1r, f1w, d1w = inp.f1s, inp.d1s, inp.f1r, inp.d1r, inp.f1w, inp.d1w

#assign net return for all scores in range of analysis for each type of bet
o1_rez = [o1w if n >= o1s else -o1r for n in inp.tp_pts]
u1_rez = [-u1r if n >= u1s else u1w for n in inp.tp_pts]
f1_rez = [-f1r if n >= f1s else f1w for n in inp.spr_pts]
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

#assign (t)otal point and (s)pread scenario-specific variables
tww, twL, tLw = o1w + u1w, o1w - u1r, u1w - o1r
sww, swL, sLw = f1w + d1w, f1w - d1r, d1w - f1r

#netret scenario notation: over / under / fav / dog
wLwL, wLww, wLLw = twL + swL, twL + sww, twL + sLw
wwwL, wwww, wwLw = tww + swL, tww + sww, tww + sLw #all tp win-win values
LwwL, Lwww, LwLw = tLw + swL, tLw + sww, tLw + sLw

scenarios = {1: wLwL, 2: wLww, 3: wLLw, 4: wwwL, 5: wwww, 6: wwLw, 7: LwwL, 8: Lwww, 9: LwLw}

#tp / spr scenario dictionaries & lists
scntpd = {1: swL, 2: sww, 3: sLw, 4: swL, 5: sww, 6: sLw, 7: swL, 8: sww, 9: sLw}
scnsprd = {1: twL, 2: twL, 3: twL, 4: tww, 5: tww, 6: tww, 7: tLw, 8: tLw, 9: tLw}
scntp = [swL, sww, sLw, swL, sww, sLw, swL, sww, sLw]
scnspr = [twL, twL, twL, tww, tww, tww, tLw, tLw, tLw]

scn_list = [scenarios[scn] for scn in scenarios]

#spread / tp scenario lists
sscwL, sscww, sscLw = [wLwL, wwwL, LwwL], [wLww, wwww, Lwww], [wLLw, wwLw, LwLw]
sscwL_avg, sscww_avg, sscLw_avg = (sum(sscwL)/ 3), (sum(sscww)/ 3), (sum(sscLw)/ 3)
tscwL, tscww, tscLw = [wLwL, wLww, wLLw], [wwwL, wwww, wwLw], [LwwL, Lwww, LwLw]
tscwL_avg, tscww_avg, tscLw_avg = (sum(tscwL)/ 3), (sum(tscww)/ 3), (sum(tscLw)/ 3)

#avg tp / spr nested lists
tsc_avgs, sscLw_avgs = [tscwL_avg, tscww_avg, tscLw_avg], [sscwL_avg, sscww_avg, sscLw_avg]

# <DataFrame> scenario matrix w/ tpscn as columns
tdf = pd.DataFrame({'wLtp': tscwL, 'wwtp': tscww, 'Lwtp': tscLw}, index = ['wLspr', 'wwspr', 'Lwspr'])

# <DataFrame> scenario sum and diff
key = ['wLwL', 'wwwL', 'LwwL', 'wLww', 'wwww', 'Lwww', 'wLLw', 'wwLw', 'LwLw']
scndf = pd.DataFrame({'key': key, 'scn($)': scn_list, 'tp($)': scntp, 'spr($)': scnspr})

print("Scenario Matrix\n")
print(tdf)
print("\nTP Scenario Stats")
print(tdf.describe())
print("\nScenario ∑ & ∆ DataFrame\n")
print(scndf)

print()

import surf4
