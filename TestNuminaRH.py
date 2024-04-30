from cProfile import run
from unittest import runner
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class NuminaRH(unittest.TestCase):

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
		driver.get("https://test-rrhh.numina.mx/login")
		buscar_user = driver.find_element(By.NAME, "email")
		buscar_password = driver.find_element(By.NAME, "password")
		buscar_user.send_keys("test_rocket1999@test.com")
		buscar_password.send_keys("Revilla#99")
		submit = driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div[1]/div/form/button")
		submit.click()
		self.assertTrue(self.is_element_present(By.XPATH, "/html/body/app-root/app-admin/div/app-navbar/app-sidebar/div/div/div[3]/div/a/div/em"))
		#driver.implicitly_wait(50)

	def test_AddEmployModal(self):
		driver = self.driver
		section_employees = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-admin > div > app-navbar > app-sidebar > div > div > div:nth-child(3) > div:nth-child(2) > a > div")
		section_employees.click()
		add_employ = driver.find_element(By.XPATH, "/html/body/app-root/app-admin/div/main/app-employees/div/div/div[1]/div[2]/button[1]")
		add_employ.click()
		first_name = driver.find_element(By.NAME, "primerNombre")
		second_name = driver.find_element(By.NAME, "segundoNombre")
		lastname_p = driver.find_element(By.NAME, "apellidoPaterno")
		lastname_m = driver.find_element(By.NAME, "apellidoMaterno")
		salary = driver.find_element(By.NAME, "sueldoNeto")
		mail = driver.find_element(By.NAME, "email")
		num_employ = driver.find_element(By.NAME, "numeroDeEmpleado")
		payment_frecuency = driver.find_element(By.NAME, "frecuenciaDePago")
		first_name.send_keys("Luis")
		second_name.send_keys("Test")
		lastname_p.send_keys("Revilla")
		lastname_m.send_keys("Belmont")
		salary.send_keys("20000")
		mail.send_keys("test_selenium004@python.com")
		num_employ.send_keys("7")
		dd = Select(payment_frecuency)
		dd.select_by_value("3")
		time.sleep(2)
		create_employ = driver.find_element(By.XPATH, "/html/body/modal-container/div/div/app-create-employee-modal/div/form/div/div[5]/button")
		create_employ.click()
		time.sleep(5)
		self.assertTrue(self.is_element_present(By.CLASS_NAME, "no-results"))
		inicio = driver.find_element(By.XPATH, "/html/body/modal-container/div/div/app-create-employee-modal/div/div[2]/div/button")
		inicio.click()
		time.sleep(5)
		employ_created = driver.find_element(By.XPATH, "// td[contains(text(),\'test_selenium004@python.com')]")
		#self.assertIn(mail, driver.title)
		self.assertTrue(self.is_element_present(By.XPATH, employ_created))



	def tearDown(self):
		driver = self.driver
		cerrar = driver.find_element(By.XPATH, "/html/body/app-root/app-admin/div/app-navbar/app-sidebar/div/div/div[3]/div/a/div/em")
		cerrar.click()
		self.driver.close()
	
def suite():
	suite = unittest.TestSuite()
	suite.addTest(NuminaRH('test_Login'))
	suite.addTest(NuminaRH('test_AddEmployModal'))
	return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(suite())
	#unittest.main()