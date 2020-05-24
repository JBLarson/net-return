from pandas import DataFrame
import pandas as pd
import numpy as np

import input_twob_model as tp
import input_spr_model as inp
import netret_results as nr


#tp/spr net w/o rounding
tp_scores = nr.tp_scores
spr_scores = nr.spr_scores

tp_net = nr.ntp_net
spr_net = nr.nspr_net


n3t = DataFrame({'pts':tp_scores, 'tp_net':tp_net, 'score':spr_scores, 'spr_net':spr_net})

print()
print(n3t)




for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'(str(spr_scores[{n}]) + str(tp_scores[5]))', f'(str(spr_scores[{n}]) + str(tp_scores[4]))', f'(str(spr_scores[{n}]) + str(tp_scores[3]))', f'(str(spr_scores[{n}]) + str(tp_scores[2]))', f'(str(spr_scores[{n}]) + str(tp_scores[1]))', f'(str(spr_scores[{n}]) + str(tp_scores[0]))']:
		eval(f'nr.spr{n}').append(eval(s))

net_map_map = pd.DataFrame({'s0': nr.spr0, 's1': nr.spr1, 's2': nr.spr2, 's3': nr.spr3, 's4': nr.spr4, 's5': nr.spr5})



#create x_map
for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))', f'(str(spr_scores[{n}]))']:
		eval(f'nr.xm{n}').append(eval(s))

net_xmap = pd.DataFrame({'spr0': nr.xm0, 'spr1': nr.xm1, 'spr2': nr.xm2, 'spr3': nr.xm3, 'spr4': nr.xm4, 'spr5': nr.xm5})


#create y_map
for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'(str(tp_scores[{n}]))', f'(str(tp_scores[{n}]))', f'(str(tp_scores[{n}]))', f'(str(tp_scores[{n}]))', f'((tp_scores[{n}]))', f'(str(tp_scores[{n}]))']:
		eval(f'nr.ym{n}').append(eval(s))

net_ymap = pd.DataFrame({'tp0': nr.ym0, 'tp1': nr.ym1, 'tp2': nr.ym2, 'tp3': nr.ym3, 'tp4': nr.ym4, 'tp5': nr.ym5})






for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'sum(tp_net[5]+spr_net[{n}])', f'sum(tp_net[4]+spr_net[{n}])', f'sum(tp_net[3]+spr_net[{n}])', f'sum(tp_net[2]+spr_net[{n}])', f'sum(tp_net[1]+spr_net[{n}])', f'sum(tp_net[0]+spr_net[{n}])']:
		eval(f'nr.net{n}').append(eval(s))

net_map_net = pd.DataFrame({'s0': nr.net0, 's1': nr.net1, 's2': nr.net2, 's3': nr.net3, 's4': nr.net4, 's5': nr.net5})




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




