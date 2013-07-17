'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

import time

from robot.libraries.BuiltIn import BuiltIn

class PurchaseConfirmModal:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def close_modal(self):
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
        
    ########################################################################
        
    def click_receive_emails(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]")), 'Purchase Confirm Modal not present.')
        
        _receive_emails = self._webd_wrap._driver.find_element_by_id('receive_author_emails')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _receive_emails)
        time.sleep(2)
        
    def click_buy(self):
        _buy_button = self._webd_wrap._driver.find_element_by_class_name("l-modal-section-content").find_element_by_xpath("footer/a[1]")
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _buy_button)
        
    def click_done(self):
        self._webd_wrap.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]")), 'modal not present')
        
        time.sleep(3)
       
        _elt = self._webd_wrap._driver.find_element_by_id('sign-in-modal').find_element_by_xpath('footer/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _elt)