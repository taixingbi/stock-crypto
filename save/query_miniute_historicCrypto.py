import pandas as pd

from Historic_Crypto import HistoricalData
from Historic_Crypto import Cryptocurrencies
from Historic_Crypto import LiveCryptoData
# https://pypi.org/project/Historic-Crypto/

# ticker= 'ETH-USD'
# ticker= 'BTC-USD'
# ticker= 'DOGE-USD'
ticker= 'SHIB-USD'


# 60, 300, 900, 3600, 21600, 86400 seond
# 1m, 5m, 15m, 1h, 9h, 1day
period= 60

start= '2021-06-16-00-00'

# df = HistoricalData("ETH-USD", 300, '2021-06-08-00-00', '2021-06-09-00-00').retrieve_data()
df = HistoricalData(ticker, period, start).retrieve_data()
print(df)
df.to_csv('data/' + ticker + '.csv')

print("done")