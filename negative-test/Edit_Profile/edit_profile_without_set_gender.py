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
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path  # python3 only
env_path = Path('../Edit_Profile/negative-test') / '.env'
load_dotenv(dotenv_path=env_path)

class EditProfileWithoutSetGender(unittest.TestCase):
	def setUp(self):
		
		self.driver = webdriver.Chrome()
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_edit_profile_without_set_gender(self):
		
		driver = self.driver
		
		driver.delete_all_cookies()
		
		email_gmail = os.getenv("EMAIL_GMAIL")
		password_gmail = os.getenv("PASSWORD_GMAIL")
		# auth
		get_url_kumparan = "https://kumparan.com/"
		
		get_url_gmail_auth = "https://accounts.google.com/signin/oauth/identifier?client_id=203797405389-ebvfbi965n9kis0qeg8h8mgq40fr5i7k.apps.googleusercontent.com&as=R0Bk2zEa3ll-7jEHdDB4gg&destination=https%3A%2F%2Fkumparan.com&approval_state=!ChR6MXY0ZnpyNXlRMi10M1kzSjRjSxIfQTRkWlFjUzBwTUFTOEhuU1JuY2dubW8tTVIwOGlCWQ%E2%88%99APNbktkAAAAAXEwCGN0ieJBQJ1fiHGZMNjMY-z1VSJlH&oauthgdpr=1&oauthriskyscope=1&xsrfsig=ChkAeAh8T-9mb8w4R-ZatL32ljogj900kUA4Eg5hcHByb3ZhbF9zdGF0ZRILZGVzdGluYXRpb24SBXNvYWN1Eg9vYXV0aHJpc2t5c2NvcGU&flowName=GeneralOAuthFlow"
		
		driver.get(get_url_kumparan)
		time.sleep(10)
		
		driver.get(get_url_gmail_auth)
		time.sleep(5)
		
		driver.find_element_by_xpath("(.//*[@id='identifierId'])").click()
		driver.find_element_by_xpath("(.//*[@id='identifierId'])").send_keys(email_gmail)
		time.sleep(3)
		
		driver.find_element_by_xpath("(.//*[@id='identifierNext']/content)").click()
		time.sleep(3)
		
		driver.find_element_by_xpath("(.//*[@id='password']/div[1]/div/div[1]/input)").click()
		driver.find_element_by_xpath("(.//*[@id='password']/div[1]/div/div[1]/input)").send_keys(password_gmail)
		time.sleep(5)
		
		driver.find_element_by_xpath("(.//*[@id='passwordNext']/content)").click()
		time.sleep(5)
		
		# open a new window
		driver.execute_script("window.open('http://www.kumparan.com', 'new window')")
		time.sleep(5)
		
		window_after = driver.window_handles[1]
		
		# switch on to new child window
		driver.switch_to.window(window_after)
		time.sleep(5)
		
		driver.find_element_by_xpath("(.//*[@id='login']/div/div/div[2]/div[2]/button/span/span)").click()
		time.sleep(5)
		
		print("-> Try to login gmail valid")
		
		element_gmail = driver.find_element_by_xpath("(.//*[@id='login']/div/div/div[2]/div[2]/button/span/span)")
		
		if element_gmail.is_displayed():
			print("Should the user can get session gmail and success login with gmail")
			print("It's bug")
		
		else:
			
			driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[1]/div/nav/div/div[2]/div[3]/div/div/a/span/div/span/div)").click()
			time.sleep(3)
			
			driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[3]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/a[2]/div[2]/div/div/div/span)").click()
			time.sleep(3)
			
			select_gender = driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/div[7]/div/div/div/div/div/div[1]/select)")
			select_gender.click()
			Select(select_gender).select_by_visible_text("Pilih")
			
			time.sleep(3)
			
			driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/div[11]/button/span/span)").click()
			time.sleep(3)
			
			alert_notif = driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[3]/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div/span)")
			
			if alert_notif.text == 'Perubahan berhasil di simpan':
				print("Should value Nama is mandatory (required)  or user get Notification appears 'Maaf, Terjadi galat. Perubahan anda tidak berhasil di simpan'")
				print("It's a bug.")
			
			else:
				print("Notification appears 'Perubahan berhasil di simpan', value Nama not appear in setting page and Nama field.")
			
			time.sleep(3)
			
			print("-> Edit Profile with name empty is success")
	
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