from selenium.webdriver.common.by import By


class MainPageLocators():
    ENTRY_AND_REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".buttonSecondary.inButtonText.undefined.inButtonText")
    PLACE_AN_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    AVATAR_OF_THE_USER = (By.XPATH, "//button[@class='circleSmall']")
    NAME_OF_THE_USER = (By.XPATH, "//h3[@class='profileText name']")


class LoginAndRegistrationLocators():
    THERE_IS_NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and contains(text(), 'Нет аккаунта')]")
    ENTER_EMAIL = (By.XPATH, "//input[@name='email']")
    ENTER_PASSWORD = (By.XPATH, "//input[@name='password']")
    REPEAT_PASSWORD = (By.XPATH, "//input[@name='submitPassword']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_ALREADY_EXISTS_ERROR_TEXT = (By.XPATH, "//span[text()='Ошибка']")
    EMAIL_HIGHLIGHTED_IN_RED = (By.XPATH, "//div[@class='input_inputError__fLUP9']//input[@name='email']")
    PASSWORD_HIGHLIGHTED_IN_RED = (By.XPATH, "//div[@class='input_inputError__fLUP9']//input[@name='password']")
    REPEAT_PASSWORD_HIGHLIGHTED_IN_RED = (By.XPATH,
                                          "//div[@class='input_inputError__fLUP9']//input[@name='submitPassword']")
    ALREADY_HAVE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Уже есть аккаунт']")
    POPUP_LOGIN = (By.XPATH, "//form[@class='popUp_shell__LuyqR']")


class PlaceAnAddLocators():
    TO_PLACE_AN_AD_LOG_IN = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    TITLE = (By.XPATH, "//input[@placeholder='Название']")
    PRODUCT_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
    COST = (By.XPATH, "//input[@name='price']")
    DROPDOWN_CITY_BUTTON = (By.XPATH, "//input[@name='city']/..//button[contains(@class, 'arrowDown')]")
    DROPDOWN_CITY_SPB = (By.XPATH, "//span[contains(@class, 'dropDownMenu') and contains(text(), 'Санкт-Петербург')]")
    DROPDOWN_CATEGORY_BUTTON = (By.XPATH, "//input[@name='category']/..//button[contains(@class, 'arrowDown')]")
    DROPDOWN_CATEGORY_BUTTON_LIST = (By.XPATH, "//div[contains(@class, 'dropDownMenu_options')]")
    DROPDOWN_CATEGORY_CAR = (By.XPATH, "//span[contains(@class, 'dropDown') and text()='Авто']")
    CONDITION_OF_PRODUCT_NEW_BUTTON = (By.XPATH, "//label[text()='Новый']/preceding-sibling::div[contains(@class, 'radioUnput_inputActive')]")
    CONDITION_OF_PRODUCT_USED_BUTTON = (By.XPATH, "//div[contains(@class, 'radioUnput_shell')]//label[text()='Б/У']/preceding-sibling::div[contains(@class, 'radioUnput_inputRegular')]")
    PUBLISH_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'buttonPrimary') and text()='Опубликовать']")
    LIST_OF_ADDS = (By.XPATH, "//h2[text()='Первое объявление ']")
    MY_ADD = (By.CLASS_NAME, "card")
    ADDS_LOADED = (By.CSS_SELECTOR, "profilePage_gridAndPaginaton__togPs")
