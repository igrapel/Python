import yfinance as yf

def stockHistorydf(stock, s, e):
    tickerData = yf.Ticker(stock)
    tickerDf = tickerData.history(period='id', start=s, end=e)
    return tickerDf
    
def stockHistoryCol(stock, s, e, col):
    myStockdf = stockHistorydf(stock, s, e)
    myStockCol = myStockdf[col]
    return myStockCol
    
mydata = stockHistoryCol('AAPL', '2020-3-1', '2020-12-12', 'Close')

#Index(['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'], dtype='object')
#print(tickerDf['Close'])

def graphHistory(stock, s, e, col):
    data = stockHistoryCol(stock, s, e, col)
    data.plot(linewidth=0.5)
    
#graphHistory('AAPL', '2020-3-1', '2020-12-12', 'Close')
print(type(mydata))
