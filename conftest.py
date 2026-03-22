from selenium import webdriver
from faker import Faker
import pytest
from locators import (MainPageLocators)


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(MainPageLocators.MAIN_PAGE_URL)
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture()
def fake_email():
    fake = Faker()
    return fake.email()


@pytest.fixture()
def incorrect_fake_email():
    fake = Faker()
    return fake.domain_name()


@pytest.fixture()
def fake_password():
    fake = Faker()
    return fake.password()
