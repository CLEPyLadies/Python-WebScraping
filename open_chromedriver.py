from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from selenium import webdriver


chrome_options = Options()

# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument('--disable-extensions')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=900,1050')
# chrome_options.add_argument('--incognito')
# chrome_options.add_argument("start-minimized")  # open Browser in maximized mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("disable-infobars")  # disabling infobars
chrome_options.add_argument("--disable-extensions")  # disabling extensions
chrome_options.add_argument("--disable-gpu")  # applicable to windows os only
chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
chrome_options.add_argument('--incognito')
chrome_options.add_experimental_option("detach", False)  # keep chrome open

# chrome_options.add_argument('--headless')


#
try:
    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                            # and if it doesn't exist, download it automatically,
                                            # then add chromedriver to path
    driver = webdriver.Chrome(service=Service(),options=chrome_options)
    print(f' Chrome Version: ', driver.capabilities['browserVersion'])
    driver.get('https://www.google.com/')

    # driver.minimize_window()  # minimize window after opening
except Exception as e:
    print(e)
