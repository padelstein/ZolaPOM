'''
Created on Jul 2, 2013

@author: padelstein
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time

class ACPList:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self, _acp_type=None):
        ''' raises AssertionError if page is incorrect. takes the type of acp as arg1 '''
        
        _actual_url = self._webd_wrap._driver.current_url
        _actual_title = self._webd_wrap._driver.title
        
        if _acp_type is None:
            _url = 'https://zolaqc.com/people/'
        else:
            _url = 'https://zolaqc.com/people/' + _acp_type
            _title = 'Zola Books | ebook | ' + _acp_type.capitalize()
        
        
        if _acp_type is None:
            if not _actual_url.startswith(_url):
                raise AssertionError("Not on an ACP page")
        else:
            if _url != _actual_url  or _title != _actual_title:
                raise AssertionError("Not on the appropriate ACP list page.")  
    
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    ########################################################################
    ########################################################################
        
    def click_first_acp(self):
        ''' clicks the first acp in the main list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[1]/h5/a').click()
        
    def click_follow_first_acp(self):
        ''' clicks follow on the first acp in the main list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[2]/a').click()
        
    ########################################################################
    ########################################################################
        
    def confirm_bookseller_page(self):
        bookstore_button = self._webd_wrap._driver.find_element_by_class_name("author").find_element_by_xpath("a/div/img")
        #bookstore_button = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/section/div/a/div/img")
        #note: line 79 is flaky; it is more robust than the commented out line (80) but doesn't always work
        if bookstore_button is None: raise Exception('bookstore button not found')
        element_to_hover_over =  bookstore_button
        hover = ActionChains(self._webd_wrap._driver).move_to_element(element_to_hover_over)
        hover.perform()
        self._webd_wrap._driver.execute_script('$(arguments[0]).click()', bookstore_button)