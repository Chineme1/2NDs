"""
from bs4 import BeautifulSoup
import requests

html = requests.get("https://umdearborn.campuslabs.com/engage/events")
soup = BeautifulSoup(html, "lxml")

links = soup.find_all('a')
for link in links:
    print(link.get('href'))
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from total_scraper import scrape_all
from snaxk import  snack_all #this is for snacks/Maybe later

def MAIN_SCRAPER(url):
    # Initialize Selenium WebDriver (make sure to install the appropriate driver, e.g., ChromeDriver)
    driver = webdriver.Chrome()

    # Open the webpage
    driver.get(url)

    # Get the page source after JavaScript has executed
    html = driver.page_source

    # Parse the fully-rendered HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <a> tags with href attributes
    links = [a['href'] for a in soup.find_all('a', href=True)]
    #print(links)

    for i in range(len(links)):
        tmplist = links[i][1:].split("/")
        if(len(tmplist)==3):
            a, b, c = tmplist[0], tmplist[1], tmplist[2]
            urladdress_food = url[:len(url)-14]+links[i]
            print(urladdress_food)
            scrape_all(urladdress_food)

    # Close the browser
    driver.quit()



MAIN_SCRAPER('https://umdearborn.campuslabs.com/engage/events')
