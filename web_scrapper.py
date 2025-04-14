import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])
        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = ", ".join(tag.text for tag in quote.find_all("a", class_="tag"))
            writer.writerow([text, author, tags])
    print("Scraping complete! Check 'quotes.csv'.")

if __name__ == "__main__":
    scrape_quotes()