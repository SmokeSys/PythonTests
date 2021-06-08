import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..\n")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..\n")
    browser.quit()