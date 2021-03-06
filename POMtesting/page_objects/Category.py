'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time

class Category:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        _url = self._webd_wrap._driver.current_url
        _title = self._webd_wrap._driver.title
        
        if not _url.startswith(self._webd_wrap._baseURL + '/category'):
            raise AssertionError("Not on a Category page.")
        
    def page_title_should_be(self, _correct_title):
        ''' raises AssertionError if page title is not arg1 '''
        
        # waits until title is arg1
        self._webd_wrap.wait.until(EC.title_is(_correct_title), "Title should have been %s but was %s" % (_correct_title, self._webd_wrap._driver.title))
        
        
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    ########################################################################
    ########################################################################

    def click_first_book(self):
        ''' clicks first book in the main list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("l-main-primary").find_element_by_xpath("section[3]/div/a/img").click()
        
    def click_second_book(self):
        ''' clicks first book in the main list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("l-main-primary").find_element_by_xpath("section[4]/div/a/img").click()

    ########################################################################
    ########################################################################
    
    def confirm_all_categories_page(self):
        
        self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'header-category-1'), 'ALL'), 'not on the all categories page')
        
    def confirm_children_page(self):
        
        self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'header-category-1'), 'CHILDREN'), 'not on the children categories page')
        
    def confirm_ya_page(self):
        
        self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'header-category-1'), 'YOUNG'), 'not on the young adult categories page')
        