'''
Created on Jul 29, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.category import category

class dropdown_parenting(unittest.TestCase):
          
    def dropdown_parenting_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.hover_over_category_dropdown()
        page_homepage.click_on_link("Parenting & Family")
        
        page_category = category(webd_wrap)
        page_category.page_title_should_be("Parenting & Family")
        
        
        webd_wrap.close_the_browser()
        
        
    
    def test_dropdown_parenting(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.dropdown_parenting_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()