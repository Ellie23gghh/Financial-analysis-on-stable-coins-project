from pycoingecko import CoinGeckoAPI  #imported the library in order to work with Coin Gecko API.This is needed for extraction of the data about the stable coins on which I made the study
import pandas as pd   #imported the pandas library for data manipulation
import matplotlib.pyplot as mat #imported the matplotlib library for data visualization
cg=CoinGeckoAPI()

stablecoins = ['tether', 'usd-coin', 'binance-usd', 'dai', 'true-usd']  #defined a list of stable coins on which the study focuses on


sc_marketdata=cg.get_coins_markets(vs_currency='usd',     #the get_coins_markets method fetches market data, including price trends (sparkline) for the specified coins.
                                   ids=stablecoins,
                                   order='market_cap_desc',
                                   per_page=100,
                                   page=1,
                                   sparkline=True)

sc_df=pd.DataFrame(sc_marketdata)  #aggregates the data in a Pandas DataFrame



mat.figure(figsize=(8,5))  #a figure is created for the plot, and we iterate over each row of the DataFrame


#for each stablecoin, we extract the last 7 prices from the sparkline data and plot them
for col,row in sc_df.iterrows():
    sparkline_prices=row['sparkline_in_7d']['price']
    last_7_prices = sparkline_prices[-7:] 
    mat.plot(last_7_prices, label=row['id'])

mat.title('7 Days Price Trends of Stablecoins')
mat.xlabel('Days')
mat.ylabel('Price in USD')
mat.xticks(ticks=range(len(last_7_prices)),labels=range(1,8))
mat.legend()
mat.grid()
mat.show()
#the plot is titled, labeled, and displayed with grid lines for better readability.