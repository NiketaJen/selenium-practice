# Error: "chromedriver" cannot be opened because the developer cannot be verified
# Solution:  xattr -d com.apple.quarantine /Users/niketajenerette/Downloads/chromedriver-mac-x64/chromedriver
# Solution:  xattr -d com.apple.quarantine /Users/niketajenerette/Downloads/chromedriver-mac-x64/chromedriver


from selenium import webdriver


### Chrome
# driver = webdriver.Chrome()
# driver.get('http://myteststore.local/')


### Firefox
# driver = webdriver.Firefox()
# driver.get('http://demostore.supersqa.com')

### Safari
driver = webdriver.Safari()
driver.get('http://demostore.supersqa.com')