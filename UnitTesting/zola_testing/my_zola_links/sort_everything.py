'''
Created on Jul 17, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.my_zola import my_zola

class my_zola_sort_everything(unittest.TestCase):
          
    def sort_everything_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in()
        page_homepage.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.sort_everything()
        page_my_zola.confirm_page()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_sort_everything(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.sort_everything_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()