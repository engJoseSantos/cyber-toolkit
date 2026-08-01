import requests
from bs4 import BeautifulSoup

url = "https://nmap.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

#print(soup)

links = []

for a in soup.find_all("a"):
    href = a.get("href")
    if href:
        links.append(href)

unique_links = set(links)

for link in unique_links:
    print(link)