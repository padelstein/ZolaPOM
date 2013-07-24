'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time

class PurchaseConfirmModal:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def _confirm_modal(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, "web-purchase")), 'Purchase Confirm Modal not present.')
    
    def close_modal(self):
        self._confirm_modal()
        
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
        
    ########################################################################
        
    def click_receive_emails(self):
        self._confirm_modal()
        
        _receive_emails = self._webd_wrap._driver.find_element_by_id('receive_author_emails')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _receive_emails)
        time.sleep(1)
        
    def click_buy(self):
        self._confirm_modal()
        
        _buy_button = self._webd_wrap._driver.find_element_by_class_name("l-modal-section-content").find_element_by_xpath("footer/a[1]")
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _buy_button)
        time.sleep(1)
        
    def click_done(self):
        time.sleep(5)
       
        _elt = self._webd_wrap._driver.find_element_by_id('sign-in-modal').find_element_by_xpath('footer/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _elt)