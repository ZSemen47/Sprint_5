import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v145.fed_cm import open_url
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
import pytest
from helpers import (RegistrationOfAccount, EmailGeneration)
from locators import (MainPageLocators, LoginAndRegistrationLocators, PlaceAnAddLocators)


class TestLogin():

    def test_login_user(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON))
        existing_email = EmailGeneration.fake_email()
        existing_password = EmailGeneration.fake_password()
        RegistrationOfAccount.register_account(driver, existing_email, existing_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(MainPageLocators.EXIT_BUTTON))
        driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginAndRegistrationLocators.ENTER_BUTTON))
        driver.find_element(*LoginAndRegistrationLocators.ENTER_EMAIL).send_keys(existing_email)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(LoginAndRegistrationLocators.ENTER_BUTTON))
        expected_result = True
        actual_result_1 = driver.find_element(*MainPageLocators.AVATAR_OF_THE_USER).is_displayed()
        actual_result_2 = driver.find_element(*MainPageLocators.NAME_OF_THE_USER).is_displayed()
        assert expected_result == actual_result_1
        assert expected_result == actual_result_2


class TestLogout():
    def test_logout_user(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON)).click()
        driver.find_element(*LoginAndRegistrationLocators.THERE_IS_NO_ACCOUNT_BUTTON).click()
        existing_email = EmailGeneration.fake_email()
        existing_password = EmailGeneration.fake_password()
        driver.find_element(*LoginAndRegistrationLocators.ENTER_EMAIL).send_keys(existing_email)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.REPEAT_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(MainPageLocators.EXIT_BUTTON))
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginAndRegistrationLocators.POPUP_LOGIN))
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LoginAndRegistrationLocators.ENTER_EMAIL)).send_keys(existing_email)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()
        expected_result = True
        actual_result = driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).is_displayed()
        assert expected_result == actual_result
