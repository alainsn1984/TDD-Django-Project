from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from solos.models import Solo

class StudentTesCase(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.implicitly_wait(2)
        self.solo1 = Solo.objects.create(
            instrument='saxophone',
            artist='John Coltrane',
            track='My Favorite Things'
        )
        self.solo2 = Solo.objects.create(
            instrument='saxophone',
            artist='Cannonball Adderley',
            track='All Blues'
        )
        self.solo3 = Solo.objects.create(
            instrument='saxophone',
            artist='Cannonball Adderley',
            track='Waltz for Debby'
        )
    def tearDown(self):
        self.browser.quit()
    
    def test_student_find_solos(self):
        """
        Test that a user can search for solos
        """
        
        # He knows he's in the right place because he can see
        # the name of the site in the heading.
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element(by=By.CLASS_NAME, value='navbar-brand')
        self.assertEqual('JMAD',brand_element.text)
        
        # Steve is a jazz student who would like to find more
        # examples of solos so he can improve his own
        # improvisation. He visits the home page of JMAD.
        # He sees the inputs of the search form, including
        # labels and placeholders.
        instrument_input = self.browser.find_element(by=By.CSS_SELECTOR,value='input#jmad-instrument')
        self.assertIsNotNone(self.browser.find_element(by=By.CSS_SELECTOR,value='label[for="jmad-instrument"]'))
        self.assertEqual(instrument_input.get_attribute('placeholder'),'i.e. trumpet')
        artist_input = self.browser.find_element(By.CSS_SELECTOR,value='input#jmad-artist')
        self.assertIsNotNone(self.browser.find_element(By.CSS_SELECTOR,value='label[for="jmad-artist"]'))
        self.assertEqual(artist_input.get_attribute('placeholder'),'i.e. Davis')
        # He types in the name of his instrument and submits
        # it.
        instrument_input.send_keys('saxophone')
        self.browser.find_element(by=By.CSS_SELECTOR, value='form button').click()
        # He sees too many search results...
        # ...so he adds an artist to his search query and
        search_results = self.browser.find_elements(By.CLASS_NAME, 'jmad-search-result')
        self.assertGreater(len(search_results), 2)
        # gets a more manageable list.
        second_artist_input = self.browser.find_element(By.ID, value='jmad-artist')
        second_artist_input.send_keys('Cannonball Adderley')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()
        second_search_results = self.browser.find_elements(By.CSS_SELECTOR,'.jmad-search-result a')
        self.assertEqual(len(second_search_results), 2)
        # He clicks on a search result.
        second_search_results[0].click()
        # The solo page has the title, artist and album for
        # this particular solo.
        self.assertEqual(self.browser.current_url, '{}/solos/2/'.format(self.live_server_url))
        self.assertEqual(self.browser.find_element(By.ID,'#jmad-artist').text,'Cannonball Adderley')
        self.assertEqual(self.browser.find_element(By.ID,'#jmad-track').text,'All Blues')
        self.assertEqual(self.browser.find_element(By.ID,'#jmad-album').text,'Kind of Blue')
        # He also sees the start time and end time of the solo.
        self.assertEqual(self.browser.find_element(By.ID,'#jmad-start-time').text,'2:06')
        self.assertEqual(self.browser.find_element(By.ID,'#jmad-end-time').text,'4:01')
        import pdb; pdb.set_trace()
        self.assertEqual(self.browser.current_url, '{}/solos/2/'.format(self.live_server_url))
        self.fail('Incomplete Test')