import time
import os

from selenium import webdriver


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
try:
    driver.get(link)
    els = driver.find_elements_by_css_selector("[required]")
    for i in range(3):
        els[i].send_keys("i")
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'temp.txt')           
    els[3].send_keys(file_path)
    driver.find_element_by_css_selector(".btn").click()
    
    


except Exception as e:
    print(e)

finally:
    input()
    driver.quit()