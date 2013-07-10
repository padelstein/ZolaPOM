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

import random
import time

class SignInModal:

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        self._random_email = 'jay' + str( random.randint(0,10000000) ) + 'zolabooks.com'
    
    def click_sign_up(self):
        _sign_up_button = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_xpath('div/section[2]/div/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _sign_up_button)
        
    def sign_in(self, _username='davidtennant@zolabooks.com', _password='kingkong'): 

        self._webd_wrap._driver.execute_script('$(arguments[0]).val(arguments[1])', self._webd_wrap._driver.find_element_by_id('sign-in-modal').find_element_by_name('username'), _username)
        self._webd_wrap._driver.execute_script('$(arguments[0]).val(arguments[1])', self._webd_wrap._driver.find_element_by_id('sign-in-modal').find_element_by_name('password'), _password)

        _send = self._webd_wrap._driver.find_element_by_id("login_modal").find_element_by_xpath('div[3]/p/input')

        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _send)
        time.sleep(3) # waits for the login to register before moving on

