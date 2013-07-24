'''
Created on Jul 23, 2013

@author: emma
'''
from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from robot.libraries.BuiltIn import BuiltIn

import time

class YourCollection:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    
    def click_all_rated(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[6]").click()
    
    def click_purchased(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[2]").click()
    
    def click_preordered(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[3]").click()
    
    def click_favorites(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[4]").click()
        
    def click_wishlist(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[5]").click()
        
    def click_not_for_me(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[7]").click()
        
    def click_private_books(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[8]").click()
        
    def click_edit_devices(self):
        self._webd_wrap._driver.find_element_by_class_name("t-center").find_element_by_xpath("a").click()
        
    def click_view_all(self):
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div/div[2]/a').click()
         
#         
#     def open_book_modal(self):