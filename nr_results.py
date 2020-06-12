from pandas import DataFrame
import pandas as pd
import numpy as np

#2a import input_nr, create tp/spr DataFrames, add ranges to each
import input_nr as inp

tp_df = DataFrame()
spr_df = DataFrame()

tp_range = [pt for pt in inp.tp_pts]
spr_range = [pt for pt in inp.spr_pts]
tp_df['tp'] = tp_range
spr_df['spr'] = spr_range

#2b create lists with monetary results for each wager
o1_rez = [inp.o1w if n >= inp.o1s else -inp.o1r for n in inp.tp_pts]
u1_rez = [-inp.u1r if n >= inp.u1s else inp.u1w for n in inp.tp_pts]
f1_rez = [-inp.f1r if n >= inp.f1s else inp.f1w for n in inp.spr_pts]
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

#2c append lists to df's and calculate net results for each
tp_df['o1'] = o1_rez
tp_df['u1'] = u1_rez
tp_df['tp_net'] = round((tp_df['o1'] + tp_df['u1']), ndigits=2)
spr_df['f1'] = f1_rez
spr_df['d1'] = d1_rez
spr_df['spr_net'] = round((spr_df['f1'] + spr_df['d1']), ndigits=2)

#2d df variables -> numpy variables -> list variables
dtp_net = DataFrame(tp_df['tp_net'])
dspr_net = DataFrame(spr_df['spr_net'])
tp_net = np.array(dtp_net[0:]).tolist()
spr_net = np.array(dspr_net[0:]).tolist()

#2e create 12x12 Numpy array of net-return
net0, net1, net2, net3, net4, net5 = [], [], [], [], [], []
net6, net7, net8, net9, net10, net11= [], [], [], [], [], []

for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
	for s in [f'sum(tp_net[11]+spr_net[{n}])', f'sum(tp_net[10]+spr_net[{n}])', f'sum(tp_net[9]+spr_net[{n}])', f'sum(tp_net[8]+spr_net[{n}])', f'sum(tp_net[7]+spr_net[{n}])', f'sum(tp_net[6]+spr_net[{n}])', f'sum(tp_net[5]+spr_net[{n}])', f'sum(tp_net[4]+spr_net[{n}])', f'sum(tp_net[3]+spr_net[{n}])', f'sum(tp_net[2]+spr_net[{n}])', f'sum(tp_net[1]+spr_net[{n}])', f'sum(tp_net[0]+spr_net[{n}])']:
		eval(f'net{n}').append(eval(s))

net_map = np.array([net0, net1, net2, net3, net4, net5, net6, net7, net8, net9, net10, net11])

