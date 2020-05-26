import numpy as np
import pandas as pd

######################################################
### Shift

close = pd.DataFrame(
    {
        'ABC': [1, 5, 3, 6, 2],
        'EFG': [12, 51, 43, 56, 22],
        'XYZ': [35, 36, 36, 36, 37],},
    pd.date_range('10/01/2018', periods=5, freq='D'))

close.shift(2)

######################################################
### Shift

dates = pd.date_range('10/10/2018', periods=11, freq='D')
close_prices = np.arange(len(dates))

close = pd.Series(close_prices, dates)
close

close.resample('3D')

pd.DataFrame({
    'days': close,
    'weeks': close.resample('W').first()}) # Get opening closing high low after grouping by monthly, weekly or yearly
close.resample('W').ohlc() # open high low close

######################################################

s = pd.Series([1, 2, 3, 4, 5])
s.rolling(3).sum()
# 0     NaN
# 1     NaN
# 2     6.0
# 3     9.0
# 4    12.0

s.expanding(3).sum()
# 0     NaN
# 1     NaN
# 2     6.0
# 3    10.0
# 4    15.0


s.rolling(3).max()
