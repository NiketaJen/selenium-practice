
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://myteststore.local/')

#cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart')
#my_acct = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-10 > a')

my_acct = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
time.sleep(3)
#cart.click()
my_acct.click()

