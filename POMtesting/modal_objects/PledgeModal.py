'''
Created on Jul 10, 2013

@author: emma
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from robot.libraries.BuiltIn import BuiltIn

class PledgeModal:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
    
    def detect_modal_element(self):
        self._webd_wrap._driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/div/section[2]/div/section[2]/div/div[2]/div/div/a")
        return self
   
    def modal_should_be_present(self):
        ''' raises AssertionError if modal is not displayed '''
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "l-570px")))
        return self
    
    def click_signup_button(self):
        signup_button = self._webd_wrap._driver.find_element_by_id('sign-in-modal').find_element_by_xpath('section[2]/div/a')
        hover = ActionChains(self._webd_wrap._driver).move_to_element(signup_button)
        hover.perform()
        self._webd_wrap._driver.execute_script('(arguments[0]).click()', signup_button)
        return self
    
    
    def initial_pledge(self):
        pledge_button = self._webd_wrap._driver.find_element_by_class_name("l-710px").find_element_by_xpath("section/p/a/img")
        if pledge_button is None: raise Exception('pledge button not found')
        element_to_hover_over =  pledge_button
        hover = ActionChains(self._webd_wrap._driver).move_to_element(element_to_hover_over)
        hover.perform()
        self._webd_wrap._driver.execute_script('(arguments[0]).click()', pledge_button)
    
    def pledge_confirm(self):
        #self._driver.find_element_by_class_name("margin-left-250px").find_element_by_xpath("p/label")
        pledge_button2 = self._webd_wrap._driver.find_element_by_class_name("l-modal-800px").find_element_by_xpath("section[2]/a/img")
        if pledge_button2 is None: raise Exception('pledge button not found')
        element_to_hover_over =  pledge_button2
        hover = ActionChains(self._webd_wrap._driver).move_to_element(element_to_hover_over)
        hover.perform()
        self._webd_wrap._driver.execute_script('(arguments[0]).click()', pledge_button2)
        
    
    def initial_unpledge(self):
        pledge_button = self._webd_wrap._driver.find_element_by_class_name("l-710px").find_element_by_xpath("section/div[2]/a/img")
        if pledge_button is None: raise Exception('pledge button not found')
        element_to_hover_over =  pledge_button
        hover = ActionChains(self._webd_wrap._driver).move_to_element(element_to_hover_over)
        hover.perform()
        self._webd_wrap._driver.execute_script('(arguments[0]).click()', pledge_button)
        
    def unpledge_confirm(self):
        self._webd_wrap._driver.find_element_by_class_name("l-modal-800px").find_element_by_xpath("section[2]/a[2]")
        pledge_button2 = self._webd_wrap._driver.find_element_by_class_name("l-modal-800px").find_element_by_xpath("section[2]/a/input")
        if pledge_button2 is None: raise Exception('pledge button not found')
        element_to_hover_over =  pledge_button2
        hover = ActionChains(self._webd_wrap._driver).move_to_element(element_to_hover_over)
        hover.perform()
        self._webd_wrap._driver.execute_script('(arguments[0]).click()', pledge_button2)
        