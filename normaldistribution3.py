import pandas as pd
import csv
import plotly.figure_factory as fx
df=pd.read_csv("distplot.csv")
fig=fx.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)
fig.show()
