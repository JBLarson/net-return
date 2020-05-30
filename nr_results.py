from pandas import DataFrame
import pandas as pd
import numpy as np

import input_nr as inp

tp_df = DataFrame()
spr_df = DataFrame()

tp_range = [pt for pt in inp.tp_pts]
spr_range = [pt for pt in inp.spr_pts]

tp_df['tp'] = tp_range
spr_df['spr'] = spr_range

#find df results

o1_rez = [inp.o1w if n >= inp.o1s else -inp.o1r for n in inp.tp_pts]
u1_rez = [-inp.u1r if n >= inp.u1s else inp.u1w for n in inp.tp_pts]
f1_rez = [-inp.f1r if n >= inp.f1s else inp.f1w for n in inp.spr_pts]

#find df results for dog bets (struggled to create list comprehension because of +spr)

d1_rez = []

for pt in inp.spr_pts:
	if pt < 0:	
		if abs(pt) >= inp.d1s:
			d1_rez.append(-inp.d1r)
		elif abs(pt) < inp.d1s:
			d1_rez.append(inp.d1w)
	elif pt >= 0:
		if inp.d1s >= 0:	
			d1_rez.append(inp.d1w)



#append lists to df's and create net df's
tp_df['o1'] = o1_rez
tp_df['u1'] = u1_rez
tp_df['tp_net'] = round((tp_df['o1'] + tp_df['u1']), ndigits=2)

spr_df['f1'] = f1_rez
spr_df['d1'] = d1_rez
spr_df['spr_net'] = round((spr_df['f1'] + spr_df['d1']), ndigits=2)

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
tp_net = ntp_net
spr_net = nspr_net

n3t = DataFrame({'pts':tp_scores, 'tp_net':tp_net, 'score':spr_scores, 'spr_net':spr_net})

xm0, xm1, xm2, xm3, xm4, xm5 = [], [], [], [], [], []
xm6, xm7, xm8, xm9, xm10, xm11= [], [], [], [], [], []

#create list mapping x-values
for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
	for s in [f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))']:
		eval(f'xm{n}').append(eval(s))

xmap = (xm0, xm1, xm2, xm3, xm4, xm5, xm6, xm7, xm8, xm9, xm10, xm11)

ym0, ym1, ym2, ym3, ym4, ym5 = [], [], [], [], [], []
ym6, ym7, ym8, ym9, ym10, ym11= [], [], [], [], [], []


#create list mapping y-values
for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
	for s in [f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))']:
		eval(f'ym{n}').append(eval(s))

ymap = (ym0, ym1, ym2, ym3, ym4, ym5, ym6, ym7, ym8, ym9, ym10, ym11)


net0, net1, net2, net3, net4, net5 = [], [], [], [], [], []
net6, net7, net8, net9, net10, net11= [], [], [], [], [], []

for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
	for s in [f'sum(tp_net[11]+spr_net[{n}])', f'sum(tp_net[10]+spr_net[{n}])', f'sum(tp_net[9]+spr_net[{n}])', f'sum(tp_net[8]+spr_net[{n}])', f'sum(tp_net[7]+spr_net[{n}])', f'sum(tp_net[6]+spr_net[{n}])', f'sum(tp_net[5]+spr_net[{n}])', f'sum(tp_net[4]+spr_net[{n}])', f'sum(tp_net[3]+spr_net[{n}])', f'sum(tp_net[2]+spr_net[{n}])', f'sum(tp_net[1]+spr_net[{n}])', f'sum(tp_net[0]+spr_net[{n}])']:
		eval(f'net{n}').append(eval(s))

net_map = np.array([net0, net1, net2, net3, net4, net5, net6, net7, net8, net9, net10, net11])

