# 4. Retrieving GameStop revenue data using Web scraping #6. GameStop revenue dashboard

import requests
import plotly.graph_objs as go
from bs4 import BeautifulSoup
import pandas as pd

url = "https://companiesmarketcap.com/gamestop/revenue/"
response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    tables = soup.find("table")
    # print(table)
    df = pd.DataFrame(columns=["Year","Revenue","Change"])

    if tables:
        
        for index, table in enumerate(tables):
            # print(f"index --> {index} \ntable --> {table}")
            if index == 3:

                rows = table.find_all("tr")
                # print(rows)
                for row in rows:
                
                    column = row.find_all("td")
                    # print(f"Cells {counter}:{cell}\n")
                    
                    if (column != []):
                        year = column[0].text.strip()
                        revenue = column[1].text.strip()
                        change = column[2].text.strip()
                        df.loc[len(df)] = [year, revenue, change]
                    
                break 

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

df["Revenue"] = df["Revenue"].replace({'\$': '', ' B': ''}, regex=True).astype(float)
df["Year"] = df["Year"].str.replace(' (TTM)', '').astype(int)
print("GameStop Revenue tail -->\n",df.tail())

fig = go.Figure([go.Scatter(
    x=df["Year"], 
    y=df['Revenue'],
    text=df['Change'].apply(lambda x: x),
    mode='lines + text',  
    textposition="top left",  
    line=dict(color='blue', width=1)  
)])

fig.update_layout(
            title="GME Revenue",
            xaxis_title='Date',
            yaxis_title='Revenue',
            template='plotly_white'
            )

fig.show()
