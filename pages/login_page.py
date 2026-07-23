from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait_for_write


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.language_ru = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-bot-langs > div:nth-child(1)")
        self.login = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center > div > label > input")
        self.btn_enter = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button")
        self.password = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center.log-in__newContent-right-block-center-checkpass > div.log-in__newContent-right-block-center-inp > label > input")
        self.btn_login = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button")
        self.device_1 = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2)")
        self.confirm_1 = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div.drop-down-component__content > div.sessions__item-content > button")

    def change_language_ru(self):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.element_to_be_clickable(self.language_ru))
        self.driver.execute_script("arguments[0].click();", element)

    def enter_login(self, login):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login)).send_keys(login)

    def click_btn_enter(self):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.element_to_be_clickable(self.btn_enter))
        self.driver.execute_script("arguments[0].click();", element)

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.password)).send_keys(password)

    def click_btn_login(self):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.element_to_be_clickable(self.btn_login))
        self.driver.execute_script("arguments[0].click();", element)

    def click_device_1(self):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.element_to_be_clickable(self.device_1))
        self.driver.execute_script("arguments[0].click();", element)

    def click_confirm_1(self):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.element_to_be_clickable(self.confirm_1))
        self.driver.execute_script("arguments[0].click();", element)