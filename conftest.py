import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    option = webdriver.ChromeOptions()
    option.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=option)
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()