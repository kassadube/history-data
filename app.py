import requests                    # for "get" request to API
import json                        # parse json into a list
import pandas as pd                # working with data frames
import datetime as dt              # working with dates
import matplotlib.pyplot as plt    # plot data
import qgrid                       # display dataframe in notebooks 


url = "https://api.binance.com/api/v3/klines"
interval = '1h'
symbol = 'ETHUSDT'
startTime = str(int(dt.datetime(2020, 1, 1).timestamp() * 1000))
endTime = str(int(dt.datetime(2020, 2, 1).timestamp() * 1000))
limit = '1000'

req_params = {"symbol" : symbol, 'interval' : interval, 'startTime' : startTime, 'endTime' : endTime, 'limit' : limit}
df = pd.DataFrame(json.loads(requests.get(url, params = req_params).text))
 
#if (len(df.index) == 0):
 #   return None
    
df = df.iloc[:, 0:6]
df.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']

df.open      = df.open.astype("float")
df.high      = df.high.astype("float")
df.low       = df.low.astype("float")
df.close     = df.close.astype("float")
df.volume    = df.volume.astype("float")

df['adj_close'] = df['close']
    
df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.datetime]
print(df)
df.to_csv("foo.csv")
df['close'].astype('float').plot()