'''
Created on Jul 17, 2013

@author: emma
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import random

class FindFriends:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self, _name=None):
        ''' raises AssertionError if page is incorrect '''
        
        _actual_url = self._webd_wrap._driver.current_url
        _actual_title = self._webd_wrap._driver.title
        
        _url = 'https://zolaqc.com/profile/people/finder'
        if _name is None:
            _title = _actual_title
        else:
            _title = 'Zola Books | ' + _name
        
        if _url != _actual_url  or _title != _actual_title:
            raise AssertionError("Not on the People Finder page.")
        
    def click_skip_this(self):
        #self._webd_wrap._driver.find_element_by_xpath("/html/body/div[3]/div/div/footer/form/a").click()
        pass
    
            
    ########################################################################
    ########################################################################