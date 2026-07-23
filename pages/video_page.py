import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class VideoPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_play = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button > span")
        self.btn_fullscreen = (By.CSS_SELECTOR,"#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3) > span")
        # self.screen = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__actinview")
        self.btn_pause = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button > span")
        self.btn_collapse = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3) > span")
        self.star_5 = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div.videolesson__general-footer-rating.mt10 > div > div > div > div > span:nth-child(5)")
        self.btn_send = (By.CSS_SELECTOR, "#dialog > div > div > div > div > div > button")
        self.btn_leave = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(1) > button")
        self.logo_home = (By.CSS_SELECTOR, "#app > div > div.header > nav > div.header__logo > div > a")





    def click_btn_play(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_play)).click()

    def click_btn_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()

    # def click_screen(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.screen)).click()

    def click_btn_pause(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_pause)).click()

    def click_btn_collapse(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_collapse)).click()

    def click_star_5(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.star_5))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(2)
        wait.until(EC.element_to_be_clickable(self.star_5)).click()

    def click_btn_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_send)).click()

    def click_btn_leave(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.btn_leave))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.btn_leave)).click()

    def click_logo_home(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.logo_home)).click()

    def is_video_paused(self):
        try:
            return self.driver.execute_script(
                "let v = document.querySelector('video'); return v ? v.paused : null;"
            )
        except Exception:
            return None

    def resume_if_paused(self):
        if self.is_video_paused():
            self.click_btn_play()
