'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from robot.libraries.BuiltIn import BuiltIn

class AddCard:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    ########################################################################
    ########################################################################
        
    def submit_new_cc_info(self):
        self.enter_cc_number()
        self.click_cc_month_dropdown()
        self.click_cc_year_dropdown()
        self.enter_cc_adress()
        self.click_state_dropdown()
        self.enter_zip()
        self.click_cc_submit()
        
    def enter_cc_number(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("card_number").send_keys("378282246310005")
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("security_code").send_keys("266")
        
    def click_cc_month_dropdown(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("dk_container_pp_cc_exp_month").find_element_by_xpath("a").click()
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_link_text("08").click()
        
    def click_cc_year_dropdown(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("dk_container_pp_cc_exp_year").find_element_by_xpath("a").click()
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_link_text("2015").click()
            
    def enter_cc_adress(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("pp_address_1").send_keys("221B Baker Street")
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("pp_city").send_keys("London")
        
    def click_state_dropdown(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("dk_container_pp_state").find_element_by_xpath("a").click()
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_link_text("CA").click()
    
    def enter_zip(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("pp_zip").send_keys("07751")
        
    def click_cc_submit(self):
        self._webd_wrap._driver.find_element_by_name("save_billing_info").click()

    
    