'''
Created on Jul 15, 2013

@author: emma
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from UnitTesting.page_objects.base_page_object import base_page_object

import time

class book(base_page_object):
    
    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
       
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'purchase-button')), 'Not on Book Profile page')
       
        _url = self._webd_wrap._driver.current_url
        
        if not _url.startswith(self._webd_wrap._baseURL + '/book'):
            raise AssertionError("Not on a Book Profile page.")
    
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()   
    
    ########################################################################
    ########################################################################
        
    def rate(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-rating-bar-section-large').find_element_by_xpath('span/div[3]/a').click()
        # make sure the rating bar reloads before moving on
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-rating-bar-section-large')), 'rating bar not present')
        
    def click_buy(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/span/a').click()
        
    def click_add_to_list(self):
        self.confirm_page()
        self._webd_wrap._driver.find_element_by_link_text("ADD TO LIST").click()

        
    def click_recommend(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/ul/li[3]/a').click()
        
    def choose_wishlist(self):
        time.sleep(1)
        
        self._webd_wrap._driver.find_element_by_link_text('My Wishlist').click()