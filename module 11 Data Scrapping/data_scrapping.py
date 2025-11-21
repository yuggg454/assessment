import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print("Failed to fetch page! Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print("\n--- Soup object created successfully! ---\n")
print(soup.prettify()[:500]) 

page_title = soup.title.string if soup.title else "No title found"
print("\nPage Title:", page_title)

links = soup.find_all("a")
print("\nFound", len(links), "links")
for link in links[:10]: 
    print("Link:", link.get("href"))

headings = soup.find_all("h1")
print("\nH1 Headings found:", len(headings))
for h in headings:
    print("Heading:", h.text.strip())

paragraphs = soup.find_all("p")
print("\nParagraphs found:", len(paragraphs))