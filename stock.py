import requests
import json
import time
from bs4 import BeautifulSoup

def getHTML(html):
	response = requests.get("https://www.marketwatch.com/investing/stock/" + ticker)
	html = response.text
	return html 


def scrape(html):
	soup = BeautifulSoup(html, "html.parser")

	cur_price = soup.find_all("bg-quote", class_="value")[0].text
	
	past_month_performance = float(soup.find_all("li", class="content__item value ignore-color")[0].text[:-1])

	if past_month_performance > 0:
		past_month_performance = "UP TREND"
	else:
		past_month_performance= "DOWN TREND"

	volume = soup.find_all("span", class_="volume last-value")[0].text

	return cur_price, past_month_performance, volume


def create_output(ticker):
	html = getHTML(ticker)
	cur_price,past_month_performance,volume = scrape(html)

	final_output = f"This is the Analysis of Stock {ticker} \nThe Current Stock Price is {cur_price} \nThe Price has been going in an {past_month_performance} \nThe Volume of the stock is {volume}"
	
#	print(final_output)

	file_output = f"{cur_price},{past_month_performance},{volume}\n"

	return file_output

def main():
	global ticker
	ticker = input("Please input ticker:")
	
	while True:
		file_line = create_output(ticker)					

		with open("data.csv","a") as file:
			file.write(file_line)
		
		time.sleep(5)

main()				
