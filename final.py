import sys
import numpy
import pylab as pl
import pandas as pd

def main ():
	data = pd.read_csv('gapminder_gdp_america.csv', index_col = 0, header = 0)
	data_mean = data.mean(axis = 0)
	x = ('1952', '1957', '1962', '1967', '1972', '1977', '1982', 
'1987', '1992', '1997', '2002', '2007')
	N = len(x)
	ind = numpy.arange(N)
	average_gpd = data_mean
	width = 0.8
	xlabel = ['1952', '1957', '1962', '1967', '1972', '1977', 
'1982', '1987', '1992', '1997', '2002', '2007']
	pl.bar(ind, average_gpd, width, align = 'center')
	pl.xlabel('Time - Year')
	pl.ylabel('Average GPD')
	pl.xticks(ind, xlabel, rotation = 'vertical')
	pl.savefig('final.png')
	
	

main()

	
