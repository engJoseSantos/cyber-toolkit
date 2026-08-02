import requests
from bs4 import BeautifulSoup

#url = "https://nmap.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

def get_unique_links(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")


    links = []

    for a in soup.find_all("a"):
        href = a.get("href")
        if href:
            links.append(href)

    return set(links)

if __name__ == "__main__":
    url = input("Type the URL to find links: ")
    unique_links = get_unique_links(url)
    for link in unique_links:
        print(link)