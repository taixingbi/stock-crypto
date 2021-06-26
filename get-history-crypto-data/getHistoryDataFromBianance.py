from binance.client import Client
import pandas as pd    # for storing and manipulating the data we get back
from datetime import datetime

client = Client()
# interval= Client.KLINE_INTERVAL_1DAY
# interval= Client.KLINE_INTERVAL_12HOUR
#interval= Client.KLINE_INTERVAL_1HOUR
# interval= Client.KLINE_INTERVAL_30MINUTE
# interval= Client.KLINE_INTERVAL_15MINUTE
interval= Client.KLINE_INTERVAL_1MINUTE

def downloadTicker(ticker, start):
    print(ticker, start)
    # for price in client.get_all_tickers():    print(price)

    data = client.get_historical_klines(ticker, interval, start)
    df = pd.DataFrame(data)
    df.columns = [  'open_time',
                    'o', 'h', 'l', 'c', 'v',
                    'close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore']

    df['open_time'] = df['open_time'].apply( lambda time: datetime.fromtimestamp(time/1000) )

    # print(df.tail())

    df.to_csv('../data/' + ticker + '-' + start + '-' + interval+ '.csv')

tickers= [ "BTCUSDT", "DOGEUSDT", "SHIBUSDT", "ETHUSDT"]
# start= "22June2021"
start= "1April2021"

for ticker in tickers:  
    downloadTicker(ticker, start)

print("done")
