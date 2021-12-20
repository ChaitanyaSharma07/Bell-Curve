import pandas
import plotly.figure_factory as ff

data = pandas.read_csv("data.csv")

fig = ff.create_distplot([data["Avg Rating"].to_list()], ["Mobile Brand"])
fig.show()