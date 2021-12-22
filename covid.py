import pandas as pd
import plotly_express as px

#data = [1,2,3,4,5]
#df = pd.DataFrame(data)
#print(df)

df = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.line(df, x= "date", y = "cases",
color = "country", title = "Covid Data in Different Countries")
fig.show()