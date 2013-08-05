'''
Created on Jul 15, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.sign_up import sign_up
from page_objects.homepage import homepage
from page_objects.add_card import add_card
from page_objects.my_zola import my_zola
from page_objects.bestsellers import bestsellers
from page_objects.book import book

class test_rating_signedin(unittest.TestCase):
          
    def rating_signedin_profile_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.click_sign_up()
         
        page_sign_up = sign_up(webd_wrap)
        email = page_sign_up.submit_new_member_info()
        
        page_sign_up.click_skip_this()
        page_homepage.click_sign_out()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in(email, 'password')
        page_homepage.click_bestsellers()
        
        page_bestsellers = bestsellers(webd_wrap)
        book_title = page_bestsellers.book_modal.get_book_title()
        page_bestsellers.book_modal.click_full_profile()
        
        page_book = book(webd_wrap)
        page_book.rate()
        page_book.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.first_activity_should_be_rated_book(book_title)
    
        webd_wrap.close_the_browser()
    
    def test_rating_signedin_profile(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.rating_signedin_profile_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()