from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.implicitly_wait(5)
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    driver.get(link)
    
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    driver.find_element_by_css_selector("#book").click()
    
    
    x = driver.find_element_by_css_selector("#input_value").text
    ans = driver.find_element_by_css_selector("#answer").send_keys(calc(x))
    sub = driver.find_element_by_css_selector(".form-group .btn").click()  
    


except Exception as e:
    print(e)

finally:
    input()
    driver.quit()