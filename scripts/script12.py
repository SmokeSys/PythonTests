import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
try:
    driver.get(link)
    driver.find_element_by_css_selector(".btn").click()
    driver.switch_to_window(driver.window_handles[1])
    driver.find_element_by_css_selector("#answer").send_keys(calc(driver.find_element_by_css_selector("#input_value").text))
    driver.find_element_by_css_selector(".btn").click()


except Exception as e:
    print(e)

finally:
    input()
    driver.quit()