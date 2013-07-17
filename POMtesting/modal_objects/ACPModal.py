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

class ACPModal:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def close_modal(self):
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
        
    ######################################################################## 
        
    def click_follow(self):
        _follow_button = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_xpath('div/div/section[1]/section[2]/section/ul/li[1]/a')
        self._webd_wrap._driver.execute_script('$(arguments[0]).click()', _follow_button)
        self._webd_wrap.wait.until(EC.title_contains("Zola"))
        
    def click_full_profile(self):
        _full_profile = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_xpath('div/div/footer/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _full_profile)

    ########################################################################

    def get_name(self):
        self._webd_wrap.wait.until(EC.title_contains("Zola"))
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]')), 'modal not present')
        _elt = self._webd_wrap._driver.find_element_by_class_name("fancybox-inner").find_element_by_class_name('name-header').find_element_by_xpath("div/a")
        print _elt.text
        return _elt.text
    
    