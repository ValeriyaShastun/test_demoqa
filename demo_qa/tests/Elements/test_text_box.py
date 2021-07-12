import time

import unittest

from selenium.webdriver.common.by import By
from demo_qa.page_obects_gui.Elements import Elements
import demo_qa.parameters as par
import demo_qa.utils as util

page = Elements()

class Fill_in_form(unittest.TestCase):

    @classmethod
    def setUp(self):
        page.elements_page_verification()

    def test_02_check_submitted_info(self):
        #arrange
        page.verify_text_box()
        page.click_text_box()
        time.sleep(3)
        page.fill_in_text_box_name(name_text='Valeriya')
        page.fill_in_text_box_email(email='aaabbb@gmail.com')
        page.fill_in_text_box_current_address(current_address='Ukraine, Odessa, Onilovoy ave 18')
        page.fill_in_text_box_permanent_address(permanent_address='Ukraine, Odessa, Onilovoy ave 18')
        #act
        page.text_box_press_submit()
        #assert
        time.sleep(3)
        page.checking_filled_name_text_box()
        page.checking_filled_email_text_box()
        page.checking_filled_current_address_text_box()
        page.checking_filled_permanent_address_text_box()

    @classmethod
    def tearDown(self):
        par.driver.quit()



