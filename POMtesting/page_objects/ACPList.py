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

class ACPList:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def click_my_zola(self):
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    ########################################################################
    ########################################################################
        
    def click_first_acp(self):
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[1]/h5/a').click()
        
    def click_follow_first_acp(self):
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[2]/a').click()
        
    ########################################################################
    ########################################################################
        
    def confirm_bookseller_page(self):
        bookstore_button = self._webd_wrap._driver.find_element_by_class_name("author").find_element_by_xpath("a/div/img")
        #bookstore_button = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/section/div/a/div/img")
        #note: line 79 is flaky; it is more robust than the commented out line (80) but doesn't always work
        if bookstore_button is None: raise Exception('bookstore button not found')
        element_to_hover_over =  bookstore_button
        hover = ActionChains(self._webd_wrap._driver).move_to_element(element_to_hover_over)
        hover.perform()
        self._webd_wrap._driver.execute_script('$(arguments[0]).click()', bookstore_button)