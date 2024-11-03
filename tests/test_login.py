from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from locators import TestLocators


class TestsLogin:

    def test_login_using_the_login_to_your_account_button_on_the_main_page(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_TO_ACCOUNT))

        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.ENTRY_FIELD_EMAIL_FOR_LOGIN).send_keys(data.email)
        driver.find_element(*TestLocators.ENTRY_FIELD_PASSWORD_FOR_LOGIN).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        text = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text

        assert text == 'Оформить заказ'


    def test_login_using_the_personal_account_button(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.ENTRY_FIELD_EMAIL_FOR_LOGIN).send_keys(data.email)
        driver.find_element(*TestLocators.ENTRY_FIELD_PASSWORD_FOR_LOGIN).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        text = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text

        assert text == 'Оформить заказ'


    def test_login_using_the_button_in_the_registration_form(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_TO_ACCOUNT))

        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.REGISTRATION_LINK))

        driver.find_element(*TestLocators.REGISTRATION_LINK).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.ENTRY_FIELD_EMAIL_FOR_LOGIN).send_keys(data.email)
        driver.find_element(*TestLocators.ENTRY_FIELD_PASSWORD_FOR_LOGIN).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        text = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text

        assert text == 'Оформить заказ'


    def test_login_using_the_button_in_the_password_recovery_form(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_TO_ACCOUNT))

        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_TO_RESET_PASSWORD))

        driver.find_element(*TestLocators.LINK_TO_RESET_PASSWORD).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.ENTRY_FIELD_EMAIL_FOR_LOGIN).send_keys(data.email)
        driver.find_element(*TestLocators.ENTRY_FIELD_PASSWORD_FOR_LOGIN).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        text = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text

        assert text == 'Оформить заказ'
