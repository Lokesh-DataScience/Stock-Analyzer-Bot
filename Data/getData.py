import yfinance as yf

class GetData:

    def __init__(self, stock, period, interval):
        self.stock = stock
        self.period = period
        self.interval = interval
        self.data = None

    def fetch_data(self):
        ticker = yf.Ticker(self.stock)
        self.data = ticker.history(period=self.period, interval=self.interval)
        return self.data
