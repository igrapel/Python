import yfinance as yf
import seaborn as sns


#Open    High     Low   Close   Volume  Dividends  Stock Splits
#time '2020-1-1'
def stockHistory(symbol, s, e):
    #define the ticker symbol
    tickerSymbol = symbol

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start= s, end= e)

    return tickerDf    


def stockHistoryColumn(symbol, s, e, col):
    #define the ticker symbol
    tickerSymbol = symbol

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start= s, end= e)
    
    tickerCol = tickerDf[col]

    return tickerCol    

def graphHistory(symbol, s, e, col):
    data = stockHistoryColumn(symbol, s, e, col)
    data.plot(linewidth=0.5);

print(stockHistoryColumn('HLT', '2020-6-1', '2021-1-1', 'Close'))
graphHistory('PLTR', '2020-6-1', '2021-1-1', 'Close')
