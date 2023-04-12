## Packges Needed:
## pip install selenium
## pip install webdriver_manager
## pip install beautifulsoup4

##############
import selenium.webdriver as webdriver
'''
WHAT IS SELENIUM?
Selenium is a powerful tool for controlling web browsers and performing browser automation.

What is Selenium WebDriver? 
The selenium.webdriver module provides all the WebDriver implementations. 
Currently supported WebDriver implementations are Firefox, Chrome
'''
##############################################
from selenium.webdriver.chrome.options import Options
"""
The Chromeoptions Class is a concept in Selenium WebDriver for manipulating various properties of the Chrome drive
It helps you perform various operations like opening Chrome in maximized mode, disable existing extensions, disable pop-ups, etc.
"""
##############################################
from selenium.webdriver.chrome.service import Service
''' A Service class that is responsible for the starting and stopping of chromedriver'''
###############################################
from bs4 import BeautifulSoup
'''
What Is Beautiful Soup?
 It is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files. 
 It creates a parse tree from the page source code that can be used to extract data in a order and more readable manner.
'''

## For more Chrom Options:
# https://www.guru99.com/chrome-options-desiredcapabilities.html#:~:text=The%20Chromeoptions%20Class%20is%20a,for%20customizing%20Chrome%20driver%20sessions.

chrome_options = Options()
## Chrome Options:

# chrome_options.add_argument('incognito') ## Opens Chrome in incognito mode

# chrome_options.add_argument('--user-agent=DuckDuckBot')

# chrome_options.add_experimental_option("detach", True) ## chromedriver will stay open afterward

# chrome_options.add_argument('--headless') ## chrome window will not popup

# 1. Passes the chromedriver path to the service object
# 2. stores the service object in the s variable
service_obj = Service("WebDrivers_path\chromedriver.exe")

# 1. Passes service object into the webdriver.Chrome
# 2. Stores object in driver variable
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

##'https://www.google.com'

##################
amazon_base_url = "https://www.amazon.com"
lindt ='B07BNNQJSL'
product = 'B076B7V2QJ'

amazon_product_url = amazon_base_url + "/dp/" + product
driver.get(amazon_product_url)
time.sleep(2)  # imp to sleep
page_title = driver.title
print(page_title)
assert "Amazon.com : Wholesale Ferrero Rocher Choc 12pc 5.3oz : Grocery & Gourmet Food" in page_title

##################
##  Beautiful Soup Documentation
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

html_page_source = driver.page_source
soup = BeautifulSoup(html_page_source, "html.parser")

print(soup.prettify())
print(soup.get_text())

# 2 -  Get Review Link
review_link = soup.find("a", {'data-hook': "see-all-reviews-link-foot"})
review_link = review_link['href']
print(review_link)

# 3- Open Reviews page
reviews_url = amazon_base_url + review_link
driver.get(reviews_url)
# print(reviews_url)
html2 = driver.page_source
soup = BeautifulSoup(html2, "html.parser")

###########################

# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
rev_html = soup.find_all("div", {'data-hook': "review"})

rev_string = str(rev_html)
# rev_string = rev_string.split('div></div></div></div></div></div>')
# print(rev_string)

product_name = soup.find("a", {'data-hook': "product-link"}).text.strip("\n")
reviews_title = soup.find("a", {'data-hook': "review-title"}).text.strip("\n")
reviews_body = soup.find("span", {'data-hook': "review-body"}).text.strip("\n")
reviews_date = soup.find("span", {'data-hook': "review-date"}).text.strip("\n")
reviews_stars = soup.find("i", {'data-hook': "review-star-rating"}).text.strip("\n")

print(f'product_name: {product_name}')
print(f'reviews_title: {reviews_title}')
print(f'reviews_body: {reviews_body}')
print(f'reviews_date: {reviews_date}')
print(f'reviews_stars: {reviews_stars}')

driver.quit()   # closes the browser
