import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
try:
    driver.get(link)
    ans = int(driver.find_element_by_css_selector("#num1").text) + int(driver.find_element_by_css_selector("#num2").text)
    select = Select(driver.find_element_by_css_selector("select"))
    select.select_by_visible_text(str(ans))
    driver.find_element_by_css_selector(".btn").click()

    


except Exception as e:
    print(e)

finally:
    input()
    driver.quit()