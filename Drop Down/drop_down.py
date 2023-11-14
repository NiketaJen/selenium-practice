
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get('file:///Users/niketajenerette/Downloads/Udemy/QA%20Automation/Super%20SQA-%20Python-Selenium/selen3/Drop%20Down/drop_down_example.html')

my_dropdown = driver.find_element('id', 'age-range-select')

# Option 1 is using the Select Class
# dropdown_object = Select(my_dropdown)
# dropdown_object.select_by_index(3)
# dropdown_object.select_by_value('21-40')
# all_options = dropdown_object.options
# for option in all_options:
#     print(option.text)

# Option 2
dropdown_btn = driver.find_element('id', 'dropdownMenuButton')
dropdown_btn.click()
my_option = driver.find_element('xpath', '//*[@id="dropdowns"]/div[2]/div/ul/li[1]/a')
my_option.click()

import pdb; pdb.set_trace()