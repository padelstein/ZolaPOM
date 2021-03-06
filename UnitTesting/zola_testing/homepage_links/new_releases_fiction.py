'''
Created on Jul 16, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage

class new_releases_fiction(unittest.TestCase):
          
    def new_releases_fiction_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_fiction_new_releases_link('ROMANCE',2)
        page_homepage.click_fiction_new_releases_link('FICTION',1)
        
        webd_wrap.close_the_browser()
        
        
    
    def test_new_releases_fiction(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.new_releases_fiction_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()