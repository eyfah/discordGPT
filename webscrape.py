import re

import requests
from bs4 import BeautifulSoup

url_pattern = r"(https?://[^\s]+)"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


def get_url(prompt):
    urls = re.findall(url_pattern, prompt)
    for url in urls:
        print(f"url: {url}")
        return url


def parse(url):
    response = requests.get(url, headers=headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    print(text)
    return text
