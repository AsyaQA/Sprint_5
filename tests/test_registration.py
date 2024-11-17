from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import helpers
from locators import TestLocators



class TestsRegistration:

    def test_successful_registration(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_TO_ACCOUNT))

        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.REGISTRATION_LINK))

        driver.find_element(*TestLocators.REGISTRATION_LINK).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ENTRY_FIELD_NAME))

        driver.find_element(*TestLocators.ENTRY_FIELD_NAME).send_keys(helpers.random_name())
        driver.find_element(*TestLocators.ENTRY_FIELD_EMAIL).send_keys(helpers.random_email())
        driver.find_element(*TestLocators.ENTRY_FIELD_PASSWORD).send_keys(helpers.random_password())
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        text = driver.find_element(*TestLocators.LOGIN_BUTTON).text

        assert text == 'Войти'


    def test_error_for_invalid_password(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGIN_TO_ACCOUNT))

        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.REGISTRATION_LINK))

        driver.find_element(*TestLocators.REGISTRATION_LINK).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ENTRY_FIELD_NAME))

        driver.find_element(*TestLocators.ENTRY_FIELD_NAME).send_keys(helpers.random_name())
        driver.find_element(*TestLocators.ENTRY_FIELD_EMAIL).send_keys(helpers.random_email())
        driver.find_element(*TestLocators.ENTRY_FIELD_PASSWORD).send_keys(helpers.random_password_invalid())
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        text = driver.find_element(*TestLocators.PASSWORD_ERROR).text

        assert text == 'Некорректный пароль'
