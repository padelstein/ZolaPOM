from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from UnitTesting.page_objects.modals.base_modal import base_modal

import time

class book_modal(base_modal):
    def __init__(self, webd_wrap):
        base_modal.__init__(self, webd_wrap)
    
    def _confirm_modal(self):
        ''' raises AssertionError if modal is incorrect '''
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fancybox-inner')), 'modal not present')
        
        # waits until the rating bar is present to confirm the a book modal is present
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ui-rating-bar-section-large")), 'rating bar')

        _full_profile_link = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_xpath('div/footer/a')
        
        if "full book info" not in _full_profile_link.get_attribute("innerHTML").lower():
            raise AssertionError("Not on a Book Modal.")
     
    def close_modal(self):
        self._confirm_modal()
        
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
    
        # confirms the modal is gone
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))
        
    ########################################################################
        
    def rate(self):
        ''' rates the book '''
        self._confirm_modal()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-rating-bar-section-large').find_element_by_xpath('span/div[3]/a').click()    
        
    def click_buy(self):
        ''' clicks the buy button on the book modal '''
        self._confirm_modal()
        
        _purchase_button = self._webd_wrap._driver.find_element_by_class_name('l-230px').find_element_by_xpath('div/div/span/a')
        self._webd_wrap._driver.execute_script('$(arguments[0]).click()', _purchase_button)
        self._webd_wrap.wait.until(EC.title_contains("Zola"))
        
    def click_recommend(self):
        ''' clicks the recommend button on the book modal '''
        self._confirm_modal()
        
        _recommend_button = self._webd_wrap._driver.find_element_by_class_name("l-230px").find_element_by_xpath("div/div/ul/li[3]/a")
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _recommend_button)
        
    def click_full_profile(self):
        ''' clicks the full profile button on the book modal '''
        self._confirm_modal()
        
        _full_profile = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_xpath('div/footer/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _full_profile)
        
        # confirms the modal is gone
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))
           
    def choose_wishlist(self):
        ''' once add to list dialog is displayed, chooses the wishlist '''
        self._confirm_modal()
        
        self._webd_wrap._driver.find_element_by_link_text('My Wishlist').click()
        

    def click_view_your_list(self):
        ''' clicks the view your list option after adding the book the the list '''
        self._confirm_modal()
        
        self.webd_wrap._driver.find_element_by_class_name('move-left-10px').find_element_by_xpath('li[2]/a').click()
                
    def click_add_to_list(self):
        ''' clicks the add to list button '''
        self._confirm_modal()
        
        self._webd_wrap._driver.find_element_by_link_text("ADD TO LIST").click()


    ########################################################################
        
    def get_book_title(self):
        ''' returns the title of the book '''
        self._confirm_modal()
        
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2[class='header-1 margin-bottom-10px']")))
        _elt = self._webd_wrap._driver.find_element_by_class_name("fancybox-inner").find_element_by_xpath("div/div/section[1]/div/section/div[2]/h2/a")
        return _elt.get_attribute('innerHTML')