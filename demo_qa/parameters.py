import os
from selenium import webdriver

url = 'https://demoqa.com/'

driverLocation = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)

# !Locators Homepage!
CATEGORY_CARDS_CLASS_NAME = 'category-cards'

# Elements
ELEMENTS_MAIN_MENU_CLASS_NAME = 'show'

# Locators Elements page - GENERAL
TEXT_BOX_ID = 'item-0'

#==Text Box form==
NAME_ID = 'userName'
EMAIL_ID = 'userEmail'
CURRENT_ADDRESS_ID = 'currentAddress'
PERMANENT_ADDRESS_ID = 'permanentAddress'
SUBMIT_BUTTON_ID = 'submit'
#===CHECKING Text Box submitted data===
CHECK_NAME_ID = 'name'
CHECK_EMAIL_ID = 'email'
CHECK_CURRENT_ADDRESS_CSS = 'p#currentAddress'
CHECK_PERMANENT_ADDRESS_CSS = 'p#permanentAddress'


