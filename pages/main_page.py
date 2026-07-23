import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.coworking_booking = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__reminders > div.home-eduV2__reminders-block > div:nth-child(1) > div.home-eduV2__reminders-coworking > div.flex.column.gap10.jcsb > div.home-eduV2__reminders-action.flex.column > div > div.list-tile__trailing")
        self.see_coworking = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__reminders > div.home-eduV2__reminders-block > div:nth-child(1) > div.flex.aic.jcsb.mb10 > div")
        self.watch_more = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__watched > div.home-eduV2__watched-segments > div > button:nth-child(2)")
        self.lesson_29 = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__watched > div.w100.hidden.relative > div > div:nth-child(1) > div.flex.grow.column.jcsb.gap5.primary-text-color.mb5 > div.flex.aic.jcsb.gap5.w100p.home-eduV2__watched-footer > div.flex.aic.gap5 > div:nth-child(2) > span")
        self.btn_profile = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar.pointer.flex.gap5")
        self.btn_exit = (By.CSS_SELECTOR, "#app > div > div.user-container > div > div > div.relative.w100p > div.flex.column.gap15.w100p.relative > div:nth-child(6) > div")
        self.btn_confirm = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")

    def click_coworking_booking(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.coworking_booking)).click()

    def click_see_coworking(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.see_coworking)).click()

    def click_watch_more(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.watch_more))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(1.5)
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.watch_more)).click()

    def click_lesson_29(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.lesson_29)).click()


    def click_btn_profile(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_profile)).click()

    def click_btn_exit(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.btn_exit))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.btn_exit)).click()

    def click_btn_confirm(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_confirm)).click()

