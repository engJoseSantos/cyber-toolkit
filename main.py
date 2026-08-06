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
from urllib.parse import urljoin, urlparse

TIMEOUT = 10

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

def is_valid_url(url: str) -> bool:

    if not url or not isinstance(url, str):
        return False
    
    parsed = urlparse(url) 

    return (parsed.scheme in ("http", "https") and bool(parsed.hostname))

def get_unique_links(url):
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        soup = BeautifulSoup(response.text, "html.parser")


        links = []

        for a in soup.find_all("a", href=True):
            href = a.get("href")

            absolute_url = urljoin(url, href)
            links.append(absolute_url)

        return set(links)
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
        return None

def classify_links(links):
    web_links = []
    other_links = []

    for href in links:

        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            other_links.append(href)
            continue

        parsed_url = urlparse(href)

        if parsed_url.scheme in ("http", "https"):
            web_links.append(href)
        else:
            other_links.append(href)

    return web_links, other_links

def get_headers(url):
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()

        return response.headers
    
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
        return None

        
def main():
    while True:
        print("\n=== Cyber Tool ===")
        print("1. Get unique links")
        print("2. Classify links")
        print("3. Get headers")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            url = input("Enter URL: ").strip()

            if not is_valid_url(url):
                print("Invalid URL.")
                continue

            links = get_unique_links(url)

            if links is not None:
                print(f"\nFound {len(links)} unique links:")

                for link in sorted(links):
                    print(f" - {link}")

        elif choice == "2":
            url = input("Enter URL: ").strip()

            if not is_valid_url(url):
                print("Invalid URL.")
                continue

            links = get_unique_links(url)

            if links is None:
                continue

            web_links, other_links = classify_links(links)

            print(f"\nWeb links ({len(web_links)}):")

            for link in sorted(web_links):
                print(f" - {link}")

            print(f"\nOther links ({len(other_links)}):")

            for link in sorted(other_links):
                print(f" - {link}")

        elif choice == "3":
            url = input("Enter URL: ").strip()

            if not is_valid_url(url):
                print("Invalid URL.")
                continue

            response_headers = get_headers(url)

            if response_headers is not None:
                print("\nHTTP Headers:")

                for key, value in response_headers.items():
                    print(f" - {key}: {value}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()