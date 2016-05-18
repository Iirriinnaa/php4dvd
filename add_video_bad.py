from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/php4dvd")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("submit").click()

#Нажимаем на кнопку добавления видео
driver.find_element_by_partial_link_text("Add movie").click()

#Определяем обязательные поля, кроме последнего, и заполняем
er = driver.find_elements_by_css_selector("input[class$='error']")
i = 0
while i < len(er)-1:
    er[i].send_keys('12345')
    i +=1

#Заполняем еще пару полей
driver.find_element_by_name('duration').send_keys('30')
driver.find_element_by_name('aka').send_keys('Проверяем добавляется ли')
driver.find_element_by_xpath("//input[@value='Save']").click()
