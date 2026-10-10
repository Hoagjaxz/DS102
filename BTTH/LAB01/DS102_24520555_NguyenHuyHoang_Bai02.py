
import csv

import requests
from bs4 import BeautifulSoup

url =  "https://www.scrapethissite.com/pages/simple/"
HEADERS = {"User-Agent" : "Mozilla/5.0 (bai-tap-thu-thap-du-lieu)"}
response = requests.get(url, headers = HEADERS)
response.raise_for_status()
html = response.text


soup = BeautifulSoup(html, "html.parser")

all_countries = []

for item in soup.select("div.country"):
    name = item.select_one("h3.country-name").get_text().strip()
    capital = item.select_one("span.country-capital").get_text(strip = True)
    population = item.select_one("span.country-population").get_text(strip = True)
    area = item.select_one("span.country-area").get_text(strip = True)

    all_countries.append({
        "Country name": name,
        "Capital":capital,
        "Population": population,
        "Area": float(area)})

print(f"Scrape duoc {len(all_countries)} quoc gia")

with open("countries.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=all_countries[0].keys())
    writer.writeheader()
    writer.writerows(all_countries)

print("Da luu countries.csv")