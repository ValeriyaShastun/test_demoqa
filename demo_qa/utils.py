from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import demo_qa.parameters as par
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ac


def allocate_element(locator, timeout, driver=par.driver):
    '''Finding element on page
    :param locator: web element on page
    :param timeout: time of waiting in sec prior finding element
    :param driver: chromedriver call
    in case element is not found on the page, function raises TimeoutException
    '''
    return WebDriverWait(driver, timeout).until(ac.presence_of_element_located(locator))

def click_on_web_element(web_element):
    web_element.click()






