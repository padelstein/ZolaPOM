'''
Created on Jul 16, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage


class bottom_copyright_icon(unittest.TestCase):
          
    def bottom_copyright_icon_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_copyright_icon()
        page_homepage.confirm_page()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_bottom_copyright_icon(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.bottom_copyright_icon_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()