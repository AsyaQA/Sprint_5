from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators


class TestsConstructor:

    def test_go_to_the_filling_section(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.FILLING_SECTION))

        driver.find_element(*TestLocators.FILLING_SECTION).click()

        element = driver.find_element(*TestLocators.FILLING_SECTION_PARENT).get_attribute("class")

        assert 'tab_tab_type_current' in element


    def test_go_to_the_sauces_section(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.SAUCES_SECTION))

        driver.find_element(*TestLocators.SAUCES_SECTION).click()

        element = driver.find_element(*TestLocators.SAUCES_SECTION_PARENT).get_attribute("class")

        assert 'tab_tab_type_current' in element


    def test_go_to_the_buns_section(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.BUNS_SECTION))

        element = driver.find_element(*TestLocators.BUNS_SECTION_PARENT).get_attribute("class")

        assert 'tab_tab_type_current' in element
