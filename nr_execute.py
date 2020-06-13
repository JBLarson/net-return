from pandas import DataFrame
import pandas as pd

#import scenario and matrix DataFrames / surface-plot function
from nr_input import tdf, scndf
from nr_results import nrvisual
import nr_input as inp

#localize variables from inp
o1s, u1s, o1r, u1r, o1w, u1w = inp.o1s, inp.u1s, inp.o1r, inp.u1r, inp.o1w, inp.u1w
f1s, d1s, f1r, d1r, f1w, d1w = inp.f1s, inp.d1s, inp.f1r, inp.d1r, inp.f1w, inp.d1w



#define scenario stats function
def scn_stats():
	print(scndf, '\n', '\n', tdf, '\n')

#define surf decorator function that outputs scn_stats and surf-plot visual
def surf_decr(surf4):
	def wrapper():
		print()
		scn_stats()
		surf4()
	return wrapper

#attach surf decorator to surf 4 function
@surf_decr
def surf4():
	nrvisual()

#desc = False
desc = True
if desc == True:

	print("Over:",o1s,"pts - Risk: $",o1r,"Net: $",round(o1w, ndigits=2))
	print("Under:",u1s,"pts - Risk: $",u1r,"Net: $",round(u1w, ndigits=2))
	print()
	print("Fav:",f1s,"pt - Risk: $",f1r,"Net: $",round(f1w, ndigits=2))
	print("Dog:",d1s,"pt - Risk: $",d1r,"Net: $",round(d1w, ndigits=2))
	print()



surf4()
