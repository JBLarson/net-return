from pandas import DataFrame
import pandas as pd
import numpy as np

#import input_nr, create tp/spr DataFrames, add ranges to each
import nr_input as inp

tp_df = DataFrame()
spr_df = DataFrame()

tp_range = [pt for pt in inp.tp_pts]
spr_range = [pt for pt in inp.spr_pts]
tp_df['tp'] = tp_range
spr_df['spr'] = spr_range

#create lists with monetary results for each wager

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


def nr_result():


	#append lists to df's and calculate net results for each
	tp_df['o1'] = o1_rez
	tp_df['u1'] = u1_rez
	tp_df['tp_net'] = round((tp_df['o1'] + tp_df['u1']), ndigits=2)

	spr_df['f1'] = f1_rez
	spr_df['d1'] = d1_rez
	spr_df['spr_net'] = round((spr_df['f1'] + spr_df['d1']), ndigits=2)


	#df variables -> numpy variables -> list variables
	dtp_net = DataFrame(tp_df['tp_net'])
	dspr_net = DataFrame(spr_df['spr_net'])
	tp_net = np.array(dtp_net[0:]).tolist()
	spr_net = np.array(dspr_net[0:]).tolist()

	#create 12x12 Numpy array of net-return
	net0, net1, net2, net3, net4, net5 = [], [], [], [], [], []
	net6, net7, net8, net9, net10, net11= [], [], [], [], [], []

	for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
		for s in [f'sum(tp_net[11]+spr_net[{n}])', f'sum(tp_net[10]+spr_net[{n}])', f'sum(tp_net[9]+spr_net[{n}])', f'sum(tp_net[8]+spr_net[{n}])', f'sum(tp_net[7]+spr_net[{n}])', f'sum(tp_net[6]+spr_net[{n}])', f'sum(tp_net[5]+spr_net[{n}])', f'sum(tp_net[4]+spr_net[{n}])', f'sum(tp_net[3]+spr_net[{n}])', f'sum(tp_net[2]+spr_net[{n}])', f'sum(tp_net[1]+spr_net[{n}])', f'sum(tp_net[0]+spr_net[{n}])']:
			eval(f'net{n}').append(eval(s))
	global net_map

	net_map = np.array([net0, net1, net2, net3, net4, net5, net6, net7, net8, net9, net10, net11])

#create decorator for visual / net-map
def nrrez_decr(nrvisual):
	def wrapper():
		nr_result()
		nrvisual()
		print()
	return wrapper

@nrrez_decr


def nrvisual():

	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import axes3d

	fig = plt.figure(figsize=(12,6))
	fig.suptitle('Above the Book - NetRet Model')
	ax1 = fig.add_subplot(221, projection='3d')
	ax2 = fig.add_subplot(222, projection='3d')
	ax3 = fig.add_subplot(223, projection='3d')
	ax4 = fig.add_subplot(224, projection='3d')

	#create x/y variables, with values determined by 'range variables' from nr_input 
	x = np.arange(inp.exp_spr-6, inp.exp_spr+6, 1)
	y = np.arange(inp.lo_tp, inp.hi_tp, 1)

	#use 'x' and 'y' to create Numpy meshgrid 'X, Y', assign net_map (from nr_results) to 'Z'
	X, Y = np.meshgrid(x, y)
	Z = net_map

	#create colormap. For each axis: define subplot titles and create surface plot
	mycmap = plt.get_cmap('RdYlGn')

	ax1.set_title('Spread Angle')
	ax1.set_zlabel('Result ($)')
	ax1.set_xlabel('Spread')
	ax1.set_ylabel('Total Points')
	surf1 = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
	ax1.set_zlim(np.min(Z), np.max(Z))
	fig.colorbar(surf1, ax=ax1, shrink=.7, aspect=15)

	ax2.set_title('Total Pt Angle')
	ax2.set_zlabel('Result ($)')
	ax2.set_xlabel('Spread')
	ax2.set_ylabel('Total Points')
	surf2 = ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
	ax2.set_zlim(np.min(Z), np.max(Z))
	fig.colorbar(surf2, ax=ax2, shrink=.7, aspect=15)

	ax3.set_title('Spread View')
	ax3.set_xlabel('Spread')
	ax3.set_zlabel('Result ($)')
	ax3.set_yticks([])
	surf3 = ax3.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
	ax3.set_zlim(np.min(Z), np.max(Z))
	fig.colorbar(surf3, ax=ax3, shrink=.7, aspect=15)

	ax4.set_title('Total Pt View')
	ax4.set_zlabel('Result ($)')
	ax4.set_ylabel('Total Points')
	ax4.set_xticks([])
	surf4 = ax4.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
	ax4.set_zlim(np.min(Z), np.max(Z))
	fig.colorbar(surf4, ax=ax4, shrink=.7, aspect=15)


	#assign view angles to each surface plot (elevation, azimuth)
	ax1.view_init(40, 65)
	ax2.view_init(40, 25)
	ax3.view_init(0, 90)
	ax4.view_init(0, 180)


	#display matplotlib figure
	plt.show()


nrvisual()



