'''
Created on Jul 22, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.my_ebooks import my_ebooks
from UnitTesting.page_objects.your_collection import your_collection

class top_preordered(unittest.TestCase):
          
    def top_preordered_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in()
        page_homepage.click_my_ebooks()
        
        page_my_ebooks = my_ebooks(webd_wrap)
        page_my_ebooks.click_preordered()
        
        page_your_collection = your_collection(webd_wrap)
        page_your_collection.confirm_filter_selected('preordered')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_top_preordered(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.top_preordered_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()