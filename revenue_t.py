# 2. Extract Tesla revenue data using Webscraping #5. Tesla revenue dashboard 
import requests
from bs4 import BeautifulSoup
import plotly.graph_objs as go
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

session = requests.Session()
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
# data  = requests.get(url).text
response = session.get(url, headers=headers)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    table = soup.find("table", class_="historical_data_table")
    # print(table)

    df = pd.DataFrame(columns=["Year","Revenue"])

    if table:

        rows = table.find_all("tr")

        for row in rows[1:]:

            cells = row.find_all("td")
            year = cells[0].text.strip()
            revenue = cells[1].text.strip()
            df.loc[len(df)] = [year, revenue]

    else:
        print("Table not found. Check the HTML structure.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)

tesla_revenue = "TSLA Revenue"

df["Revenue"] = df["Revenue"].replace({'\$': ''}, regex=True)
df["Revenue"] = df["Revenue"].str.replace(',', '').astype(float)
print(df.tail())

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=df["Year"], 
        y=df["Revenue"], 
        name=tesla_revenue, 
        marker=dict(color='blue')
        ))

fig.update_layout(
        title='Tesla Revenue Over Time',
        xaxis_title='Date',
        yaxis=dict(
            side='right',
            title='Revenue',
            tickvals=[5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000,50000,60000,70000,80000,90000,100000],
            ticktext=['5B$', '10B$','15B$','20B$','25B$', '30B$', '35B$','40B$','50B$','60B$','70B$','80B$','90B$','100B$']),
        barmode='group'
        )

fig.show()
