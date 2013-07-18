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
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, "web-purchase")), 'Purchase Confirm Modal not present.')
        
        _receive_emails = self._webd_wrap._driver.find_element_by_id('receive_author_emails')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _receive_emails)
        
    def click_buy(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, "web-purchase")), 'Purchase Confirm Modal not present.')
        
        _buy_button = self._webd_wrap._driver.find_element_by_class_name("l-modal-section-content").find_element_by_xpath("footer/a")
        #_buy_button.click()
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _buy_button)
        
    def click_done(self):
        #_elt = self._webd_wrap._driver.find_element_by_class_name('l-modal-section-content').find_element_by_xpath('section/div/div[1]/div')
        
        #self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html/div[4]/div/div/div/div/div[1]/div/footer/a'), 'Done'), 'Purchase Confirm Modal not present.')
        
        time.sleep(5)
       
        _elt = self._webd_wrap._driver.find_element_by_id('sign-in-modal').find_element_by_xpath('footer/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _elt)
        
        time.sleep(3)