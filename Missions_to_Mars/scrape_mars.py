from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import time
def scrape():
    def init_browser():
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        return browser

    #Scraping code for Nasa Mars News
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find("div", class_="content_title").get_text()
    news_p =soup.find("div", class_="article_teaser_body").get_text()
    browser.quit()

    #Scrapeing code for JPL Featured Space Image
    browser = init_browser()
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    browser.find_by_id('full_image').click()
    html = browser.html
    soup = bs(html, "html.parser")
    full_image = browser.find_by_css('.fancybox-image')['src']
    browser.quit()

    #Scraping code for Martian Weather
    browser = init_browser()
    url3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    time.sleep(5)
    html = browser.html
    soup = bs(html, "html.parser")
    mars_weather = soup.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    browser.quit()
    #Scraping code 
    url4 = "https://space-facts.com/mars/"
    tables = pd.read_html(url4)
    facts = tables[1]
    facts_html = facts.to_html()
    #Depositing into table
