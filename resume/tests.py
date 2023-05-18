from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_log_in(self):
		self.browser.get('http://localhost:8000/')
		self.browser.find_element_by_id('login')

	def tearDown(self):
		self.browser.quit()
