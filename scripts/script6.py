import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
try:
    driver.get("http://suninjuly.github.io/math.html")
    time.sleep(2)
    xel = driver.find_element_by_css_selector("#input_value")   
    ans = driver.find_element_by_css_selector("#answer")
    y = str(math.log(abs(12*math.sin(int(xel.text)))))
    ans.send_keys(y)
    chb = driver.find_element_by_css_selector("#robotCheckbox").click()
    rb = driver.find_element_by_css_selector("#robotsRule").click()
    sub = driver.find_element_by_css_selector(".btn").click()

except Exception as e:
    print(e)

finally:
    input()
    driver.quit()