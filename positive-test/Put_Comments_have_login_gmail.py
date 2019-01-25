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
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path  # python3 only
env_path = Path('../positive-test') / '.env'
load_dotenv(dotenv_path=env_path)

class PutCommentHaveLoginGmail(unittest.TestCase):
	def setUp(self):
		
		self.driver = webdriver.Chrome()
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_put_comment_have_login_gmail(self):
		
		driver = self.driver
		delay = 10  # seconds
		
		driver.delete_all_cookies()
		
		email_gmail = os.getenv("EMAIL_GMAIL")
		password_gmail = os.getenv("PASSWORD_GMAIL")
		
		# url_site
		get_url_kumparan = "https://kumparan.com/"
		
		# auth
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
		
		try:
			myElem = WebDriverWait(driver, delay).until(
				EC.presence_of_element_located((By.XPATH, "(.//*[@id='onesignal-popover-cancel-button'])")))
			driver.find_element_by_xpath("(.//*[@id='onesignal-popover-cancel-button'])").click()
			time.sleep(3)
			print("Page is ready!")
		
		except TimeoutException:
			print("Pop Over doesn't exist")
		
		else:
			print("See news detail")
			
			time.sleep(5)
			
			driver.find_element_by_xpath(
				"(.//*[@id='content']/div/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div/a/div[1]/div/span)").click()
			
			print("-> Try to see news detail")
			time.sleep(8)
			
			driver.find_element_by_xpath(
				"(.//*[@id='content']/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div)").click()
			time.sleep(3)
			
			driver.find_element_by_xpath(
				"(.//*[@id='content']/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div)").click()
			time.sleep(3)
			
			driver.find_element_by_xpath(
				"(.//*[@id='content']/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div)").send_keys(
				"berita ini bagus")
			time.sleep(5)
			
			driver.find_element_by_xpath(
				"(.//*[@id='content']/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/a)").click()
			time.sleep(5)
			
			print("-> Try to put comment have login gmail")
			
			comment = driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/span/span)")
			print("The comment is : ", comment.text)
			
			time.sleep(5)

			if comment.text == "":
				print("Ups, comment is empty")

			else:
				print("Put comment is success")
				
			try:
				
				modal_login = driver.find_element_by_xpath("(.//*[@id='content']/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/button/span/span)")
				
				if modal_login.is_displayed():
					modal_login.click()
					time.sleep(3)
					
					if modal_login.is_displayed():
						print("It's bug")
					
					else:
						element_validation = driver.find_element_by_xpath("(.//*[@id='login']/div/div/div[2]/div[1]/button/span/span)")
						time.sleep(3)
						
						if element_validation:
							print("Page have not session account of gmail")
						
						else:
							print("Page have session account of gmail")
							
				else:
					print("You have a session")
	
			except:
				pass
			
			else:
				print("You have a session")
			
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