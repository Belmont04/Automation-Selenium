from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class using_unitest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\zorobabel\AppData\Local\Programs\Python\Python38\chromedriver.exe")
		self.driver.implicitly_wait(60)
		self.driver.maximize_window()

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException: return False
		return True

	def test_Login(self):
		driver = self.driver
		driver.get("https://dev.alpex.dynamicreinsurance.com/login/")
		buscar_user = driver.find_element(By.NAME, "email")
		buscar_password = driver.find_element(By.NAME, "password")
		buscar_user.send_keys("luis.revilla@therocketcode.com")
		buscar_password.send_keys("Abc12345!")
		submit = driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div[1]/div/form/button")
		submit.click()
		self.assertTrue(self.is_element_present(By.XPATH, "/html/body/app-root/app-admin/div/app-navbar/app-sidebar/div/div/div[3]/div/a/div/em"))
        #go to perfil screen


	def tearDown(self):
		driver = self.driver
		cerrar = driver.find_element(By.XPATH, "/html/body/app-root/app-admin/div/app-navbar/app-sidebar/div/div/div[3]/div/a/div/em")
		cerrar.click()
		self.driver.close()

if __name__ == '__main__':
	unittest.main()

