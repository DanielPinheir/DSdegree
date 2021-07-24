# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCetipdados():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cetipdados(self):
    self.driver.get("http://estatisticas.cetip.com.br/astec/series_v05/paginas/lum_web_v05_template_informacoes_di.asp?str_Modulo=completo&int_Idioma=1&int_Titulo=6&int_NivelBD=2")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.NAME, "DT_DIA_DE").click()
    self.driver.find_element(By.NAME, "DT_DIA_DE").send_keys("01")
    self.driver.find_element(By.NAME, "DT_MES_DE").click()
    self.driver.find_element(By.CSS_SELECTOR, ".large-2:nth-child(2)").click()
    self.driver.find_element(By.NAME, "DT_MES_DE").send_keys("05")
    self.driver.find_element(By.NAME, "DT_ANO_DE").click()
    self.driver.find_element(By.NAME, "DT_ANO_DE").send_keys("2020")
    self.driver.find_element(By.NAME, "DT_DIA_ATE").click()
    self.driver.find_element(By.CSS_SELECTOR, ".large-2:nth-child(4)").click()
    self.driver.find_element(By.NAME, "DT_DIA_ATE").send_keys("31")
    self.driver.find_element(By.NAME, "DT_MES_ATE").click()
    self.driver.find_element(By.CSS_SELECTOR, ".large-8 > .row").click()
    self.driver.find_element(By.NAME, "DT_MES_ATE").send_keys("06")
    self.driver.find_element(By.NAME, "DT_ANO_ATE").click()
    self.driver.find_element(By.CSS_SELECTOR, ".large-8 > .row").click()
    self.driver.find_element(By.NAME, "DT_ANO_ATE").send_keys("2020")
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(2)").click()
    assert self.driver.switch_to.alert.text == "Para os meses: Abr, Jun, Set, Nov\n\nDia deve ser entre 1 e 30."
    self.driver.find_element(By.NAME, "DT_DIA_ATE").click()
    self.driver.find_element(By.NAME, "DT_DIA_ATE").send_keys("30")
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(2)").click()
  
