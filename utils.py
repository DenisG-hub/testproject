import os
from selenium import webdriver

class Herokuapp(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def visit_page1(self):
        self.driver.get("http://the-internet.herokuapp.com/dynamic_content")
        self.driver.implicitly_wait(10)
        return self.driver.find_elements_by_xpath("//*/div/img")

    def visit_page2(self):
        self.driver.get("http://the-internet.herokuapp.com/upload")
        self.driver.implicitly_wait(10)

    def load_file(self):
        self.visit_page2()
        file = os.path.abspath("test_text.txt")
        self.driver.find_element_by_id("file-upload").send_keys(file)
        self.driver.find_element_by_id("file-submit").click()

    def teardown(self):
        self.driver.quit()
