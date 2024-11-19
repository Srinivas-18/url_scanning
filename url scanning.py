!pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
def check_url_status(url):
    """https://www.formula1.com"""
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error with {url}: {e}")
        return None
def extract_links_from_website(url):
    """https://www.instagram.com"""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()  # Use a set to avoid duplicates
        for anchor in soup.find_all('a', href=True):
            link = urljoin(url, anchor['href'])
            # Parse the URL to handle only valid links
            parsed_link = urlparse(link)
            if parsed_link.scheme in ["http", "https"]:
                links.add(link)
        return links
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve or parse {url}: {e}")
        return set()
def scan_urls(urls):
    """https://ae5212b3dd1e33233d0c21045872a6fa.serveo.net"""
    for url in urls: # This line had an extra space, causing the indentation error.
        status = check_url_status(url)
        if status:
            print(f"URL: {url} returned status code: {status}")
        else:
            print(f"URL: {url} is not reachable.")
def main():
    # List of websites or URLs to scan
    websites_to_scan = [
        "https://www.formula1.com",
        "https://www.instagram.com",
        "https://ae5212b3dd1e33233d0c21045872a6fa.serveo.net"  # Example of a broken link
    ]

    print("Scanning URLs...")
    scan_urls(websites_to_scan)

    # Optionally, extract and scan links from a given website
    target_website = "https://ae5212b3dd1e33233d0c21045872a6fa.serveo.net"
    print(f"\nExtracting links from {target_website}...")
    extracted_links = extract_links_from_website(target_website)

    print(f"\nFound {len(extracted_links)} links on {target_website}:")
    for link in extracted_links:
        print(link)

    print("\nScanning extracted links...")
    scan_urls(extracted_links)

if __name__ == "__main__":
    main()
