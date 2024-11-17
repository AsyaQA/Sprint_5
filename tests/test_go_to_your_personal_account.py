from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from locators import TestLocators


class TestsPersonalAccount:

    def test_go_to_your_personal_account(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.ENTRY_FIELD_EMAIL_FOR_LOGIN).send_keys(data.email)
        driver.find_element(*TestLocators.ENTRY_FIELD_PASSWORD_FOR_LOGIN).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.SAVE_BUTTON))

        text = driver.find_element(*TestLocators.LINE_OF_TEXT).text

        assert text == 'В этом разделе вы можете изменить свои персональные данные'