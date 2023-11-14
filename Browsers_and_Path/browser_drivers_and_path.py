# Error: "chromedriver" cannot be opened because the developer cannot be verified
# Solution:  xattr -d com.apple.quarantine /Users/niketajenerette/Downloads/chromedriver-mac-x64/chromedriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# option 1 (Selenium 3)
# driver = webdriver.Chrome(executable_path='/Users/niketajenerette/Downloads/chromedriver-mac-x64/chromedriver')
# driver.get("https://google.com")

# option 1 (Selenium 4)
# se = Service(executable_path='/Users/niketajenerette/Downloads/chromedriver-mac-x64/chromedriver')
# driver = webdriver.Chrome(service=se)

# option 2 adding the executable to system path (preferred)
driver = webdriver.Chrome()
