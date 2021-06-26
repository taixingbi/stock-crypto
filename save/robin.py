import os
import robin_stocks.robinhood as rs

robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

def purchase(symbol, ammountInDollars):
    rs.login(username=robin_user,
            password=robin_pass,
            expiresIn=86400,
            by_sms=True)

    # rs.orders.order_buy_fractional_by_price(symbol,
    rs.orders.order_buy_crypto_by_price(symbol, 
                                    ammountInDollars,
                                    timeInForce='gtc')

    # rs.logout()

symbol='ETH'
ammountInDollars=0.8
purchase(symbol, ammountInDollars)

print("$"+str(ammountInDollars), "was placed for", symbol)