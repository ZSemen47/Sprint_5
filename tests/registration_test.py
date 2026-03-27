import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import (RegistrationOfAccount, EmailGeneration)
from locators import (MainPageLocators, LoginAndRegistrationLocators)


class TestRegistration():

    def test_registration_of_the_user(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON))
        RegistrationOfAccount.register_account(driver, EmailGeneration.fake_email(), EmailGeneration.fake_password())
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        expected_result = True
        actual_result_1 = driver.find_element(*MainPageLocators.AVATAR_OF_THE_USER).is_displayed()
        actual_result_2 = driver.find_element(*MainPageLocators.NAME_OF_THE_USER).is_displayed()
        assert expected_result == actual_result_1
        assert expected_result == actual_result_2


    def test_user_registration_email_differs_from_the_mask(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON))
        RegistrationOfAccount.an_account_with_an_incorrect_email(driver, EmailGeneration.incorrect_fake_email())
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginAndRegistrationLocators.EMAIL_ALREADY_EXISTS_ERROR_TEXT))
        expected_result = True
        actual_result_1 = driver.find_element(*LoginAndRegistrationLocators.EMAIL_ALREADY_EXISTS_ERROR_TEXT).is_displayed()
        actual_result_2 = driver.find_element(*LoginAndRegistrationLocators.EMAIL_HIGHLIGHTED_IN_RED).is_displayed()
        actual_result_3 = driver.find_element(*LoginAndRegistrationLocators.PASSWORD_HIGHLIGHTED_IN_RED).is_displayed()
        actual_result_4 = driver.find_element(*LoginAndRegistrationLocators.REPEAT_PASSWORD_HIGHLIGHTED_IN_RED).is_displayed()
        assert expected_result == actual_result_1
        assert expected_result == actual_result_2
        assert expected_result == actual_result_3
        assert expected_result == actual_result_4

    def test_registration_existing_user(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON))
        driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginAndRegistrationLocators.THERE_IS_NO_ACCOUNT_BUTTON).click()
        existing_email = EmailGeneration.fake_email()
        existing_password = EmailGeneration.fake_password()
        RegistrationOfAccount.an_account_with_existing_email(driver, existing_email, existing_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()
        time.sleep(3)
        driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(LoginAndRegistrationLocators.THERE_IS_NO_ACCOUNT_BUTTON))
        driver.find_element(*LoginAndRegistrationLocators.THERE_IS_NO_ACCOUNT_BUTTON).click()
        RegistrationOfAccount.an_account_with_existing_email(driver, existing_email, existing_password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            LoginAndRegistrationLocators.EMAIL_ALREADY_EXISTS_ERROR_TEXT))
        expected_result = True
        actual_result_1 = driver.find_element(*LoginAndRegistrationLocators.EMAIL_ALREADY_EXISTS_ERROR_TEXT).is_displayed()
        actual_result_2 = driver.find_element(*LoginAndRegistrationLocators.EMAIL_HIGHLIGHTED_IN_RED).is_displayed()
        actual_result_3 = driver.find_element(*LoginAndRegistrationLocators.PASSWORD_HIGHLIGHTED_IN_RED).is_displayed()
        actual_result_4 = driver.find_element(*LoginAndRegistrationLocators.REPEAT_PASSWORD_HIGHLIGHTED_IN_RED).is_displayed()
        assert expected_result == actual_result_1
        assert expected_result == actual_result_2
        assert expected_result == actual_result_3
        assert expected_result == actual_result_4
