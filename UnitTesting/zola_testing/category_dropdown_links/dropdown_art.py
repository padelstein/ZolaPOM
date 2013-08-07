'''
Created on Jul 29, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.category import category

class dropdown_art(unittest.TestCase):
          
    def dropdown_art_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.hover_over_category_dropdown()
        page_homepage.click_on_link("Art, Architecture, & Design")
        
        page_category = category(webd_wrap)
        page_category.page_title_should_be("Zola Books | ebook | Art, Architecture, & Design")
        
        
        webd_wrap.close_the_browser()
        
        
    
    def test_dropdown_art(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.dropdown_art_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()