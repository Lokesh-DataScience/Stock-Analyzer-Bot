import plotly.express as px
import pandas as pd
import plotly.io as pio

class PlotData:

    def __init__(self, data):
        self.data = data

    def plot_open(self, stock_name):
        self._plot_column('Open', stock_name)

    def plot_high(self, stock_name):
        self._plot_column('High', stock_name)

    def plot_low(self, stock_name):
        self._plot_column('Low', stock_name)

    def plot_close(self, stock_name):
        self._plot_column('Close', stock_name)

    def plot_volume(self, stock_name):
        self._plot_column('Volume', stock_name)

    def plot_dividends(self, stock_name):
        if 'Dividends' in self.data.columns:
            self._plot_column('Dividends', stock_name)
        else:
            print("Dividends data not available.")

    def _plot_column(self, column_name, stock_name):
        fig = px.line(self.data, x=self.data.index, y=column_name,
                      title=f'{stock_name} {column_name} Over Time',
                      labels={'x': 'Date', column_name: column_name})
        
        # Optional: Show plot in notebook or browser
        fig.show()
        