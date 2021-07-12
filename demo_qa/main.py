from selenium.webdriver.common.by import By
import demo_qa.parameters as par
import demo_qa.utils as util


class HomePage():

    def __init__(self, url=par.url, driver=par.driver):
        '''Getting Home page
        :param url: url of home page
        :param driver: chromedriver call'''
        driver.get(url)

    def page_verification(self):
        '''Verification of correctness of page by
        checking presence of main menu --- using utils method'''
        try:
            menu_el = (By.CLASS_NAME, par.CATEGORY_CARDS_CLASS_NAME)
            self.found_menu_el = util.allocate_element(menu_el, 5)
        except AssertionError as error:
            print(f"Element was not found of the page: {error}")

    # def page_verification_duplicate(self):
    #     '''Verification of correctness of page by
    #     checking presence of main menu --- using time.sleep and find_by_element'''
    #     try:
    #         time.sleep(3)
    #         self.found_menu_el = par.driver.find_element_by_class_name('category-cards')
    #     except AssertionError as error:
    #         print(f"Element was not found of the page: {error}")
