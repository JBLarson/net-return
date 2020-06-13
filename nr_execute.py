from pandas import DataFrame
import pandas as pd

#import scenario and matrix DataFrames / surface-plot function
from nr_input import tdf, scndf
from nr_results import nrvisual

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

surf4()
