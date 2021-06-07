import time

import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    driver.get("http://suninjuly.github.io/get_attribute.html")
    elpic = driver.find_element_by_css_selector("#treasure")
    valx = elpic.get_attribute("valuex")
    ans = driver.find_element_by_css_selector("#answer").send_keys(calc(valx))
    chb = driver.find_element_by_css_selector("#robotCheckbox").click()
    rb = driver.find_element_by_css_selector("#robotsRule").click()
    sub = driver.find_element_by_css_selector(".btn").click()   


except Exception as e:
    print(e)

finally:
    input()
    driver.quit()