# Author: José Santos
# GitHub: https://github.com/engJoseSantos
#
# "Be sober-minded; be watchful. Your adversary the devil
# prowls around like a roaring lion, seeking someone to devour."
# — 1 Peter 5:8
#
# Stay alert. Stay secure.

import requests
from ui_utils import *
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

def make_request(url):
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        print(f"[{response.status_code}] {response.reason} - {url}\n")

        return response
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
        return None

def get_unique_links(response, url):
    soup = BeautifulSoup(response.text, "html.parser")


    links = []

    for a in soup.find_all("a", href=True):
        href = a.get("href")

        absolute_url = urljoin(url, href)
        links.append(absolute_url)

    return set(links)

def classify_links(links, base_url):
    internal_links = []
    external_links = []
    other_links = []

    base_domain = urlparse(base_url).netloc

    for href in links:

        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            other_links.append(href)
            continue

        parsed_url = urlparse(href)

        if parsed_url.scheme in ("http", "https"):

            if parsed_url.netloc == base_domain:
                internal_links.append(href)
            else:
                external_links.append(href)

        else:
            other_links.append(href)

    return internal_links, external_links, other_links

def get_headers(response):
    return response.headers
    

def detect_technologies(response):
    technologies = set()

    html = response.text.lower()
    response_headers = {key.lower(): value.lower() for key, value in response.headers.items()}

    # Server
    if "server" in response_headers:
        technologies.add(response_headers["server"])

    # X-Powered-By
    if "x-powered-by" in response_headers:
        technologies.add(response_headers["x-powered-by"])

    # WordPress
    if "wp-content" in html or "wp-includes" in html:
        technologies.add("WordPress")

    # Bootstrap
    if "bootstrap" in html:
        technologies.add("Bootstrap")

    # jQuery
    if "jquery" in html:
        technologies.add("jQuery")

    # React
    if "react" in html or "__react" in html:
        technologies.add("React")

    # Vue
    if "vue" in html:
        technologies.add("Vue.js")

    return technologies

def main():
    while True:
        print_title("Cyber Tool")
        print_warning()
        print("1. Get unique links")
        print("2. Classify links")
        print("3. Get headers")
        print("4. Get technologies")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            url = input("Enter URL: ").strip()

            if not is_valid_url(url):
                print("Invalid URL.")
                continue
            response = make_request(url)

            if response is None:
                continue

            links = get_unique_links(response, url)

            if links is not None:
                print(f"\nFound {len(links)} unique links:")

                for link in sorted(links):
                    print(f" - {link}")

        elif choice == "2":
            url = input("Enter URL: ").strip()

            if not is_valid_url(url):
                print("Invalid URL.")
                continue
            response = make_request(url)

            if response is None:
                continue

            links = get_unique_links(response, url)

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

            response = make_request(url)

            if response is None:
                continue


            response_headers = get_headers(response)

            if response_headers is not None:
                print("\nHTTP Headers:")

                for key, value in response_headers.items():
                    print(f" - {key}: {value}")


        elif choice == "4":
            url = input("Enter URL: ").strip()

            if not is_valid_url(url):
                print("Invalid URL.")
                continue

            response = make_request(url)

            if response is None:
                continue

            technologies = detect_technologies(response)

            print("\nTechnologies:")

            for technology in sorted(technologies):
                print(f" - {technology}")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()