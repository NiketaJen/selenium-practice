
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
url = 'file:///Users/niketajenerette/Downloads/Udemy/QA%20Automation/Super%20SQA-%20Python-Selenium/selen3/Alerts/alerts_example.html'

driver.get(url)

# Example 1
alrt_1_btn = driver.find_element('css selector', 'div#jsAlertExample button')
alrt_1_btn.click()

my_alert = driver.switch_to.alert
assert my_alert.text == 'I am a Javascript Alert', "Unexpected text on alert"
my_alert.accept()
# my_alert.dismiss()

# Example 2
my_js_confirm_btn = driver.find_element('css selector', 'div#jsConfirmExample button')
my_js_confirm_btn.click()
my_confirm_alert = driver.switch_to.alert
# my_confirm_alert.accept()
# rs_message = driver.find_element('id', 'userResponse1').text
# assert rs_message == 'Great! You will love it!', "Wrong message after accepting"

my_confirm_alert.dismiss()
rs_message = driver.find_element('id', 'userResponse1').text
assert rs_message == "Too bad!!! You would've loved it!", "Wrong message after accepting"


# Example 3 send keys
# my_prompt_btn = driver.find_element('css selector', "div#jsPromptExample button")
# my_prompt_btn.click()
#
# my_prompt_btn.send_keys("Mighty Mouse")
# my_prompt_alert = driver.switch_to.alert
# my_prompt_alert.accept()


import pdb; pdb.set_trace()