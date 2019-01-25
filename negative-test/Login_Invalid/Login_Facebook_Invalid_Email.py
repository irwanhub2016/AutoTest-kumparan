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


class LoginFacebookInvalidEmail(unittest.TestCase):
	def setUp(self):
		
		self.driver = webdriver.Chrome()
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_login_facebook_invalid_email(self):
		
		driver = self.driver
		
		driver.delete_all_cookies()
		
		# auth
		get_url_kumparan = "https://kumparan.com/"
		
		get_url_facebook_auth = "https://www.facebook.com/login.php?skip_api_login=1&api_key=261539327577949&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fchannel%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fconnect%252Fxd_arbiter.php%253Fversion%253D43%2523cb%253Df33832e74c1146%2526domain%253Dkumparan.com%2526origin%253Dhttps%25253A%25252F%25252Fkumparan.com%25252Ff692146d5761c%2526relation%253Dopener%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fconnect%252Fxd_arbiter.php%253Fversion%253D43%2523cb%253Dfc507afa2b8a6%2526domain%253Dkumparan.com%2526origin%253Dhttps%25253A%25252F%25252Fkumparan.com%25252Ff692146d5761c%2526relation%253Dopener%2526frame%253Df5b3da4c1f42c4%26display%3Dpopup%26scope%3Demail%252Cpublic_profile%252Cuser_friends%252Cuser_location%252Cuser_birthday%26response_type%3Dtoken%252Csigned_request%26domain%3Dkumparan.com%26origin%3D1%26client_id%3D261539327577949%26ret%3Dlogin%26sdk%3Djoey%26fallback_redirect_uri%3Dhttps%253A%252F%252Fkumparan.com%252F%26logger_id%3D4c1f1de6-6580-5e46-8d0b-4ff314892b50&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter.php%3Fversion%3D43%23cb%3Dfc507afa2b8a6%26domain%3Dkumparan.com%26origin%3Dhttps%253A%252F%252Fkumparan.com%252Ff692146d5761c%26relation%3Dopener%26frame%3Df5b3da4c1f42c4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26e2e%3D%257B%257D&display=popup&locale=en_GB&logger_id=4c1f1de6-6580-5e46-8d0b-4ff314892b50"
		
		driver.get(get_url_kumparan)
		time.sleep(10)
		
		driver.get(get_url_facebook_auth)
		time.sleep(5)
		
		driver.find_element_by_id("email").click()
		driver.find_element_by_id("email").send_keys("irwansyarifudin0812812@yahoo.com")
		time.sleep(3)
		
		driver.find_element_by_id("pass").click()
		driver.find_element_by_id("pass").send_keys("xxxxxx")
		time.sleep(5)
		
		driver.find_element_by_id("loginbutton").click()
		time.sleep(5)
		
		error_box = driver.find_element_by_id("error_box")
		
		if error_box.is_displayed():
			print("The inputted email is not registered")
			note_error = driver.find_element_by_xpath("(.//*[@id='error_box']/div[1])")
			print("Notification by system : ", note_error.text)
			
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
			
			print("-> Login facebook is success")
	
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