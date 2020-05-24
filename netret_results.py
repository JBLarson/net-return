from pandas import DataFrame
import pandas as pd
import numpy as np

import input_twob_model as tp
import input_spr_model as inp

#localize input variables
fb1s = inp.b1s
db2s = inp.b2s
fb1r = inp.b1r
db2r = inp.b2r
fb1w = inp.b1w
db2w = inp.b2w

ob1s = tp.b1s
ub2s = tp.b2s
ob1r = tp.b1r
ub2r = tp.b2r
ob1w = tp.b1w
ub2w = tp.b2w

tp_range = []
tp_df = DataFrame()
ob1_rez = []
ub2_rez = []

spr_range = []
spr_df = DataFrame()
fb1_rez = []
db2_rez = []

net0 = []
net1 = []
net2 = []
net3 = []
net4 = []
net5 = []
net6 = []

spr0 = []
spr1 = []
spr2 = []
spr3 = []
spr4 = []
spr5 = []
spr6 = []

xm0 = []
xm1 = []
xm2 = []
xm3 = []
xm4 = []
xm5 = []
xm6 = []

ym0 = []
ym1 = []
ym2 = []
ym3 = []
ym4 = []
ym5 = []
ym6 = []



tp_pts = range(40, 46)
spr_pts = range(-4, 2)

for num in tp_pts:
	tp_range.append(num)
tp_df['tp'] = tp_range

for num in spr_pts:
	spr_range.append(num)
spr_df['spr'] = spr_range

#find df results for over
for pt in tp_pts:
	if pt < ob1s:
		ob1_rez.append(-ob1r)
	elif pt >= ob1s:
		ob1_rez.append(ob1w)
#find df results for under
for pt in tp_pts:
	if pt > ub2s:
		ub2_rez.append(-ub2r)
	elif pt <= ub2s:
		ub2_rez.append(ub2w)

#find df results for fav bets (-spr)
for pt in spr_pts:
	if pt >= fb1s:
		fb1_rez.append(-fb1r)
	elif pt < fb1s:
		fb1_rez.append(fb1w)

#find df results for dog bets (+spr)
for pt in spr_pts:
	if pt < 0:	
		if abs(pt) >= db2s:
			db2_rez.append(-db2r)
		elif abs(pt) < db2s:
			db2_rez.append(db2w)
	elif pt >= 0:
		if db2s >= 0:	
			db2_rez.append(db2w)

#append lists to df's and create net df's
tp_df['ob1'] = ob1_rez
tp_df['ub2'] = ub2_rez
tp_df['tp_net'] = round((tp_df['ob1'] + tp_df['ub2']), ndigits=2)

spr_df['fb1'] = fb1_rez
spr_df['db2'] = db2_rez
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
