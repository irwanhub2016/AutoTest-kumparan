from selenium import webdriver
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


class LoginGmailInvalidEmail(unittest.TestCase):
	def setUp(self):
		
		self.driver = webdriver.Chrome()
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_login_gmail_invalid_email(self):
		
		driver = self.driver
		
		driver.delete_all_cookies()
		
		# auth
		get_url_kumparan = "https://kumparan.com/"
		
		get_url_gmail_auth = "https://accounts.google.com/signin/oauth/identifier?client_id=203797405389-ebvfbi965n9kis0qeg8h8mgq40fr5i7k.apps.googleusercontent.com&as=R0Bk2zEa3ll-7jEHdDB4gg&destination=https%3A%2F%2Fkumparan.com&approval_state=!ChR6MXY0ZnpyNXlRMi10M1kzSjRjSxIfQTRkWlFjUzBwTUFTOEhuU1JuY2dubW8tTVIwOGlCWQ%E2%88%99APNbktkAAAAAXEwCGN0ieJBQJ1fiHGZMNjMY-z1VSJlH&oauthgdpr=1&oauthriskyscope=1&xsrfsig=ChkAeAh8T-9mb8w4R-ZatL32ljogj900kUA4Eg5hcHByb3ZhbF9zdGF0ZRILZGVzdGluYXRpb24SBXNvYWN1Eg9vYXV0aHJpc2t5c2NvcGU&flowName=GeneralOAuthFlow"
		
		driver.get(get_url_kumparan)
		time.sleep(10)
		
		driver.get(get_url_gmail_auth)
		time.sleep(5)
		
		driver.find_element_by_xpath("(.//*[@id='identifierId'])").click()
		driver.find_element_by_xpath("(.//*[@id='identifierId'])").send_keys("irwansyarifud1299910@gmail.com")
		time.sleep(3)
		
		driver.find_element_by_xpath("(.//*[@id='identifierNext']/content)").click()
		time.sleep(3)
		
		error_box = driver.find_element_by_xpath(
			"(.//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[2]/div[2]/div)")
		
		if error_box.is_displayed():
			print("The inputted email is not registered")
			print("Notification by system : ", error_box.text)
			print("-> Login gmail invalid email is success")
		
		else:
			
			driver.find_element_by_xpath("(.//*[@id='password']/div[1]/div/div[1]/input)").click()
			driver.find_element_by_xpath("(.//*[@id='password']/div[1]/div/div[1]/input)").send_keys("xxx122017")
			time.sleep(5)
			
			driver.find_element_by_xpath("(.//*[@id='passwordNext']/content)").click()
			time.sleep(5)
			
			password_error = driver.find_element_by_xpath("(.//*[@id='password']/div[2]/div[2]/div)")
			
			if password_error.is_displayed():
				print("The inputted password is wrong")
				print("Notification by system : ", error_box.text)
				print("-> Login gmail invalid password is success")
			
			else:
				
				# open a new window
				driver.execute_script("window.open('http://www.kumparan.com', 'new window')")
				time.sleep(5)
				
				window_after = driver.window_handles[1]
				
				# switch on to new child window
				driver.switch_to.window(window_after)
				time.sleep(5)
				
				driver.find_element_by_xpath("(.//*[@id='login']/div/div/div[2]/div[2]/button/span/span)").click()
				time.sleep(5)
				
				print("-> Login gmail valid is success")
	
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