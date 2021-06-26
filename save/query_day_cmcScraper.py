
from cryptocmd import CmcScraper
scraper = CmcScraper("BTC", "15-01-2021", "17-06-2021")
headers, data = scraper.get_data()
json_data = scraper.get_data("json")

for data in data:
    print(data)

print("done")