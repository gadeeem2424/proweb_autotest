import pytest
from selenium import webdriver

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


