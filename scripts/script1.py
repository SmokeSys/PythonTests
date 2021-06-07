import time

from selenium import webdriver


driver = webdriver.Chrome()


driver.get("https://yandex.ru/")

time.sleep(5)

textarea = driver.find_element_by_id("text")

textarea.send_keys("тензор")


suggest = driver.find_element_by_class_name("mini-suggest__popup-content")

if (suggest.is_enabled): print(1)

tempbut = driver.find_element_by_class_name("search2__button")

tempbut.click()
#proverka ssilok
time.sleep(5)
driver.quit()