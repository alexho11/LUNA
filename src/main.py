import pandas as pd
import yfinance as yf
from datetime import datetime
from datetime import timedelta
import plotly.graph_objects as go



today=datetime.today().strftime('%Y-%m-%d')
start_date='2017-01-01'

eth_df=yf.download('LUNA1-USD',start_date,today)
#eth_df.tail()
#eth_df.info()
eth_df.reset_index(inplace=True)
#print(eth_df.columns)
df=eth_df[["Date","Open"]]
new_names={
    "Date": "ds",
    "Open": "y",
}
df.rename(columns=new_names,inplace=True)

x=df["ds"]
y=df["y"]

fig=go.Figure()
fig.add_trace(go.Scatter(x=x,y=y))

# Set title
fig.update_layout(
    title_text="Time series plot of Terra Luna Open Price"
)
fig.show()