'''
Created on Jul 17, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage
from page_objects.my_zola import my_zola


class my_zola_profile_picture(unittest.TestCase):
          
    def profile_picture_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in()
        page_homepage.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.click_profile_picture()
        page_my_zola.user_modal.close_modal()
        webd_wrap.check_url('https://zolaqc.com/profile/')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_profile_picture(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.profile_picture_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()