
from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.get('http://myteststore.local/')


cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()

driver.get('http://myteststore.local/my-account/')
u_name = driver.find_element(By.ID, 'username')
u_name.send_keys('myusername')

pdb.set_trace()

# to find available methods just do dir(<variable>)
# Example: dir(driver)
# Example: dir(cart)