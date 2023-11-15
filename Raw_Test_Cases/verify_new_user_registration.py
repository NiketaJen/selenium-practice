
from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
time.sleep(2)

url = 'http://myteststore.local/my-account/'
email_field_id = 'reg_email'
password_field_id = 'reg_password'
logout_btn_css = 'li.woocommerce-MyAccount-navigation-link--customer-logout  a'

# go to the url
driver.get(url)

# user is able to register account
email_field = driver.find_element(By.ID, email_field_id)

# generate random email
letters = string.ascii_lowercase
rand_string = ''.join(random.choice(letters) for i in range(15))
random_email = rand_string + '@supersqa.com'

# type in the email field
email_field.send_keys(random_email)

# find password field and enter password
password_field = driver.find_element(By.ID, password_field_id)
password_field.send_keys('mypassword!12345')

time.sleep(2)
register_button = driver.find_element(By.CSS_SELECTOR, 'button[value="Register"]')
register_button.click()
print("I clicked the button")
try:
    logout_btn = driver.find_element(By.CSS_SELECTOR, logout_btn_css)
except:
    raise Exception("User not logged in after registering")

if logout_btn.is_displayed():
    print("PASS")
else:
    raise Exception("User not logged in after registering")