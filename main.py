# Author: José Santos
# GitHub: https://github.com/engJoseSantos
#
# "Be sober-minded; be watchful. Your adversary the devil
# prowls around like a roaring lion, seeking someone to devour."
# — 1 Peter 5:8
#
# Stay alert. Stay secure.

import requests
from bs4 import BeautifulSoup

TIMEOUT = 10

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

def get_unique_links(url):
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        soup = BeautifulSoup(response.text, "html.parser")


        links = []

        for a in soup.find_all("a", href=True):
            href = a.get("href")
            if href:
                links.append(href)

        return set(links)
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
        return None


def get_headers(url):
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()

        return response.headers
    
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
        return None

if __name__ == "__main__":
    url = input("Type the URL to find links: ").strip()
    unique_links = get_unique_links(url)

    if unique_links:
        print(f"Found {len(unique_links)} unique links")

        for link in unique_links:
            print(link)

    #response_headers = get_headers(url)

    #if response_headers:
    #    print("\nHTTP Headers:")
    #    for name, value in response_headers.items():
    #       print(f"{name}: {value}")
