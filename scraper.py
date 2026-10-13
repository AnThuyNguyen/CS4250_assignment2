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
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Printing the text contained in the <h1> element
    heading = soup.find("h1")
    if heading:
        print(heading.get_text())

    # Extracting and processing hyperlinks
    # --> add your Python code here


# Printing all URLs in seen
# --> add your Python code here