from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app
import test_login
import pytest

test_login.test_login(app)

#Нажимаем на кнопку добавления видео
app.find_element_by_partial_link_text("Add movie").click()

#Определяем обязательные поля и заполняем
er = app.find_elements_by_css_selector("input[class$='error']")
i = 0
while i < len(er):
    er[i].send_keys('12345')
    i +=1

#Заполняем еще пару полей
app.find_element_by_name('duration').send_keys('30')
app.find_element_by_name('aka').send_keys('Проверяем добавляется ли')
app.find_element_by_xpath("//input[@value='Save']").click()


