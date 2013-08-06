'''
Created on Jun 18, 2013

@author: jsflax
'''
from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
import random


class webdriver_wrapper():

    ################################################
    ##############GLOBAL VARIABLES##################
    ################################################
    
    _browsers = ["chrome", "firefox"]
    #_browsers = ["safari"]
    _authUrl = 'https://zola_stage:zola123@zolaqc.com'
    _baseUrl = 'https://zolaqc.com'
    
    #r2 = str( random.randint(0,1000000) )
    
    ################################################
    #####################SETUP######################
    ################################################
    
    def open_chrome(self):
        self._driver = webdriver.Chrome('/Library/Python/2.7/site-packages/chromedriver')
        self._driver.implicitly_wait(10)
        self.wait = WebDriverWait(self._driver, 10)
        
    def open_firefox(self):
        self._driver = webdriver.Firefox()
        self._driver.implicitly_wait(10)
        self.wait = WebDriverWait(self._driver, 10)
        
    def open_safari(self):
        self._driver = webdriver.Remote(desired_capabilities={'browserName':'safari'})
        self._driver.implicitly_wait(10)
        self.wait = WebDriverWait(self._driver, 10)
        
    def open_ie(self):
        self._driver = webdriver.Ie()
        self._driver.implicitly_wait(10)
        self.wait = WebDriverWait(self._driver, 10)
        
    def __init__(self, arg):
        self.rand_username_int = str( random.randint(0,1000000) )
        if (arg == "chrome"):
            self.open_chrome()
        elif (arg == "safari"):
            self.open_safari()
        elif (arg == "firefox"):
            self.open_firefox()
        else:
            pass
        self._driver.get(self._authUrl)
        self._driver.implicitly_wait(40)
       
    def open_firefox(self):
        self._driver = webdriver.Firefox()
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)
        self.wait = WebDriverWait(self._driver, 15)
        self._driver.get(self._authUrl)
        
    def open_chrome(self):
        self._driver = webdriver.Chrome('/Library/Python/2.7/site-packages/chromedriver')
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)
        self.wait = WebDriverWait(self._driver, 15)
        self._driver.get(self._authUrl)
        self._driver.get(self._baseUrl)
        
    def go_to_zola(self):
        self._driver.get(self._authUrl)
    
    def open_page(self, path):
        self._driver.get(self._baseUrl + path)
        
    def check_url(self, url):
        ''' raises AssertionError if page is incorrect '''
        _url = self._driver.current_url
        _title = self._driver.title
        if not _url.startswith(url):
            raise AssertionError("Not on correct page.")
        
    def close_the_browser(self):
        self._driver.quit()
        
        
    def switch_window(self):
        windows = self._driver.window_handles
        window = windows[1]
        self._driver.switch_to_window(window)
    
    
    
    
