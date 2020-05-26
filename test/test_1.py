import pandas as pd
import numpy as np
df = pd.DataFrame({"a":[1,2,3,4],"b":[3,4,8,2],"c":[0,4,8,8]})
res = df.copy()
res = pd.DataFrame(index=df.index, columns=df.columns)
res.fillna(0,inplace=True)
(df*df)/2


for i,row in df.iterrows():
    df.loc[i,row.nlargest(2).index] = 1
    row.index

## Test Resample
index = pd.date_range('1/1/2000', periods=9, freq='D')
series = pd.Series(range(9), index=index)
series.resample('3D',label='right').max()


pd.to_datetime(series.index)