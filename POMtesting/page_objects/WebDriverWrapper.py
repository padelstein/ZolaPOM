'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

class WebDriverWrapper:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
#         self._authURL = 'https://zola_stage:zola123@wuyou.divergence.zolaqc.com'
#         self._baseURL = 'https://wuyou.divergence.zolaqc.com'

        self._authURL = 'https://zola_stage:zola123@zolaqc.com'
        self._baseURL = 'https://zolaqc.com'

    def open_firefox(self):
        self._driver = webdriver.Firefox()
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)
        self.wait = WebDriverWait(self._driver, 20)
        self._driver.get(self._authURL)
        self._driver.get(self._baseURL)
        
    def open_chrome(self):
        self._driver = webdriver.Chrome('/Library/Python/2.7/site-packages/chromedriver')
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)
        self.wait = WebDriverWait(self._driver, 20)
        self._driver.get(self._authURL)
        # chrome doesn't like going straight into the test from the authorization url so we have to reload with the normal url
        self._driver.get(self._baseURL)
        
    def go_to_zola(self):
        self._driver.get(self._authURL)
    
    def open_page(self, path):
        self._driver.get(self._baseURL + path)
        
    def check_url(self, _url):
        ''' raises AssertionError if page is incorrect '''
        _actual_url = self._driver.current_url
        if _url != _actual_url:
            raise AssertionError("Not on correct page.")
        
    def close_the_browser(self):
        self._driver.quit()
        
    def switch_window(self):
        windows = self._driver.window_handles
        window = windows[1]
        self._driver.switch_to_window(window)
