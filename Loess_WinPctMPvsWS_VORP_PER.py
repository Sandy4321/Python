# -*- coding: utf-8 -*-
# import csv
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pylab as plt
import statsmodels.api as sm
import ggplot as gg
#from ggplot import *

df = pd.DataFrame.from_csv('leagues_NBA_2013_14_total_edited.csv', index_col=None)
df = df[df['WSp48'] > -0.05]
#table = df.pivot_table('WinPct', 'WSp48','Player')
x=df['WSp48']
y=df['WinPct']
#VORP are the values, Season the index, Player the columns

#print table

#Player  PlayerA  PlayerB
#Season
#'0405’     0.70     0.23
#'0506’     0.14    -0.30
lowess = sm.nonparametric.lowess(y, x, frac=0.1)
df = gg.df
gg.qplot(df.x, df.y) + gg.geom_smooth(color="blue")
#ax = table.plot(marker='o')
#ax.set_title('WinPct vs WSp48')
#ax.set_ylabel('WinPct')
#ax.legend(loc=3,prop={'size':10})
plt.plot(x, y, '+')
plt.plot(lowess[:, 0], lowess[:, 1],color='red')
plt.show()