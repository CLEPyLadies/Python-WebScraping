## Packges Needed:
## pip install selenium
## pip install webdriver_manager
## pip install beautifulsoup4

##############
"""
# Project Dependency :
    # pip install selenium
    # pip install webdriver_manager
    # pip install beautifulsoup4
"""
import time

from selenium import webdriver

from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
## For more Chrom Options:
# https://www.guru99.com/chrome-options-desiredcapabilities.html#:~:text=The%20Chromeoptions%20Class%20is%20a,for%20customizing%20Chrome%20driver%20sessions.


# Chrome Options -------------------------------------:

chrome_options.add_argument('incognito')  ## Opens Chrome in incognito mode
# chrome_options.add_experimental_option("detach", False) ## chromedriver will stay open afterward
# chrome_options.add_argument('--headless') ## chrome window will not pop up

# starting code -----------------------------------------:
# selenium Documentaion:
# https://selenium-python.readthedocs.io/getting-started.html

driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.google.com/')  # testing

amazon_base_url = "https://www.amazon.com"
lindt = 'B07BNNQJSL'  # Amazon product code
product = 'B076B7V2QJ'

amazon_product_url = amazon_base_url + "/dp/" + product
driver.get(amazon_product_url)

time.sleep(2)  # imp to sleep

page_title = driver.title  # get webpage title

# print(page_title)

##################
##  Beautiful Soup Documentation
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#
html_page_source = driver.page_source
# print(html_page_source)
soup = BeautifulSoup(html_page_source, "html.parser")

# print(soup.prettify())
# print(soup.get_text())

# 2 -  Get Review Link
review_link = soup.find("a", {'data-hook': "see-all-reviews-link-foot"})
review_link = review_link['href']
# print(review_link)

# 3- Open Reviews page
reviews_url = amazon_base_url + review_link
driver.get(reviews_url)
# print(reviews_url)
html2 = driver.page_source
soup = BeautifulSoup(html2, "html.parser")

###########################

rev_html = soup.find_all("div", {'data-hook': "review"})

Rev_String = str(rev_html)

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

# driver.quit()   # closes the browser
