from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import keys
import time

class using_unitests()

driver = webdriver.Chrome(executable_path=r"C:\Users\ZoRo\Desktop\TestSelenium\chromedriver.exe")
driver.get("http://localhost:8000/")
login = driver.find_element(By.Xpath, "//*[@id="content"]/div/div[1]/div[2]/div/a[1]")
driver.click(button)
driver.close()