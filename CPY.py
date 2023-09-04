import os
import requests
from bs4 import BeautifulSoup

# Function to create a directory for the mirrored website
def create_website_directory(url):
    website_name = url.split("//")[1].replace("/", "_")
    if not os.path.exists(website_name):
        os.makedirs(website_name)
    return website_name

# Function to download and save a web page
def save_web_page(url, website_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            page_name = "index.html" if url == website_name else url.split("/")[-1]
            with open(os.path.join(website_name, page_name), "wb") as f:
                f.write(response.content)
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

# Function to recursively mirror a website
def mirror_website(url):
    website_name = create_website_directory(url)
    save_web_page(url, website_name)
    
    # Parse the HTML to find links and assets
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    
    for link in soup.find_all("a", href=True):
        href = link.get("href")
        if not href.startswith("http"):
            href = url + href
        if href.startswith(url):
            save_web_page(href, website_name)

if __name__ == "__main__":
    target_url = "https://www.example.com"  # Replace with the URL of the website you want to mirror
    mirror_website(target_url)
