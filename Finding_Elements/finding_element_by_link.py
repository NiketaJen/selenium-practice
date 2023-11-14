
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://myteststore.local/')


# Must be an <a> tag
cart_elm = driver.find_element(By.LINK_TEXT, 'Cart')
print(cart_elm.text)

acct_elm = driver.find_element(By.LINK_TEXT, 'My account')
print(acct_elm.text)

# find by partial link text
acct_elm_p = driver.find_element(By.PARTIAL_LINK_TEXT, 'account')
print(acct_elm_p.text)

footer_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Built with Storefront')
print(footer_link.text)