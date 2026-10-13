#-------------------------------------------------------------------------
# AUTHOR: Thuy An Nguyen
# FILENAME: scraper.py
# SPECIFICATION: A simple web scraper to crawl and extract information from a set of URLs
# FOR: CS 4250 - Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup
#for handling relative URLs
from urllib.parse import urljoin 

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"

# Creating the frontier and seen collections
frontier = [seed]
seen = [seed]


# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    url = frontier.pop(0)

    # Retrieving and parsing the Web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Printing the text contained in the <h1> element
    heading = soup.find("h1")
    if heading:
        print(heading.get_text())

    # Extracting and processing hyperlinks
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href:
            absolute_url = urljoin(url, href)
            if absolute_url.startswith(seed) and absolute_url not in seen:
                seen.append(absolute_url)
                frontier.append(absolute_url)


# Printing all URLs in seen
for url in seen:
    print(url)