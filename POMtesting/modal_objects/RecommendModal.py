'''
Created on Jul 3, 2013

@author: padelstein
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from robot.libraries.BuiltIn import BuiltIn

class RecommendModal():

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
     
    def submit_recommend(self):
        self.enter_email()
        self.enter_message()
        self.submit() 
       
    def enter_email(self):
        _recommend_email_form = self._webd_wrap._driver.find_element_by_id('recommend-modal').find_element_by_id('recommend-email-form')
        self._webd_wrap._driver.execute_script('$(arguments[0]).val(arguments[1])', _recommend_email_form.find_elements_by_class_name('textboxlist-bit-editable-input')[0], '1@zolabooks.com')
        
    def enter_message(self):
        checkbox = self._webd_wrap._driver.find_element_by_id('uniform-share-with-followers').find_element_by_xpath('span/input')
        self._webd_wrap._driver.execute_script("$(arguments[0]).click()", checkbox)
        
    def submit(self):
        send = self._webd_wrap._driver.find_element_by_id('recommend-modal').find_element_by_id("recommend-email-form").find_element_by_xpath("footer/input")
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", send)
        
    def close_modal(self):
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)