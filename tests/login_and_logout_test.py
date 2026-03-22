import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v145.fed_cm import open_url
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
import pytest
from helpers import RegistrationOfAccount
from locators import (MainPageLocators, LoginAndRegistrationLocators, PlaceAnAddLocators)


class TestLogin():

    def test_login_user(self, driver, fake_email, fake_password):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON))
        driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginAndRegistrationLocators.THERE_IS_NO_ACCOUNT_BUTTON).click()
        existing_email = fake_email
        existing_password = fake_password
        driver.find_element(*LoginAndRegistrationLocators.ENTER_EMAIL).send_keys(existing_email)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.REPEAT_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()
        time.sleep(3)
        driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginAndRegistrationLocators.ENTER_BUTTON))
        driver.find_element(*LoginAndRegistrationLocators.ENTER_EMAIL).send_keys(existing_email)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        assert driver.find_element(*MainPageLocators.AVATAR_OF_THE_USER).is_displayed()
        assert driver.find_element(*MainPageLocators.NAME_OF_THE_USER).is_displayed()


class TestLogout():
    def test_logout_user(self, driver, fake_email, fake_password):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON)).click()
        driver.find_element(*LoginAndRegistrationLocators.THERE_IS_NO_ACCOUNT_BUTTON).click()
        existing_email = fake_email
        existing_password = fake_password
        driver.find_element(*LoginAndRegistrationLocators.ENTER_EMAIL).send_keys(existing_email)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.REPEAT_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginAndRegistrationLocators.POPUP_LOGIN))
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LoginAndRegistrationLocators.ENTER_EMAIL)).send_keys(existing_email)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).is_displayed()
