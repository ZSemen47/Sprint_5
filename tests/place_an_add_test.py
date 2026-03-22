import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import (MainPageLocators, LoginAndRegistrationLocators, PlaceAnAddLocators)

class TestPlaceAdd():
    def test_for_creating_ad_please_login(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_AN_AD_BUTTON))
        driver.find_element(*MainPageLocators.PLACE_AN_AD_BUTTON).click()
        assert driver.find_element(*PlaceAnAddLocators.TO_PLACE_AN_AD_LOG_IN).is_displayed()

    def test_creating_an_ad_by_an_authorized_user(self, driver, fake_email, fake_password):
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
        #ни WebdriverWait ни driver.implicitly_wait не помог, пришлось прибегнуть к ...
        time.sleep(3)
        driver.find_element(*MainPageLocators.ENTRY_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginAndRegistrationLocators.ENTER_BUTTON))
        driver.find_element(*LoginAndRegistrationLocators.ENTER_EMAIL).send_keys(existing_email)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_PASSWORD).send_keys(existing_password)
        driver.find_element(*LoginAndRegistrationLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.AVATAR_OF_THE_USER))
        driver.find_element(*MainPageLocators.PLACE_AN_AD_BUTTON).click()
        driver.find_element(*PlaceAnAddLocators.TITLE).send_keys(Data.title)
        driver.find_element(*PlaceAnAddLocators.PRODUCT_DESCRIPTION).send_keys(Data.description)
        driver.find_element(*PlaceAnAddLocators.COST).send_keys(Data.cost)
        driver.find_element(*PlaceAnAddLocators.DROPDOWN_CATEGORY_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PlaceAnAddLocators.DROPDOWN_CATEGORY_CAR))
        driver.find_element(*PlaceAnAddLocators.DROPDOWN_CATEGORY_CAR).click()
        driver.find_element(*PlaceAnAddLocators.DROPDOWN_CITY_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PlaceAnAddLocators.DROPDOWN_CITY_SPB))
        driver.find_element(*PlaceAnAddLocators.DROPDOWN_CITY_SPB).click()
        driver.find_element(*PlaceAnAddLocators.CONDITION_OF_PRODUCT_USED_BUTTON).click()
        driver.find_element(*PlaceAnAddLocators.PUBLISH_BUTTON).click()
        # ни WebdriverWait ни driver.implicitly_wait не помог, пришлось прибегнуть к ...
        time.sleep(3)
        driver.find_element(*MainPageLocators.AVATAR_OF_THE_USER).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(PlaceAnAddLocators.MY_ADD))
        expected_result = True
        actual_result = driver.find_element(*PlaceAnAddLocators.MY_ADD).is_displayed()
        assert expected_result == actual_result



