'''
Created on Jul 2, 2013

@author: padelstein
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from robot.libraries.BuiltIn import BuiltIn

import time

class MyZola:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def _confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        _url = self._webd_wrap._driver.current_url
        if not _url.startswith('https://zolaqc.com/profile'):
            raise AssertionError("Not on a profile page.")
        
    def click_my_zola(self):
        self._confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    def click_sign_in(self):
        ''' clicks the sign in button '''
        self._confirm_page()
        
        self._webd_wrap._driver.find_element_by_link_text("Register / Sign In").click()
        
    def click_sign_out(self):
        ''' clicks the sign out link '''
        self._confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('logout-link').click()
        
    ########################################################################
    ########################################################################
    
    def click_starred(self):
        ''' clicks the starred filter on the activities '''
        self._confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-buttonset-filterbar-3').find_element_by_xpath('ul/li[3]/a').click()
    
    ########################################################################
    ########################################################################
        
    def first_activity_should_be_purchased_book(self, _book_title):
        ''' raises AssertionError if page title is not arg1 '''
        self._confirm_page()
        
        actual = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[2]/ul/li/a[2]').text
        if actual != _book_title:
            raise AssertionError("Purchased book should have been %s but was %s" % (_book_title, actual))
    
    def first_activity_should_be_recommended_book(self, _book_title):
        ''' raises AssertionError if page title is not arg1 '''
        self._confirm_page()
        
        actual = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[2]/ul/li/a[2]').text
        if actual != _book_title:
            raise AssertionError("Recommended book should have been %s but was %s" % (_book_title, actual))
        
    def first_activity_should_be_follow(self):
        ''' raises AssertionError if first activity is not a follow '''
        self._confirm_page()
        
        actual = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[1]/h5').text
        if not "following" in actual:
            raise AssertionError("First activity should have been a follow")
        
    def first_activity_should_be_rated_book(self, _book_title):
        ''' raises AssertionError if first activity is not a rate the proper book '''
        self._confirm_page()
        
        _actual_book_title = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[2]/ul/li/a[2]').text
        _description = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[1]/h5').text
        if not "rated" in _description or _book_title != _actual_book_title:
            raise AssertionError("First activity should have been rated %s" % (_actual_book_title))
        
    def first_starred_activity_should_be_from(self, _name):
        ''' raises AssertionError if first starred activity is not from _name '''
        self._confirm_page()
        
        _actual_name = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div/h5/a[2]').text
        if not _actual_name in _name:
            raise AssertionError("First starred activity should have been from %s but was %s" % (_name, _actual_name))