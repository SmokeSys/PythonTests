import unittest
from selenium import webdriver



class TestPages(unittest.TestCase):
    def testPage1(self):
        driver = webdriver.Chrome()
        driver.get("http://suninjuly.github.io/registration1.html")
        els = driver.find_elements_by_css_selector("[required]")
        for i in range(3):
            els[i].send_keys("i")
        driver.find_element_by_css_selector(".btn").click()
        che = driver.find_element_by_css_selector("h1").text
        driver.quit()
        self.assertEqual(che, "Congratulations! You have successfully registered!", "Smtg going wrong in test 1")
            
    def testPage2(self):
        driver = webdriver.Chrome()
        driver.get("http://suninjuly.github.io/registration2.html")
        els = driver.find_elements_by_css_selector("[required]")
        for i in els:
            i.send_keys("i")
        driver.find_element_by_css_selector(".btn").click()
        che = driver.find_element_by_css_selector("h1").text
        driver.quit()
        self.assertEqual(che, "Congratulations! You have successfully registered!", "Smtg going wrong in test 2")

if __name__ == "__main__": unittest.main()