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
net0 = []
net1 = []
net2 = []
net3 = []
net4 = []
net5 = []
net6 = []

spr_range = []
spr_df = DataFrame()
fb1_rez = []
db2_rez = []
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

print()
print(n3t)




for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'(str(spr_scores[{n}]) + str(tp_scores[5]))', f'(str(spr_scores[{n}]) + str(tp_scores[4]))', f'(str(spr_scores[{n}]) + str(tp_scores[3]))', f'(str(spr_scores[{n}]) + str(tp_scores[2]))', f'(str(spr_scores[{n}]) + str(tp_scores[1]))', f'(str(spr_scores[{n}]) + str(tp_scores[0]))']:
		eval(f'spr{n}').append(eval(s))

net_map_map = pd.DataFrame({'s0': spr0, 's1': spr1, 's2': spr2, 's3': spr3, 's4': spr4, 's5': spr5})



#create x_map
for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))']:
		eval(f'xm{n}').append(eval(s))

net_xmap = pd.DataFrame({'spr0': xm0, 'spr1': xm1, 'spr2': xm2, 'spr3': xm3, 'spr4': xm4, 'spr5': xm5})


#create y_map
for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'(str(tp_scores[{n}]))', f'(str(tp_scores[{n}]))', f'(str(tp_scores[{n}]))', f'(str(tp_scores[{n}]))', f'((tp_scores[{n}]))', f'(str(tp_scores[{n}]))']:
		eval(f'ym{n}').append(eval(s))

net_ymap = pd.DataFrame({'tp0': ym0, 'tp1': ym1, 'tp2': ym2, 'tp3': ym3, 'tp4': ym4, 'tp5': ym5})






for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'sum(tp_net[5]+spr_net[{n}])', f'sum(tp_net[4]+spr_net[{n}])', f'sum(tp_net[3]+spr_net[{n}])', f'sum(tp_net[2]+spr_net[{n}])', f'sum(tp_net[1]+spr_net[{n}])', f'sum(tp_net[0]+spr_net[{n}])']:
		eval(f'net{n}').append(eval(s))

net_map_net = pd.DataFrame({'s0': net0, 's1': net1, 's2': net2, 's3': net3, 's4': net4, 's5': net5})




#print(net_xmap)
#print()
#print(net_ymap)

print()
print(net_map_net)


print()


#notation explained raw column 0
rc0 = net_map_net['s0']
rc1 = net_map_net['s1']
rc2 = net_map_net['s2']


#notation explained quadrant 1_ column 0
q1_0 = rc0[0:3].tolist()
q1_1 = rc1[0:3].tolist()
q1_2 = rc2[0:3].tolist()


print(q1_0)

print(q1_1)
print(q1_2)

quadrant1 = [q1_0, q1_1, q1_2]


print()
print(quadrant1)

#print(q3_0)





"""
#net map net & map for display of 6

for n in ['0', '1', '2', '3', '4', '5', '6']:
	for s in [f'(str(spr_scores[{n}]) + str(tp_scores[6]))', f'(str(spr_scores[{n}]) + str(tp_scores[5]))', f'(str(spr_scores[{n}]) + str(tp_scores[4]))', f'(str(spr_scores[{n}]) + str(tp_scores[3]))', f'(str(spr_scores[{n}]) + str(tp_scores[2]))', f'(str(spr_scores[{n}]) + str(tp_scores[1]))', f'(str(spr_scores[{n}]) + str(tp_scores[0]))']:
		eval(f'spr{n}').append(eval(s))

net_map_map = pd.DataFrame({'s0': spr0, 's1': spr1, 's2': spr2, 's3': spr3, 's4': spr4, 's5': spr5, 's6': spr6})


for n in ['0', '1', '2', '3', '4', '5', '6']:
	for s in [f'sum(tp_net[6]+spr_net[{n}])', f'sum(tp_net[5]+spr_net[{n}])', f'sum(tp_net[4]+spr_net[{n}])', f'sum(tp_net[3]+spr_net[{n}])', f'sum(tp_net[2]+spr_net[{n}])', f'sum(tp_net[1]+spr_net[{n}])', f'sum(tp_net[0]+spr_net[{n}])']:
		eval(f'net{n}').append(eval(s))



net_map_net = pd.DataFrame({'s0': net0, 's1': net1, 's2': net2, 's3': net3, 's4': net4, 's5': net5, 's6': net6})

"""

