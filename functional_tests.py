# Use Webdriver Manager for Python: https://github.com/SergeyPirogov/webdriver_manager

# Import code:
import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# Use the `install()` method to set `executabe_path` in a new `Service` instance:
service = Service(executable_path=GeckoDriverManager().install())


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # Pass in the `Service` instance with the `service` keyword: 
        self.driver = webdriver.Firefox(service=service)
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Isaac has heard about a cool new online to-do app. She goes to check out its
        #home page
        self.driver.get('http://localhost:8000')

        #He notices its title and the header mentions to-do lists
        self.assertIn('To-Do', self.driver.title) 
        self.fail('Finish the test!')

#He is invited to enter a to-do item straight away


#He types "Buy peacock feathers" into atext box (Isaac's hobby is trying fly fishing 
# lures)


#When he hits enter, the page updates, now the page lists:
#"1: Buy peacock feathers as an item in the to-do list"


#There's still a text box onviting her to add another item. He enters
#"Use peacock feathers to make a fly"


#The page updates again and npw two items are on the list

#Isaac wonders whether thes site will reember his list. The he sees that
#the site has generated a unique URL for him --there's some explanation
#text tp that effect.


#He visits the URL - his to-do list is still there


#Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')