
from selenium import webdriver

driver = webdriver.Chrome()

url = 'file:///Users/niketajenerette/Downloads/Udemy/QA%20Automation/Super%20SQA-%20Python-Selenium/selen3/iFrames/iFrames_example.html'

driver.get(url)

# Example outside of Frame
# driver.find_element('id', 'btnOutFrame').click()
# my_alert = driver.switch_to.alert
# my_alert_text = my_alert.text
# assert my_alert_text == 'Just Clicked Outside iFrame', "Should have gotten outside message"
# my_alert.dismiss()



# Notes:
#    To switch to the iframe use
#        WebElement
#         ID
#         Name
#         Index


# Example of iFrame, using WebElement
# my_frame = driver.find_element('id', 'myFrame1')
# driver.switch_to.frame(my_frame)
# driver.find_element('id', 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()

# switches back outside of frame to continue testing
# driver.switch_to.default_content()
# driver.find_element('id', 'btnOutFrame').click()
# driver.switch_to.alert.dismiss()


# Example of iFrame, using ID
# driver.switch_to.frame('myFrame1')
# driver.find_element('id', 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()

# Example of iFrame, using Index ---should get an error bc don't have ths button in frame
driver.switch_to.frame(1)
driver.find_element('id', 'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()