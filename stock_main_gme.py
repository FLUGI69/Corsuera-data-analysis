# 3. Extracting GameStop stock data using yfinance #6. GameStop Stock dashboard
""" 
    Make sure you install all of the following librarys like
    yfinance -> vscode: pip install yfinance jupyter: !pip install yfinance
    pandas: -> vscode: pip install pandas jupyter: !pip install pandas
    plotly: -> vscode: pip install plotly jupyter: !pip install plotly
    
"""

import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

class GameStop:
    def __init__(self, df: pd.DataFrame) -> None:

        self.df = df

    def set_dataframe(self):

        data = yf.Ticker("GME").history(period="max")
       
        self.df = pd.DataFrame(data)
        self.df.reset_index(inplace=True)
        self.df['Date'] = pd.to_datetime(self.df["Date"], unit="s")

        print(" GAMESTOP STOCK --> \n{}\n".format(self.df.head(10)))

        return self.df
      
    def get_fig(self):

        gamestop_stock = "GME"

        self.fig = go.Figure()

        self.fig.add_trace(
            go.Scatter(
                x=self.df['Date'], 
                y=self.df["Close"], 
                mode='lines', 
                name=gamestop_stock, 
                line=dict(color='blue')
                ))
        
        self.fig.update_layout(
            title=f"YFinance {gamestop_stock} Stock",
            xaxis_title='Date',
            yaxis_title='Close Price',
            legend_title='Stocks',
            template='plotly_white'
            )
        
        return self.fig.show()

if __name__ == "__main__":

    df = pd.DataFrame()
    gamestop_df = GameStop(df)
    gamestop_df.set_dataframe()
    gamestop_df.get_fig()
