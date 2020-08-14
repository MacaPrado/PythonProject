from bs4 import BeautifulSoup
import requests
import csv

# First Python Proyect
# Each day I want to scrap promociones aereas, and see if there's a ticket with the conditions I require
# Example, I want a Ticket to New York for less than 500 USD
# As I live in Argentina, there are two values in pesos argentinos for 1 USD
# One is called dolar blue and the other dolar oficial
# The idea is that the program compares prices in USD and in ARS and gets any Ticket to New York that is less
# than 500 USD and sends me an email or notification when it finds one
# It also compares by date so it doesn't scrape more than necessary

url = 'https://promociones-aereas.com.ar/'  # url I'd like to scrape
hdr = {'User-Agent': 'Mozilla/5.0'}

source = requests.get(url, headers=hdr).text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('promociones_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Date', 'Title'])

for header in soup.find_all('header', class_="entry-header")[1:]:
    date = header.find('div', class_="entry-meta").find_all('li')[2]
    if date.find('span', class_="d-none"):
        date_text = date.find('span', class_="d-none").text
    else:
        date_text = date.text
    title = header.find('a', class_='post-title-link').text
    csv_writer.writerow([date_text, title])
    print(date_text)
    print(title)

csv_file.close()
