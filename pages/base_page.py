from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from tests.settings import *

class Base_page:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.get_url()


    def get_url(self):
        self.driver.get(default_url)

    def wait_for(self, *locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    def check_page_base(self, link_end):
        if (self.driver.current_url) == f"{default_url+link_end}":
            return True
        else:
            return False

    def __del__(self):
        self.driver.close()