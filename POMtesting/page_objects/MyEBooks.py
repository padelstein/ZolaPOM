'''
Created on Jul 2, 2013

@author: padelstein
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

import time
from robot.libraries.BuiltIn import BuiltIn

class MyEBooks:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def click_my_zola(self):
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        _url = self._webd_wrap._driver.current_url
        _title = self.webd_wrap._driver.title
        if not _url.startswith('https://zolaqc.com/collection'):
            raise AssertionError("Not on a Category page.")
        
    def page_title_should_be(self, _correct_title):
        ''' raises AssertionError if page title is not arg1 '''
        actual = self._webd_wrap._driver.title
        if actual != _correct_title:
            raise AssertionError("Title should have been %s but was %s" % (_correct_title, actual))
        
    ########################################################################
    ########################################################################
