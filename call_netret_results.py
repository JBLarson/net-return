from pandas import DataFrame
import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import input_nr as inp
import netret_results as nr


#renamed to call_nr_results.py from netret5.py


#tp/spr net w/o rounding
tp_scores = nr.tp_scores
spr_scores = nr.spr_scores

tp_net = nr.ntp_net
spr_net = nr.nspr_net


print()
#print(nr.n3t)




for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'((spr_scores[{n}]) + (tp_scores[5]))', f'((spr_scores[{n}]) + (tp_scores[4]))', f'((spr_scores[{n}]) + (tp_scores[3]))', f'((spr_scores[{n}]) + (tp_scores[2]))', f'((spr_scores[{n}]) + (tp_scores[1]))', f'((spr_scores[{n}]) + (tp_scores[0]))']:
		eval(f'nr.spr{n}').append(eval(s))

net_map_map = pd.DataFrame({'s0': nr.spr0, 's1': nr.spr1, 's2': nr.spr2, 's3': nr.spr3, 's4': nr.spr4, 's5': nr.spr5})


#print(net_map_map)
#print(np.shape(net_map_map))
#print(type(net_map_map))



#create x_map
for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))', f'((spr_scores[{n}]))']:
		eval(f'nr.xm{n}').append(eval(s))

#net_xmap = pd.DataFrame({'spr0': nr.xm0, 'spr1': nr.xm1, 'spr2': nr.xm2, 'spr3': nr.xm3, 'spr4': nr.xm4, 'spr5': nr.xm5})

net_xmap = (nr.xm0, nr.xm1, nr.xm2, nr.xm3, nr.xm4, nr.xm5)


nx_net = np.array(net_xmap)

x_net = nx_net.tolist()

#print(nx_net)
#print(np.shape(nx_net))
#print(type(nx_net))

#create y_map
for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))', f'((tp_scores[{n}]))']:
		eval(f'nr.ym{n}').append(eval(s))

#net_ymap = pd.DataFrame({'tp0': nr.ym0, 'tp1': nr.ym1, 'tp2': nr.ym2, 'tp3': nr.ym3, 'tp4': nr.ym4, 'tp5': nr.ym5})

net_ymap = (nr.ym0, nr.ym1, nr.ym2, nr.ym3, nr.ym4, nr.ym5)


ny_net = np.array(net_ymap)

y_net = ny_net.tolist()

#print(ny_net)
#print(np.shape(ny_net))
#print(type(ny_net))




for n in ['0', '1', '2', '3', '4', '5']:
	for s in [f'sum(tp_net[5]+spr_net[{n}])', f'sum(tp_net[4]+spr_net[{n}])', f'sum(tp_net[3]+spr_net[{n}])', f'sum(tp_net[2]+spr_net[{n}])', f'sum(tp_net[1]+spr_net[{n}])', f'sum(tp_net[0]+spr_net[{n}])']:
		eval(f'nr.net{n}').append(eval(s))

#net_map_net = pd.DataFrame({'s0': nr.net0, 's1': nr.net1, 's2': nr.net2, 's3': nr.net3, 's4': nr.net4, 's5': nr.net5})

#net_map_net = [nr.net0, nr.net1, nr.net2, nr.net3, nr.net4, nr.net5]

#net_map_net = (nr.net0, nr.net1, nr.net2, nr.net3, nr.net4, nr.net5)


net_map_net = np.array([nr.net0, nr.net1, nr.net2, nr.net3, nr.net4, nr.net5])



