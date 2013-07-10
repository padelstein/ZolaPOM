'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from robot.libraries.BuiltIn import BuiltIn

class Category:
    '''
    classdocs
    '''
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')

    def click_first_book(self):
        ''' clicks first book in the main list '''
        self._webd_wrap._driver.find_element_by_class_name("l-main-primary").find_element_by_xpath("section[3]/div/a/img").click()
        
    def page_title_should_be(self, _correct_title):
        ''' raises AssertionError if page title is not arg1 '''
        actual = self._webd_wrap._driver.title
        if actual != _correct_title:
            raise AssertionError("Title should have been %s but was %s" % (_correct_title, actual))
    