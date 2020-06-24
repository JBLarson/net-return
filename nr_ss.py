from pandas import DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#import nr_input, create tp/spr DataFrames, add ranges to each
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

	trisk = inp.o1r + inp.u1r + inp.f1r + inp.d1r

	#create 12x12 Numpy array of net-results, use that to create net-return array

	netd0, netd1, netd2, netd3, netd4, netd5 = [], [], [], [], [], []
	netd6, netd7, netd8, netd9, netd10, netd11= [], [], [], [], [], []
	for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
		for s in [f'sum(tp_net[11]+spr_net[{n}])', f'sum(tp_net[10]+spr_net[{n}])', f'sum(tp_net[9]+spr_net[{n}])', f'sum(tp_net[8]+spr_net[{n}])', f'sum(tp_net[7]+spr_net[{n}])', f'sum(tp_net[6]+spr_net[{n}])', f'sum(tp_net[5]+spr_net[{n}])', f'sum(tp_net[4]+spr_net[{n}])', f'sum(tp_net[3]+spr_net[{n}])', f'sum(tp_net[2]+spr_net[{n}])', f'sum(tp_net[1]+spr_net[{n}])', f'sum(tp_net[0]+spr_net[{n}])']:
			eval(f'netd{n}').append(eval(s))

	global net_map, net_ret, X, Y, Z, Z1L

	net_map = np.array([netd0, netd1, netd2, netd3, netd4, netd5, netd6, netd7, netd8, netd9, netd10, netd11])


	net0, net1, net2, net3, net4, net5 = [], [], [], [], [], []
	net6, net7, net8, net9, net10, net11= [], [], [], [], [], []
	for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
		for s in [f'netd{n}[0]/trisk', f'netd{n}[1]/trisk', f'netd{n}[2]/trisk', f'netd{n}[3]/trisk', f'netd{n}[4]/trisk', f'netd{n}[5]/trisk', f'netd{n}[6]/trisk', f'netd{n}[7]/trisk', f'netd{n}[8]/trisk', f'netd{n}[9]/trisk', f'netd{n}[10]/trisk', f'netd{n}[11]/trisk']:
			eval(f'net{n}').append(eval(s))
	net_ret = np.array([net0, net1, net2, net3, net4, net5, net6, net7, net8, net9, net10, net11])

	#create x/y variables, with values determined by 'range variables' from nr_input 
	x = np.arange(inp.exp_spr-6, inp.exp_spr+6, 1)
	y = np.arange(inp.lo_tp, inp.hi_tp, 1)

	#use 'x' and 'y' to create Numpy meshgrid 'X, Y', assign net_map (from nr_results) to 'Z'
	X, Y = np.meshgrid(x, y)
	#change z1 to z and comment Z to display net-return graphic instead of net-result
	Z, Z1L = net_ret, []

	for zz in Z:
		for z in zz: Z1L.append(z)


#decorator for surf-scat visual
def ss_decr(surfscat):
	def wrapper():
		nr_result()
		surfscat()
		print()
	return wrapper

@ss_decr
def surfscat():
	fig = plt.figure(figsize=(8,6))
	ax1 = fig.add_subplot(211, projection='3d')
	ax2 = fig.add_subplot(212, projection='3d')
	mycmap = plt.get_cmap('RdYlGn')
	
	ax1.set_zlabel('\nROI(%)', fontsize=16)
	ax1.set_xlabel('\nSpread', fontsize=16)
	ax1.set_ylabel('\nTotal Points', fontsize=16)
	surf1 = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
	ax1.set_zlim(np.min(Z), np.max(Z))

	ax2.set_zlabel('\nROI(%)', fontsize=16)
	ax2.set_xlabel('\nSpread', fontsize=16)
	ax2.set_ylabel('\nTotal Points', fontsize=16)
	scatter1 = ax2.scatter(X, Y, Z, c = Z1L, cmap='RdYlGn', marker='D', edgecolors='black')
	ax2.set_zlim(np.min(Z), np.max(Z))
	
	ax1.view_init(30, 45)
	ax2.view_init(30, 45)
	plt.show()

#decorator for surface plot visual
def surf_decr(surf):
	def wrapper():
		nr_result()
		surf()
		print()
	return wrapper

