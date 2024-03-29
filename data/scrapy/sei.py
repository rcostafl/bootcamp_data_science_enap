# -*- coding: utf-8 -*-
import datetime
import os
import re
from selenium import webdriver

login = os.environ.get('LOGIN') or 'usuario'
passowrd = os.environ.get('PASSWORD') or 'senha'

url = 'https://sei.fazenda.gov.br/'
driver = webdriver.Firefox()
driver.get(url)
input_login = driver.find_element_by_xpath('//input[@id="txtUsuario"]')
input_login.send_keys(login)
input_senha = driver.find_element_by_xpath('//input[@id="pwdSenha"]')
input_senha.send_keys(passowrd)
option = driver.find_element_by_xpath('//option[@value="0"]')
option.click()
button_acessar = driver.find_element_by_xpath('//button[@id="sbmLogin"]')
button_acessar.click()
print(driver)
driver.close()

