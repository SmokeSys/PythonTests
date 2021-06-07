import math

from selenium import webdriver

try:
    driver = webdriver.Chrome()

    driver.get("http://suninjuly.github.io/find_link_text")

    link = driver.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = driver.find_element_by_tag_name("[required]")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    

except Exception as err:
    print(f"{err}")

finally:

    input()
    driver.quit()