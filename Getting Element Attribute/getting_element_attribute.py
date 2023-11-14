
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://myteststore.local/')

# example 1 is placeholder
search_field = driver.find_element('id', 'woocommerce-product-search-field-0')
place_holder = search_field.get_attribute('placeholder')
if place_holder != "Search products…":
    raise Exception("Placeholder for search field is not as expected. Actual: {}".format(place_holder))
else:
    print("PASS")

# Example (see which tab is selected)
# first click on my account

# my_acct = driver.find_element('css selector', 'li.page_item.page-item-10')
# my_acct.click()
#
# nav_items = driver.find_elements('css selector', 'ul.nav-menu li')
# for item in nav_items:
#     item_class = item.get_attribute('class')
#     if 'current_page_item' in item_class:
#         print("The selected tab is: {}".format(item.text))

# Example (Get Link URL)
product_link = driver.find_element('css selector', 'li.product a')
product_url = product_link.get_attribute('href')
print("The url for product is {}".format(product_url))
# import pdb; pdb.set_trace()


