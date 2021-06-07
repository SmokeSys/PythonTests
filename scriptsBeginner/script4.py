import math

from selenium import webdriver

try:
    
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_css_selector("input[type=\"text\"]")
    for element in elements:
        element.send_keys("Мой ответ")
    
    button = browser.find_element_by_xpath("//form/div[@style]//button[text()=\"Submit\"]")
    #button = browser.find_element_by_css_selector("button.btn")
    button.click()
    

except Exception as err:
    print(f"{err}")

finally:

    input()
    browser.quit()