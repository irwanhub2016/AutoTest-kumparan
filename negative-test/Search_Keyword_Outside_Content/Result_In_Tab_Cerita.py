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


class ResultInTabCerita(unittest.TestCase):
	def setUp(self):
		
		self.driver = webdriver.Chrome()
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_result_in_tab_cerita(self):
		
		driver = self.driver
		delay = 10  # seconds
		
		driver.delete_all_cookies()
		
		get_url_kumparan = "https://kumparan.com/"
		
		driver.get(get_url_kumparan)
		
		try:
			myElem = WebDriverWait(driver, delay).until(
				EC.presence_of_element_located((By.XPATH, "(.//*[@id='onesignal-popover-cancel-button'])")))
			driver.find_element_by_xpath("(.//*[@id='onesignal-popover-cancel-button'])").click()
			time.sleep(3)
			print("Page is ready!")
		except TimeoutException:
			print("Loading took too much time!")
		
		search_box = driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[1]/div/nav/div/div[1]/div[3]/div/div/div/div/div[1]/input)")
		search_box.click()
		search_box.send_keys("123xyz")
		time.sleep(5)
		
		icon_search = driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[1]/div/nav/div/div[1]/div[3]/div/div/div/div/div[2]/div/button/span/div/span/span/div/div/img)")
		icon_search.click()
		time.sleep(5)
		
		story_tab = driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div/button/span/span/span)")
		story_tab.click()
		time.sleep(5)
		
		story_note = driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]/span)")
		
		if story_note.is_displayed():
			print("Success, search results not found on story tab")
		
		else:
			print("Content that does not match the search is still displayed, it's like a bug")
	
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
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../../test-reports'), failfast=False, buffer=False,
	              catchbreak=False)