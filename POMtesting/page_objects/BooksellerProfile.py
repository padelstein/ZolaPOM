'''
Created on Jul 10, 2013

@author: emma
'''


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time

class BooksellerProfile:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect. Does this by checking for the pledge element. '''
        
        _actual_url = self._webd_wrap._driver.current_url
        _url = self._webd_wrap._baseURL + '/profile'
        
        # this should really check for the pledge webelement but there isn't a good way of identifying it yet
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, 'page')))
        
        if not _actual_url.startswith(_url):
            raise AssertionError("Not on a Booksellers profile page.")    
    
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()    
        
    ########################################################################
    ########################################################################    
        
    def click_pledge(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div/div/section/p/a/img').click()    
        
    def click_unpledge(self):
        self.confirm_page()
        
        self._webd_wrap._driver.refresh()
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div/div/section/div/a').click()

