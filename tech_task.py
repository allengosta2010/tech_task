import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


data = ['https://s3.eu-central-1.amazonaws.com/qa-web-test-task/{x}.html'.format(x=x) for x in range(1, 10000)]


class TestMainPage():

    @pytest.mark.parametrize("sites", data)
    def test_one(self, browser, sites):
        browser.get(sites)
        time.sleep(10)
        lnk = browser.find_element(By.TAG_NAME, "a")
        lnk.click()