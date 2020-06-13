from pandas import DataFrame
import pandas as pd

#1a create lambda to find win
g = lambda r, o : r * (o-1)

#1b tp/spr input variables
o1s, o1o, o1r = float(40), float(1.9), float(40)
u1s, u1o, u1r = float(44), float(1.7), float(50)
f1s, f1o, f1r = float(-3), float(1.67), float(60)
d1s, d1o, d1r = float(5), float(1.87), float(50)

#1c create pt ranges for stats and visual
exp_spr = -4
spr_pts = range(exp_spr-6, exp_spr+6)
avg_tp = (o1s + u1s)/2
lo_tp = int(avg_tp - 6)
hi_tp = int(avg_tp + 6)
tp_pts = range(lo_tp, hi_tp)
 
#1d tp/spr win variables
o1w, u1w, f1w, d1w = g(o1r, o1o), g(u1r,u1o), g(f1r,f1o), g(d1r,d1o)


#1e create (t)p and (s)pr variables, create 4-way scenario variables (over/under/fav/dog)
tww, twL, tLw = o1w + u1w, o1w - u1r, u1w - o1r
sww, swL, sLw = f1w + d1w, f1w - d1r, d1w - f1r

wLwL, wLww, wLLw = twL + swL, twL + sww, twL + sLw
wwwL, wwww, wwLw = tww + swL, tww + sww, tww + sLw #all tp win-win values
LwwL, Lwww, LwLw = tLw + swL, tLw + sww, tLw + sLw

scenarios = {1: wLwL, 2: wLww, 3: wLLw, 4: wwwL, 5: wwww, 6: wwLw, 7: LwwL, 8: Lwww, 9: LwLw}
scn_list = [scenarios[scn] for scn in scenarios]

#tp / spr scenario dictionaries & lists
scntp = [swL, sww, sLw, swL, sww, sLw, swL, sww, sLw]
scnspr = [twL, twL, twL, tww, tww, tww, tLw, tLw, tLw]

sscwL, sscww, sscLw = [wLwL, wwwL, LwwL], [wLww, wwww, Lwww], [wLLw, wwLw, LwLw]
tscwL, tscww, tscLw = [wLwL, wLww, wLLw], [wwwL, wwww, wwLw], [LwwL, Lwww, LwLw]

# <DataFrame> scenario matrix w/ tpscn as columns
tdf = pd.DataFrame({'wLtp': tscwL, 'wwtp': tscww, 'Lwtp': tscLw}, index = ['wLspr', 'wwspr', 'Lwspr'])

# <DataFrame> scenario sum and diff
key = ['wLwL', 'wwwL', 'LwwL', 'wLww', 'wwww', 'Lwww', 'wLLw', 'wwLw', 'LwLw']
scndf = pd.DataFrame({'key': key, 'scn($)': scn_list, 'tp($)': scntp, 'spr($)': scnspr})

