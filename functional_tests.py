# Use Webdriver Manager for Python: https://github.com/SergeyPirogov/webdriver_manager

# Import code:
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# Use the `install()` method to set `executabe_path` in a new `Service` instance:
service = Service(executable_path=GeckoDriverManager().install())

# Pass in the `Service` instance with the `service` keyword: 
driver = webdriver.Firefox(service=service)
driver.get('http://localhost:8000')

assert 'Congratulations' in driver.title