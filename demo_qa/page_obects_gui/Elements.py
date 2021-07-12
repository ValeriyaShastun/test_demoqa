from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import demo_qa.parameters as par
import demo_qa.utils as util

class Elements():

    def __init__(self, url=f'{par.url}elements', driver=par.driver):
        '''Getting Elements page
        :param url: url of Elements page
        :param driver: chromedriver call'''
        driver.get(url)

    def elements_page_verification(self):
        '''Verification of correctness of page by
        checking presence of main menu --- using utils method'''
        try:
            list_el = (By.CLASS_NAME, par.ELEMENTS_MAIN_MENU_CLASS_NAME)
            self.found_list_el = util.allocate_element(list_el, 5)
        except AssertionError as error:
            print(f"Element was not found on the page: {error}")

#===================TEXT BOX FUNCTIONALITY=========================

    def verify_text_box(self):
        '''Verify that Text Box is available ---- OPTIONAL'''
        try:
            text_box_elements = self.found_list_el.text
            y = text_box_elements.split("\n")
            text_box_element = 'None'
            for t in y:
                if t == 'Text Box':
                    text_box_element = t
                else:
                    pass
            print(f'The element {text_box_element} is found')
        except AssertionError as error:
            print(f"Element was not found of the page: {error}")

    def click_text_box(self):
        '''Click on Text Box'''
        text_box = par.driver.find_element_by_id(par.TEXT_BOX_ID)
        util.click_on_web_element(text_box)

    def fill_in_text_box_name(self, name_text):
        '''Filling in "TextBox" field "Name"
        :param Name: Name in string format
        '''
        self.text_from_name = name_text
        name_form = (By.ID, par.NAME_ID)
        self.name_form_find = util.allocate_element(name_form, 5)
        self.name_form_find.clear()
        try:
            if isinstance(name_text, str) == True:
                return self.name_form_find.send_keys(name_text)
            else:
                raise ValueError
        except ValueError as error:
            print(f'This function receives only string as name {error}')

    def fill_in_text_box_email(self, email):
        '''Filling in "TextBox" field "Email"
        :param Email: Email in string format
        '''
        self.text_from_email = email
        email_form = (By.ID, par.EMAIL_ID)
        self.email_form_find = util.allocate_element(email_form, 5)
        self.email_form_find.clear()

        try:
            if isinstance(email, str):
                return self.email_form_find.send_keys(email)
            else:
                raise ValueError
        except ValueError as error:
            print(f'This function receives only string as e-mail {error}')

    def fill_in_text_box_current_address(self, current_address):
        '''Filling in "TextBox" field "Current Address"
        :param current_address: Current address in string format
        '''
        self.text_from_current_address = current_address
        current_address_form = (By.ID, par.CURRENT_ADDRESS_ID)
        self.current_address_form_find = util.allocate_element(current_address_form, 5)
        self.current_address_form_find.clear()

        try:
            if isinstance(current_address, str):
                return self.current_address_form_find.send_keys(current_address)
            else:
                raise ValueError
        except ValueError as error:
            print(f'This function receives only string as Current Address {error}')

    def fill_in_text_box_permanent_address(self, permanent_address):
        '''Filling in "TextBox" field "Permanent Address"
        :param permanent_address: Permanent address in string format
        '''
        self.text_from_permanent_address = permanent_address
        permanent_address_form = (By.ID, par.PERMANENT_ADDRESS_ID)
        self.permanent_address_form_find = util.allocate_element(permanent_address_form, 5)
        self.permanent_address_form_find.clear()
        try:
            if isinstance(permanent_address, str):
                return self.permanent_address_form_find.send_keys(permanent_address)
            else:
                raise ValueError
        except ValueError as error:
            print(f'This function receives only string as Permanent Address {error}')

    def text_box_press_submit(self):
        '''Pressing submit button in "TextBox"
        '''
        submit_button = (By.ID, par.SUBMIT_BUTTON_ID)
        self.submit_button_find = util.allocate_element(submit_button, 5)
        self.submit_button_find.click()

    def checking_filled_name_text_box(self):
        '''Checking filled info after submitting in "TextBox", field "Name"
        '''
        name_form_check = (By.ID, par.CHECK_NAME_ID)
        self.name_form_check_find = util.allocate_element(name_form_check, 5)
        print(self.name_form_check_find.text)
        try:
            if self.name_form_check_find.text == f'Name:{self.text_from_name}':
                print('Element Name is correspondent with previously entered into Text Box')
            else:
                raise AssertionError
        except AssertionError as error:
            print(f"Element Name was not found on the page: {error}")

    def checking_filled_email_text_box(self):
        email_form_check = (By.ID, par.CHECK_EMAIL_ID)
        self.email_form_check_find = util.allocate_element(email_form_check, 5)
        print(self.email_form_check_find.text)
        try:
            if self.email_form_check_find.text == f'Email:{self.text_from_email}':
                print('Element Email is correspondent with previously entered into Text Box')
            else:
                raise AssertionError
        except AssertionError as error:
            print(f"Element Email was not found on the page: {error}")

    def checking_filled_current_address_text_box(self):
        current_address_form_check = (By.CSS_SELECTOR, par.CHECK_CURRENT_ADDRESS_CSS)
        self.current_address_form_check_find = util.allocate_element(current_address_form_check, 5)
        print(self.current_address_form_check_find.text)
        try:
            if self.current_address_form_check_find.text == f'Current Address :{self.text_from_current_address}':
                print('Element Current Address is correspondent with previously entered into Text Box')
            else:
                raise AssertionError
        except AssertionError as error:
            print(f"Element Current Address was not found on the page: {error}")

    def checking_filled_permanent_address_text_box(self):
        permanent_address_form_check = (By.CSS_SELECTOR, par.CHECK_PERMANENT_ADDRESS_CSS)
        self.permanent_address_form_check_find = util.allocate_element(permanent_address_form_check, 5)
        print(self.permanent_address_form_check_find.text)
        try:
            if self.permanent_address_form_check_find.text == f'Permananet Address :{self.text_from_permanent_address}':
                print('Element Permanent Address is correspondent with previously entered into Text Box')
            else:
                raise AssertionError
        except AssertionError as error:
            print(f"Element Permanent Address was not found on the page: {error}")

#===================CHECK BOX FUNCTIONALITY=========================

#   STILL TO GO: create functions for working with every item in Elements




