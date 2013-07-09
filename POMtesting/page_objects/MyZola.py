'''
Created on Jul 2, 2013

@author: padelstein
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from robot.libraries.BuiltIn import BuiltIn

class MyZola:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def first_activity_should_be_purchased_book(self, _book_title):
        ''' raises AssertionError if page title is not arg1 '''
        actual = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[2]/ul/li/a[2]').text
        if actual != _book_title:
            raise AssertionError("Purchased book should have been %s but was %s" % (_book_title, actual))
    
    def first_activity_should_be_recommended_book(self, _book_title):
        ''' raises AssertionError if page title is not arg1 '''
        actual = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[2]/ul/li/a[2]').text
        if actual != _book_title:
            raise AssertionError("Recommended book should have been %s but was %s" % (_book_title, actual))