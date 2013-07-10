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
    '''
    classdocs
    '''
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def click_first_acp(self):
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[1]/h5/a').click()
        
    def click_follow_first_acp(self):
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[2]/a').click()
        
    def click_my_zola(self):
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()