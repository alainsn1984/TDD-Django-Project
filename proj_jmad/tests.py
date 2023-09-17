from django.test import LiveServerTestCase
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class StudentTesCase(LiveServerTestCase):
    
    def setUp(self):
        self.browser =  webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.browser.implicitly_wait(2)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_student_find_solos(self):
        """
        Test that a user can search for solos
        """
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element(By.CLASS_NAME, 'navbar-brand')
        
        #brand_element = self.browser.find_element(By.CSS_SELECTOR,'.navbar-brand')
        self.assertEqual('JMAD',brand_element.text)
        self.fail('Incomplete Test')
        
        # Steve is a jazz student who would like to find more
        # examples of solos so he can improve his own
        # improvisation. He visits the home page of JMAD.
        # He knows he's in the right place because he can see
        # the name of the site in the heading.
        # He sees the inputs of the search form, including
        # labels and placeholders.
        # He types in the name of his instrument and submits
        # it.
        # He sees too many search results...
        # ...so he adds an artist to his search query and
        # gets a more manageable list.
        # He clicks on a search result.
        # The solo page has the title, artist and album for
        # this particular solo.
        # He also sees the start time and end time of the
        # solo.