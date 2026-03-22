import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
import pytest
from locators import (MainPageLocators, LoginAndRegistrationLocators, PlaceAnAddLocators)


class RegistrationOfAccount():
    @staticmethod
    def register_account(driver, fake_email, fake_password):
        driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginAndRegistrationLocators.THERE_IS_NO_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginAndRegistrationLocators.ENTER_EMAIL).send_keys(fake_email)
        password = fake_password
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(password)
        driver.find_element(*LoginAndRegistrationLocators.REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*LoginAndRegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

    @staticmethod
    def an_account_with_an_incorrect_email(driver, incorrect_fake_email):
        driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginAndRegistrationLocators.THERE_IS_NO_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginAndRegistrationLocators.ENTER_EMAIL).send_keys(incorrect_fake_email)
        driver.find_element(*LoginAndRegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

    @staticmethod
    def an_account_with_existing_email(driver, existing_email, existing_password):
        driver.find_element(*LoginAndRegistrationLocators.ENTER_EMAIL).send_keys(existing_email)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.REPEAT_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
