from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from locators import TestLocators


class TestsTransition:

    def test_click_on_constructor(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.ENTRY_FIELD_EMAIL_FOR_LOGIN).send_keys(data.email)
        driver.find_element(*TestLocators.ENTRY_FIELD_PASSWORD_FOR_LOGIN).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CONSTRUCTOR))

        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.PLACE_ORDER_BUTTON))

        text = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text

        assert text == 'Оформить заказ'


    def test_click_on_the_stellar_burgers_logo(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.ENTRY_FIELD_EMAIL_FOR_LOGIN).send_keys(data.email)
        driver.find_element(*TestLocators.ENTRY_FIELD_PASSWORD_FOR_LOGIN).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.STELLAR_BURGERS_LOGO))

        driver.find_element(*TestLocators.STELLAR_BURGERS_LOGO).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.PLACE_ORDER_BUTTON))

        text = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text

        assert text == 'Оформить заказ'