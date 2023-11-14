
from selenium import webdriver

driver = webdriver.Chrome()

url = 'file:///Users/niketajenerette/Downloads/Udemy/QA%20Automation/Super%20SQA-%20Python-Selenium/selen3/Multiple_Windows_and_Tabs/windows-and_tabs_example.html'

driver.get(url)

driver.find_element('xpath', '//*[@id="windows"]/a[1]').click()
print("Before switching focus: " + driver.title)
original_window_handle = driver.current_window_handle
all_window_handles = driver.window_handles
new_window = all_window_handles[1]
driver.switch_to.window(new_window)
print("After switching focus: " + driver.title)
print("Closing Tab")
driver.close()
print("Switching back to original")
driver.switch_to.window(original_window_handle)

import pdb; pdb.set_trace()