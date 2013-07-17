'''
Created on Jul 10, 2013

@author: emma
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains


from robot.libraries.BuiltIn import BuiltIn


class BooksellerModal:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def close_modal(self):
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
        
    ########################################################################    
    
    def detect_modal_element(self):
        self._webd_wrap._driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/div/section[2]/div/section[2]/div/div[2]/div/div/a")
        return self
   
    def modal_should_be_present(self):
        ''' raises AssertionError if modal is not displayed '''
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "l-570px")), 'modal not present')
        return self
    
    def click_full_profile(self):
        full_profile = self._webd_wrap._driver.find_element_by_class_name('name-header').find_element_by_xpath('div/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", full_profile)
        