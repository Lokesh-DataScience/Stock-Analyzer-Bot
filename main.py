from Data.getData import GetData
from Plot.plotData import PlotData

gd = GetData("RELIANCE.NS", "1mo", "1d")
df = gd.fetch_data()

# Now plot it
plotter = PlotData(df)
plotter.plot_open("RELIANCE")
plotter.plot_close("RELIANCE")
plotter.plot_volume("RELIANCE")
