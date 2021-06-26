import requests        # for making http requests to binance
import json            # for parsing what binance sends back to us
import pandas as pd    # for storing and manipulating the data we get back
import numpy as np
import matplotlib.pyplot as plt # for charts and such  
import datetime as dt  # for dealing with times

# https://steemit.com/python/@marketstack/how-to-download-historical-price-data-from-binance-with-python

# https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md

def get_bars(symbol, interval = '1m'): # 1h 
    root_url = 'https://api.binance.com/api/v3/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    
    df.columns = [  'open_time',
                    'o', 'h', 'l', 'c', 'v',
                    'close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore']
    print(df)
    
    df.to_csv('data/' + symbol + '.csv')
    df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.close_time]
    return df


steemeth = get_bars('STEEMETH')
ethusdt = get_bars('ETHUSDT')                 

steemusdt = steemeth['c'].astype('float') * ethusdt['c'].astype('float')
steemusdt.plot()


print("done")
