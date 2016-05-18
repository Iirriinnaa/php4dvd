from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost/php4dvd")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("submit").click()

#Выбираем первое видео и переходим на его страницу
driver.implicitly_wait(10)
driver.find_elements_by_xpath("//*[@class='movie_box']/div[2]")[0].click()

#Нажимаем кнопку удаления и соглашаемся с алертом
driver.implicitly_wait(10)
driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
alert = driver.switch_to_alert()
alert.accept()
