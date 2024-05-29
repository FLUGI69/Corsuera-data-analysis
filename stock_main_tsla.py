# 1. Extracting Tesla stock data using yfinance #5. Tesla stock dashboard 
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

class Tesla:
    def __init__(self, 
                df: pd.DataFrame,
                ) -> None:

        self.df = df

    def set_dataframe(self):

        data = yf.Ticker("TSLA").history(period="max")
        # print(tesla.info)
        self.df = pd.DataFrame(data)
        self.df.reset_index(inplace=True)
        self.df['Date'] = pd.to_datetime(self.df["Date"], unit="s")

        print(" TESLA STOCK --> \n{}\n".format(self.df.head(10)))
        # print(data.dtypes)

        return self.df
    
    def get_fig(self):

        tesla_stock = "TSLA"

        self.fig = go.Figure()

        self.fig.add_trace(
            go.Scatter(
                x=self.df['Date'], 
                y=self.df["Close"], 
                mode='lines', 
                name=tesla_stock, 
                line=dict(color='blue')
                ))
        
        self.fig.update_layout(
            title=f"Finance {tesla_stock} Stock",
            xaxis_title='Date',
            yaxis_title='Close Price',
            legend_title='Stocks',
            template='plotly_white'
            )
        
        return self.fig.show()
  
if __name__ == "__main__":
  
  df = pd.DataFrame()
  tesla_df = Tesla(df)
  tesla_df.set_dataframe()
  tesla_df.get_fig()
