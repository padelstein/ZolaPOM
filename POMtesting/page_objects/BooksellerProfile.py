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

class BooksellerProfile:
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def click_my_zola(self):
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()    
        
    ########################################################################
    ########################################################################    
        
    def click_pledge(self):
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div/div/section/p/a/img').click()    
        
    def click_unpledge(self):
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div/div/section/div/a').click()
    
<<<<<<< HEAD
   
=======
    def click_my_zola(self):
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
>>>>>>> 98f713de049d992e461a8e69ff9dc10da918ac24
