#driver.execute_script("return arguments[0].scrollIntoView(true);", button)
import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
try:
    driver.get(link)
    x = driver.find_element_by_css_selector("#input_value").text
    driver.execute_script("window.scrollBy(0, 100);")
    ans = driver.find_element_by_css_selector("#answer").send_keys(calc(x))
    chb = driver.find_element_by_css_selector("#robotCheckbox").click()
    rb = driver.find_element_by_css_selector("#robotsRule").click()
    sub = driver.find_element_by_css_selector(".btn").click()  


    


except Exception as e:
    print(e)

finally:
    input()
    driver.quit()