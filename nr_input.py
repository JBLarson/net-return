from pandas import DataFrame
import pandas as pd

#create lambda to find win
g = lambda r, o : r * (o-1)

#tp/spr input variables (score, odds, risk)
o1s, o1o, o1r = float(40), float(1.9), float(0)
u1s, u1o, u1r = float(46), float(1.7), float(0)
f1s, f1o, f1r = float(-4), float(1.67), float(10)
d1s, d1o, d1r = float(3), float(2.25), float(0)

#create pt ranges for stats and visual
exp_spr = 0
lo_spr = exp_spr-6
hi_spr = exp_spr+6
spr_pts = range(lo_spr, hi_spr)

#avg_tp = (o1s + u1s)/2
exp_tp = 44
lo_tp = int(exp_tp - 8)
hi_tp = int(exp_tp + 4)
tp_pts = range(lo_tp, hi_tp)


#tp/spr win variables
o1w, u1w, f1w, d1w = g(o1r, o1o), g(u1r,u1o), g(f1r,f1o), g(d1r,d1o)
