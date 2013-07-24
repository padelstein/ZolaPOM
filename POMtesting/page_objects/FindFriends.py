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
        
    def confirm_page(self):
        pass
        
    def click_skip_this(self):
        #self._webd_wrap._driver.find_element_by_xpath("/html/body/div[3]/div/div/footer/form/a").click()
        pass
    
            
    ########################################################################
    ########################################################################