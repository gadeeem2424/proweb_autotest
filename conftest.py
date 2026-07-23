import pytest
from selenium import webdriver

@pytest.fixture
def driver_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Запуск без графического окна
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def driver_edge():
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

