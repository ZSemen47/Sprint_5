from selenium import webdriver
import pytest
from data import Data


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.main_page_url)
    try:
        yield driver
    finally:
        driver.quit()
