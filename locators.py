from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_PAGE_URL = "https://qa-desk.stand.praktikum-services.ru/"
    ENTRY_AND_REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".buttonSecondary.inButtonText.undefined.inButtonText")
    PLACE_AN_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    AVATAR_OF_THE_USER = (By.XPATH, "//button[@class='circleSmall']")
    NAME_OF_THE_USER = (By.XPATH, "//h3[@class='profileText name']")


class LoginAndRegistrationLocators():
    THERE_IS_NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
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
    TO_PLACE_AN_AD_LOG_IN = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    TITLE = (By.XPATH, "//input[@placeholder='Название']")
    PRODUCT_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
    COST = (By.XPATH, "//input[@name='price']")
    DROPDOWN_CITY_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[3]/div[1]/button")
    DROPDOWN_CITY_SPB = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[3]/div[2]/button[2]/span")
    DROPDOWN_CATEGORY_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[2]/div[2]/div[1]/button")
    DROPDOWN_CATEGORY_CAR = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[2]/div[2]/div[2]/button[1]/span")
    CONDITION_OF_PRODUCT_NEW_BUTTON = (By.XPATH, "//div[@value='Новый']")
    CONDITION_OF_PRODUCT_USED_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/form/fieldset/div/div[2]/div")
    PUBLISH_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/form/button")
    LIST_OF_ADDS = (By.XPATH, "/html/body/div/div/div[2]/div[4]/div/div[2]")
    MY_ADD = (By.CLASS_NAME, "card")
    #ADDS_LOADED = (By.CSS_SELECTOR, "profilePage_gridAndPaginaton__togPs")
    ADDS_LOADED = (By.CSS_SELECTOR, "profilePage_gridAndPaginaton__togPs")