@surf_decr
def surf():
	fig = plt.figure(figsize=(8,4))
	ax1 = fig.add_subplot(111, projection='3d')
	mycmap = plt.get_cmap('RdYlGn')
	ax1.set_zlabel('\nROI(%)', fontsize=16)
	ax1.set_xlabel('\nSpread', fontsize=16)
	ax1.set_ylabel('\nTotal Points', fontsize=16)
	surf1 = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
	ax1.set_zlim(np.min(Z), np.max(Z))
	ax1.view_init(30, 45)
	plt.show()

#decorator for scatter plot visual
def scatter_decr(scatter):
	def wrapper():
		nr_result()
		scatter()
		print()
	return wrapper

@scatter_decr
def scatter():
	fig = plt.figure(figsize=(8,4))
	ax1 = fig.add_subplot(111, projection='3d')
	mycmap = plt.get_cmap('RdYlGn')
	ax1.set_zlabel('\nROI(%)', fontsize=16)
	ax1.set_xlabel('\nSpread', fontsize=16)
	ax1.set_ylabel('\nTotal Points', fontsize=16)
	scatter1 = ax1.scatter(X, Y, Z, c = Z1L, cmap='RdYlGn', marker='D', edgecolors='black')
	ax1.set_zlim(np.min(Z), np.max(Z))
	ax1.view_init(30, 45)
	plt.show()





#decorator for visual / net-map
def ssroi_decr(ssroi_visual):
	def wrapper():
		nr_result()
		ssroi_visual()
	return wrapper

@ssroi_decr

def ssroi_visual():

	fig = plt.figure(figsize=(8,4))
	ax1 = fig.add_subplot(111, projection='3d')
	x = np.arange(inp.exp_spr-6, inp.exp_spr+6, 1)
	y = np.arange(inp.lo_tp, inp.hi_tp, 1)
	X, Y = np.meshgrid(x, y)
	Z, Z1L = net_ret, []
	for zz in Z:
		for z in zz: Z1L.append(z)
	mycmap = plt.get_cmap('RdYlGn')
	ax1.set_zlabel('\nROI', fontsize=16)
	ax1.set_xlabel('\nSpread', fontsize=16)
	ax1.set_ylabel('\nTotal Points', fontsize=16)
	surf1 = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
	ax1.set_zlim(np.min(Z), np.max(Z))
	scatter1 = ax1.scatter(X, Y, Z, c = Z1L, cmap='RdYlGn', edgecolors='black')
	ax1.view_init(55, 40)

	plt.show()


#decorator for visual / net-map
def ssnet_decr(ssnet_visual):
	def wrapper():
		nr_result()
		ssnet_visual()
	return wrapper

@ssnet_decr

def ssnet_visual():
	fig = plt.figure(figsize=(8,4))
	ax1 = fig.add_subplot(111, projection='3d')
	x = np.arange(inp.exp_spr-6, inp.exp_spr+6, 1)
	y = np.arange(inp.lo_tp, inp.hi_tp, 1)
	X, Y = np.meshgrid(x, y)
	Z, Z1L = net_map, []
	for zz in Z:
		for z in zz: Z1L.append(z)
	mycmap = plt.get_cmap('RdYlGn')
	ax1.set_zlabel('\nNet($)', fontsize=16)
	ax1.set_xlabel('\nSpread', fontsize=16)
	ax1.set_ylabel('\nTotal Points', fontsize=16)
	surf1 = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
	ax1.set_zlim(np.min(Z), np.max(Z))
	scatter1 = ax1.scatter(X, Y, Z, c = Z1L, cmap='RdYlGn', edgecolors='black')
	ax1.view_init(35, 40)

	plt.show()





#options to display 3D visuals
#surface plot, scatter plot, surface / scatter (seperate axis')
#surface / scatter ROI, surface / scatter net (same axis)

d_surf, d_scat, d_ss = ('n'), ('n'), ('y')
d_ssroi, d_ssnet = ('n'), ('y')


if d_surf == 'y': surf()
if d_scat == 'y': scatter()
if d_ss == 'y': surfscat()
if d_ssroi == 'y': ssroi_visual()
if d_ssnet == 'y': ssnet_visual()





