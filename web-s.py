# Libraries to import for web scraping
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Web scrape Rate My Professor
# Note: Before web scraping any website, check to make sure it is fine to do so
# You can do this via www.website.com/robots.txt
url = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1167426'

# Download Chrome Driver and get url through browser
browser = webdriver.Chrome()
browser.get(url)

# Find class code and number
browser.find_element_by_xpath('//*[@id="ratingsList"]/li[1]/div/div/div[3]/div[1]/div[1]/div[1]')