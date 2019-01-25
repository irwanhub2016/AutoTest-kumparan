from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import unittest, time, re, datetime
import HtmlTestRunner
import progressbar
import random
import xmlrunner
import os
from time import sleep


class SeeNewsDetail(unittest.TestCase):
	def setUp(self):
		
		
		self.driver = webdriver.Chrome()
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_see_news_detail(self):
		
		driver = self.driver
		delay = 5  # seconds
		
		driver.delete_all_cookies()
		
		get_url_kumparan = "https://kumparan.com/"
		
		driver.get(get_url_kumparan)
		
		try:
			myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "(.//*[@id='onesignal-popover-cancel-button'])")))
			driver.find_element_by_xpath("(.//*[@id='onesignal-popover-cancel-button'])").click()
			time.sleep(3)
			print("Page is ready!")
		except TimeoutException:
			print("Loading took too much time!")
		else:
			print("See news detail")
		
		driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div/a/div[1]/div/span)").click()
		
		print("-> See news detail is success")
		
		time.sleep(3)
	
	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e:
			return False
		return True
	
	def is_alert_present(self):
		try:
			self.driver.switch_to_alert()
		except NoAlertPresentException as e:
			return False
		return True
	
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally:
			self.accept_next_alert = True
	
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../test-reports'), failfast=False, buffer=False,
	              catchbreak=False)