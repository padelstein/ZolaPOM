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
    
    def click_first_book(self):
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]/div/div/a[1]').click()
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]")))
        
    def click_buy_first_book(self):
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]/div/div/div[1]/a').click()
        
    def get_first_book_title(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'l-main-primary')))
        _book_title = self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]/div/a[1]')
        return _book_title.text
        
    def click_my_zola(self):
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()