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
# from tinydb import TinyDB, Query
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



def MAIN_SCRAPER(url):
    # Initialize Selenium WebDriver (make sure to install the appropriate driver, e.g., ChromeDriver)
    options = Options()
    #options.headless = True  # Run Chrome in headless mode
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')

    # Initialize the Selenium WebDriver with options
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Open the webpage
    driver.get(url)

    # Get the page source after JavaScript has executed
    html = driver.page_source

    # Parse the fully-rendered HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <a> tags with href attributes
    links = [a['href'] for a in soup.find_all('a', href=True)]
    #print(links)
    tot_lst =[]
    for i in range(len(links)):
        tmplist = links[i][1:].split("/")
        if(len(tmplist)==3):
            a, b, c = tmplist[0], tmplist[1], tmplist[2]
            urladdress_food = url[:len(url)-14]+links[i]
            # print(urladdress_food)
            info=scrape_all(urladdress_food)
            #get this and call database
            if(info != None):
                tot_lst.append([info[0], info[1], info[2], info[3]])
                #db.insert({'title':info[0], 'Location': info[1], 'start_time' :  info[2] , 'end_time' : info[3]})
            #db.insert({'title': 'John', 'Location': ' ', 'start_time' : '', 'end_time' : ' '})
    #post on website #tbd
    driver.quit()
    return tot_lst
    # Close the browser


