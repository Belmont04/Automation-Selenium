from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdrivers.driver import Driver
from selenium.webdriver.chrome.service import Service
import time

class using_unitest(unittest.TestCase):
	def setUp(self):
		chrome_path = r"C:\Users\zorobabel\AppData\Local\Programs\Python\Python38\chromedriver.exe"
		self.driver = webdriver.Chrome(service=Service(chrome_path))
		self.driver.implicitly_wait(60)
		self.driver.maximize_window()
		self.driver_method = Driver()


	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException: return False
		return True

	def test_Login(self):
		driver = self.driver
		driver.get("https://dev.alpex.dynamicreinsurance.com/login/")
		email_input = driver.find_element(By.CSS_SELECTOR, "#\:r0\:")
		password_input = driver.find_element(By.ID, "auth-login-v2-password")
		email_input.send_keys("luis.revilla@therocketcode.com")
		password_input.send_keys("Abc12345!")
		submit = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[3]/div[5]/button")
		submit.click()
		self.assertTrue(self.is_element_present(By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[3]/div[2]/div[2]"))


	def tearDown(self):
		driver = self.driver
		cerrar = driver.find_element(By.CSS_SELECTOR, "#__next > div.layout-wrapper.css-uinsfl > div.layout-content-wrapper.MuiBox-root.css-20sk7n > header > div > div.MuiBox-root.css-102yg23 > div.actions-right.MuiBox-root.css-70qvj9 > span > div")
		cerrar.click()
		Logout = driver.find_element(By.CSS_SELECTOR, "body > div.MuiPopover-root.MuiMenu-root.MuiModal-root.css-hxcdyb > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiPaper-root.MuiMenu-paper.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-1xxcosi > ul > li")
		Logout.click()
		self.driver.close()

if __name__ == '__main__':
	unittest.main()

