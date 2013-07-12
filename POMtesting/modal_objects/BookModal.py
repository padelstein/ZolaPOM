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

import time

class BookModal:

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def close_modal(self):
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
    
    ########################################################################
        
    def rate(self):
        self._webd_wrap._driver.find_element_by_xpath('/html/body/div[4]').find_element_by_class_name('ui-rating-bar-section-large').find_element_by_xpath('span/div[3]/a').click()    
        
    def click_buy(self):
        _purchase_button = self._webd_wrap._driver.find_element_by_class_name('l-230px').find_element_by_xpath('div/div/span/a')
        self._webd_wrap._driver.execute_script('$(arguments[0]).click()', _purchase_button)
        self._webd_wrap.wait.until(EC.title_contains("Zola"))
        
    def click_recommend(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]')))
        
        _recommend_button = self._webd_wrap._driver.find_element_by_class_name("l-230px").find_element_by_xpath("div/div/ul/li[3]/a")
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _recommend_button)
        
    def click_full_profile(self):
        _full_profile = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_xpath('div/footer/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _full_profile)
    
    ########################################################################
        
    def get_book_title(self):
        self._webd_wrap.wait.until(EC.title_contains("Zola"))
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]')))
        time.sleep(1)
        _elt = self._webd_wrap._driver.find_element_by_class_name("fancybox-inner").find_element_by_xpath("div/div/section[1]/div/section/div[2]/h2/a")
        print _elt.text
        return _elt.text
    
    def choose_wishlist(self):
        #self.driver.find_element_by_name(list_name).click()
        #self._driver.find_element_by_class_name("margin-bottom-20px").find_element_by_xpath("ul/li[8]/a").click()
        _element = self._webd_wrap.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/section[2]/div/div/ul/li[2]/div/div/div/div/section/ul/li/a')
        _hov = ActionChains(self._webd_wrap._driver).move_to_element(_element)
        _hov.perform()
        self._webd_wrap._driver.execute_script('(arguments[0]).click()', _element)
         #self._webd_wrap._driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/section[2]/div/div/ul/li[2]/div/div/div/div/section/ul/li[9]/a').click()

         
    def click_view_your_list(self):
        self.webd_wrap._driver.find_element_by_class_name('move-left-10px').find_element_by_xpath('li[2]/a').click()
        
        
    def click_add_to_list(self):
        add_to_list = self._webd_wrap._driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/section[2]/div/div/ul/li[2]/div/a')
        #add_to_list = self._driver.find_element_by_class_name('l-230px').find_element_by_xpath('div/div/section[2]/div/div/ul/li[2]/div/a')    
        hover = ActionChains(self._webd_wrap._driver).move_to_element(add_to_list)
        hover.perform()
        self._webd_wrap._driver.execute_script('(arguments[0]).click()', add_to_list)
    
    def click_add_to_list_nsi(self):
        add_to_list_nsi= self._webd_wrap._driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/section[2]/div/div/ul/li[2]/a')
        hover = ActionChains(self._webd_wrap._driver).move_to_element(add_to_list_nsi)
        hover.perform()
        self._webd_wrap._driver.execute_script('(arguments[0]).click()', add_to_list_nsi)
    
    