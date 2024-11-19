This code performs three main tasks: 

1. **Check the HTTP status of given URLs.**  
2. **Extract links from a website.**  
3. **Scan the extracted links for their HTTP status.**

Here’s a step-by-step explanation of the code:

---

### 1. **Importing Necessary Libraries**
```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
```
- `requests`: Sends HTTP requests to websites.
- `BeautifulSoup`: Parses HTML and extracts elements like links.
- `urlparse` & `urljoin`: Used to handle and construct URLs properly.

---

### 2. **Function to Check the Status of a URL**
```python
def check_url_status(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error with {url}: {e}")
        return None
```
- **Purpose**: Check if a website is reachable by sending an HTTP request and returning its status code (e.g., 200 for success, 404 for not found).
- **How it Works**:
  1. Sends a request to the URL using `requests.get`.
  2. If the request succeeds, returns the HTTP status code.
  3. If an error occurs (e.g., timeout, connection error), it catches the exception, prints an error message, and returns `None`.

---

### 3. **Function to Extract Links from a Website**
```python
def extract_links_from_website(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        for anchor in soup.find_all('a', href=True):
            link = urljoin(url, anchor['href'])
            parsed_link = urlparse(link)
            if parsed_link.scheme in ["http", "https"]:
                links.add(link)
        return links
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve or parse {url}: {e}")
        return set()
```
- **Purpose**: Extract all valid (HTTP/HTTPS) links from a given website.
- **How it Works**:
  1. Sends a request to the website.
  2. Parses the website’s HTML using `BeautifulSoup`.
  3. Finds all `<a>` (anchor) tags with an `href` attribute, representing hyperlinks.
  4. Joins relative URLs (e.g., `/about`) to the base URL using `urljoin`.
  5. Filters links to include only `http` and `https` schemes.
  6. Returns a `set` of unique links. If an error occurs, returns an empty set.

---

### 4. **Function to Scan URLs**
```python
def scan_urls(urls):
    for url in urls:
        status = check_url_status(url)
        if status:
            print(f"URL: {url} returned status code: {status}")
        else:
            print(f"URL: {url} is not reachable.")
```
- **Purpose**: Checks the status of multiple URLs and prints their results.
- **How it Works**:
  1. Iterates over a list of URLs.
  2. Calls `check_url_status` for each URL.
  3. Prints whether the URL is reachable (with its status code) or not.

---

### 5. **Main Function**
```python
def main():
    websites_to_scan = [
        "https://www.formula1.com",
        "https://www.instagram.com",
        "https://ae5212b3dd1e33233d0c21045872a6fa.serveo.net"
    ]

    print("Scanning URLs...")
    scan_urls(websites_to_scan)

    target_website = "https://www.formula1.com"
   
