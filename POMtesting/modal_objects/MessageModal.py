'''
Created on Jul 10, 2013

@author: emma
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from robot.libraries.BuiltIn import BuiltIn

import time

class MessageModal:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def close_modal(self):
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
        
    ########################################################################
    ########################################################################
    
    def enter_message(self, _message):
        _message_field = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_id('message-form').find_element_by_xpath('section/div/section/div/p[2]/textarea')
        self._webd_wrap._driver.execute_script('$(arguments[0]).val(arguments[1])', _message_field, _message)
        
    def submit_message(self):
        _submit = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_id('message-form').find_element_by_xpath('footer/input')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _submit)
        time.sleep(2)
        