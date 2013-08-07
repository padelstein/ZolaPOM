'''
Created on Aug 6, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.category import category

class all_categories(unittest.TestCase):
          
    def all_categories_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        
        page_homepage.click_all_categories()
        
        page_category = category(webd_wrap)
        page_category.confirm_all_categories_page()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_all_categories(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.all_categories_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()