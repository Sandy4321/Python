import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ls_symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
dt_start = dt.datetime(2006, 1, 1)
dt_end = dt.datetime(2010, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
# The reason we need to specify 16:00 hours is because we want to read the data
#that was available to us at the close of the day.
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
#above two lines provide the various data types you want to read.
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
#creates a list of dataframe objects which have all the different types of data.
d_data = dict(zip(ls_keys, ldf_data))
# converts this list into a dictionary and then we can access anytype of data we want easily.



na_price = d_data['close'].values
na_normalized_price = na_price / na_price[0, :]

#retRun Python fileurns by day
na_rets = na_normalized_price.copy()
tsu.returnize0(na_rets)
#returnize0 calculates the daily returns of the prices

dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))
na_price = d_data['close'].values

#print na_price[0, :]
#[   74.43    53.12   435.23  1268.8     50.47]
na_normalized_price = na_price / na_price[0, :]

print na_price[0]
#[   74.43    53.12   435.23  1268.8     50.47]
print na_price[-1]
#[  322.28   137.03   598.86  1257.88    70.33]