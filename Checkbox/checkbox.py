
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.get('file:///Users/niketajenerette/Downloads/Udemy/QA%20Automation/Super%20SQA-%20Python-Selenium/selen3/Checkbox/checkbox_example.html')
time.sleep(2)

# Example 1
# to_select_value = '61-80'
# locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'
# my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
# my_choice.click()
# assert my_choice.is_selected(), f"After clicking value {to_select_value} it is not selected."

# Example 2 verify number of checkboxes and they are selectable
expected_number_of_options = 4
all_checkboxes = driver.find_elements(By.NAME, 'age-group-checkbox')
assert len(all_checkboxes) == expected_number_of_options, "Number of checkboxes is not the expected number."

for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkbox with value '{value}' is selectable")
    else:
        raise Exception(f"Value '{value}' is not selectable")

# import pdb; pdb.set_trace()