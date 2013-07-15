'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
from robot.libraries.BuiltIn import BuiltIn

class Home:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def click_my_zola(self):
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    def click_sign_in(self):
        ''' clicks the sign in button '''
        self._webd_wrap._driver.find_element_by_link_text("Register / Sign In").click()
        
    def click_sign_out(self):
        ''' clicks the sign out link '''
        self._webd_wrap._driver.find_element_by_id('logout-link').click()
        
    def click_my_ebooks(self):
        ''' clicks the my ebooks link '''
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('ul/li[1]/a').click()
        
    ########################################################################
    ########################################################################

    def hover_over_category_dropdown(self):
        ''' hovers the mouse over the category drop down menu '''
        _element = self._webd_wrap._driver.find_element_by_id("h-shop-by-category").find_element_by_xpath("h2/a")
        _hov = ActionChains(self._webd_wrap._driver).move_to_element(_element)
        _hov.perform()
        
    def hover_over_connect_dropdown(self):
        ''' hovers the mouse over the connect drop down menu '''
        _element = self._webd_wrap._driver.find_element_by_id("h-connect").find_element_by_xpath("h2/a")
        _hov = ActionChains(self._webd_wrap._driver).move_to_element(_element)
        _hov.perform()
        
    def click_bestsellers(self):
        ''' clicks the link to the bestsellers list '''
        self._webd_wrap._driver.find_element_by_id('h-header').find_element_by_xpath('div/nav/ul/li[3]/a').click()    
        
    def click_on_link(self, _link_text):
        ''' clicks on a link with arg1 as the link text '''
        self._webd_wrap._driver.find_element_by_link_text(_link_text).click()
        WebDriverWait(self._webd_wrap._driver, 10).until(EC.title_contains("Zola"))
        
    def click_first_bestseller(self):
        ''' clicks the first item in the bestseller list '''
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, 'best-sellers')))
        _bestseller = self._webd_wrap._driver.find_element_by_id('best-sellers').find_element_by_xpath('ul/li/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _bestseller)
        
    def click_category(self, _category):
        self._webd_wrap._driver.find_element_by_id('s-browse-by-category').find_element_by_link_text(_category).click()
        
    