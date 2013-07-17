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

import time

class Bestsellers:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        _url = self._webd_wrap._driver.current_url
        _title = self._webd_wrap._driver.title
        if not _url.startswith('https://zolaqc.com/bestsellers') or _title != 'Zola Books | Best Sellers | Browse':
            raise AssertionError("Not on the bestsellers page.")     
        
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    ########################################################################
    ########################################################################
    
    def click_first_book(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]/div/div/a[1]').click()
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]")), 'modal not present')
        
    def click_buy_first_book(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]/div/div/div[1]/a').click()
        
    def rate_first_book(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]').find_element_by_class_name('star-rating-control').find_element_by_xpath('div[4]').click()
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'star-rating-control')), 'rating bar did not reload properly')
        
    def get_first_book_title(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'l-main-primary')))
        _book_title = self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]/div/div/a')
        return _book_title.text
        
    