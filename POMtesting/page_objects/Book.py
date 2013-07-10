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

import time

class Book:
    '''
    classdocs
    '''
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def rate(self):
        self._webd_wrap._driver.find_element_by_class_name('ui-rating-bar').find_element_by_xpath('a/div/form/span/div[3]').click()
        
    def click_buy(self):
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/span/a').click()
        
    def click_add_to_list(self):
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/ul/li[2]/a').click()
        
    def click_recommend(self):
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/ul/li[3]/a').click()
        
    def click_my_zola(self):
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()

    
    