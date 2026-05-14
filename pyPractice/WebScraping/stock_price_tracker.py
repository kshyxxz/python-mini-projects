from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://finance.yahoo.com/quote/GC%3DF/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    )
}

response = requests.get(
    URL,
    headers=headers,
    verify=False,
    timeout=10
)
soup = BeautifulSoup(response.text, "html.parser")

cards = soup.find_all("div", class_="ticker-item-wrapper yf-1o9ayn7")

stocks = []

for card in cards:
	stock_name = soup.find("spna", class_="text neo-font-label-sm-emphasis yf-18d6y07")
	stocks.append(stock_name)


print(stocks)