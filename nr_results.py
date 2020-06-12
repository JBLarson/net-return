from pandas import DataFrame
import pandas as pd
import numpy as np

import input_nr as inp

#localize input variables
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

tp_range = []
tp_df = DataFrame()
o1_rez = []
u1_rez = []

spr_range = []
spr_df = DataFrame()
f1_rez = []
d1_rez = []

net0 = []
net1 = []
net2 = []
net3 = []
net4 = []
net5 = []
net6 = []
net7 = []
net8 = []
net9 = []

spr0 = []
spr1 = []
spr2 = []
spr3 = []
spr4 = []
spr5 = []
spr6 = []
spr7 = []
spr8 = []
spr9 = []

xm0 = []
xm1 = []
xm2 = []
xm3 = []
xm4 = []
xm5 = []
xm6 = []
xm7 = []
xm8 = []
xm9 = []

ym0 = []
ym1 = []
ym2 = []
ym3 = []
ym4 = []
ym5 = []
ym6 = []
ym7 = []
ym8 = []
ym9 = []


tp_pts = inp.tp_pts
spr_pts = inp.spr_pts

for num in tp_pts:
	tp_range.append(num)
tp_df['tp'] = tp_range

for num in spr_pts:
	spr_range.append(num)
spr_df['spr'] = spr_range

#find df results for over
for pt in tp_pts:
	if pt < o1s:
		o1_rez.append(-o1r)
	elif pt >= o1s:
		o1_rez.append(o1w)
#find df results for under
for pt in tp_pts:
	if pt > u1s:
		u1_rez.append(-u1r)
	elif pt <= u1s:
		u1_rez.append(u1w)

#find df results for fav bets (-spr)
for pt in spr_pts:
	if pt >= f1s:
		f1_rez.append(-f1r)
	elif pt < f1s:
		f1_rez.append(f1w)

#find df results for dog bets (+spr)
for pt in spr_pts:
	if pt < 0:	
		if abs(pt) >= d1s:
			d1_rez.append(-d1r)
		elif abs(pt) < d1s:
			d1_rez.append(d1w)
	elif pt >= 0:
		if d1s >= 0:	
			d1_rez.append(d1w)

#append lists to df's and create net df's
tp_df['ob1'] = o1_rez
tp_df['ub2'] = u1_rez
tp_df['tp_net'] = round((tp_df['ob1'] + tp_df['ub2']), ndigits=2)

spr_df['fb1'] = f1_rez
spr_df['db2'] = d1_rez
spr_df['spr_net'] = round((spr_df['fb1'] + spr_df['db2']), ndigits=2)

#create df variables from dataframes
dtp_net = DataFrame(tp_df['tp_net'])
dtp_scores = DataFrame(tp_df['tp'])
#create df variables from dataframes
dspr_net = DataFrame(spr_df['spr_net'])
dspr_scores = DataFrame(spr_df['spr'])

#create numpy array variables from df variables
ntp_net = np.array(dtp_net[0:]).tolist()
ntp_scores = np.array(dtp_scores[0:]).tolist()
#create numpy array variables from df variables
nspr_net = np.array(dspr_net[0:]).tolist()
nspr_scores = np.array(dspr_scores[0:]).tolist()

#create array variables from numpy array variables
tp_scores = ntp_scores
spr_scores = nspr_scores

#tp/spr net w/o rounding
tp_net = ntp_net
spr_net = nspr_net


n3t = DataFrame({'pts':tp_scores, 'tp_net':tp_net, 'score':spr_scores, 'spr_net':spr_net})


