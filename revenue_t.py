# 2. Extract Tesla revenue data using Webscraping #5. Tesla revenue dashboard 
import requests
from bs4 import BeautifulSoup
import plotly.graph_objs as go

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

    revenue_date = []
    revenue_price = []
    table = soup.find("table", class_="historical_data_table")
    # print(table)

    if table:

        rows = table.find_all("tr")

        for row in rows[1:]:

            cells = row.find_all("td")
            year = cells[0].text.strip()
            revenue = cells[1].text.strip()
            revenue_date.append(year)
            revenue_price.append(revenue)

    else:
        print("Table not found. Check the HTML structure.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)

tesla_revenue = "TSLA Revenue"

sorted_date = sorted(revenue_date)
sorted_price = revenue_price[::-1]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=sorted_date, 
        y=sorted_price, 
        name=tesla_revenue, 
        marker=dict(color='blue')
        ))

fig.update_layout(
        title='Tesla Revenue Over Time',
        xaxis_title='Date',
        yaxis_title='Revenue',
        barmode='group'
        )

fig.show()
