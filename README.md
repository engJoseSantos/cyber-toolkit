# cyber-toolkit
A modular Python cybersecurity toolkit for learning and practical use

A simple Python reconnaissance tool that extracts unique links from a given website.

This project is part of my cybersecurity learning journey and focuses on practicing Python, HTTP requests, HTML parsing, and basic web reconnaissance concepts.

## Features

* Accepts a target URL from the user
* Sends an HTTP request using `Requests`
* Parses HTML content with `BeautifulSoup`
* Extracts links from `<a>` tags
* Removes duplicate links
* Prints the discovered links to the terminal
* Uses basic error handling as the project evolves

## Technologies

* **Python 3**
* **Requests** — HTTP requests
* **Beautiful Soup 4** — HTML parsing

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/web-link-extractor.git
cd web-link-extractor
```

Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script:

```bash
python main.py
```

Enter the URL when prompted:

```text
Type the URL to find links: https://example.com
```

The tool will then display the unique links found on the page.

## Example

```text
Type the URL to find links: https://example.com

https://example.com/about
https://example.com/contact
/login
https://github.com/
```

## Project Structure

```text
web-link-extractor/
│
├── main.py
├── README.md
└── requirements.txt
```

## Security & Ethical Use

This tool is intended for **educational purposes, cybersecurity labs, and authorized security testing**.

Only scan websites and systems that you own or have explicit permission to test.

Do not use this tool to perform unauthorized reconnaissance against third-party systems.

## Future Improvements

Planned improvements include:

* [ ] URL validation
* [ ] HTTP error and timeout handling
* [ ] Convert relative URLs into absolute URLs
* [ ] Separate internal and external links
* [ ] Extract forms and input fields
* [ ] Extract HTTP response headers
* [ ] Save results to a text or JSON file
* [ ] Add command-line arguments
* [ ] Improve project structure as the tool grows

## Author

**José Santos**

GitHub: https://github.com/yourusername
