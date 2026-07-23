import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class CoworkingPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkbox_confirm = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.coworking__page-dialog-rules-check > label > button")
        self.btn_next = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.oybek_2 = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.coworking__page-dialog-follow-branch > div:nth-child(2) > div.list-tile.coworking__page-dialog-follow-branch-item-list")
        self.oybek_3 = (By.CSS_SELECTOR, "#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div:nth-child(1) > div.list-tile__trailing > button > span")
        self.btn_select1 = (By.CSS_SELECTOR, "#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.date_2 = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.coworking__page-dialog-follow-date > div > div:nth-child(4) > button")
        self.group = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.list-tile.coworking__page-dialog-follow-list")
        self.qa = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div")
        self.btn_select2 = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.time = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.coworking__page-dialog-follow-timeseat > div:nth-child(1) > label")
        self.input_h = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-container > div.material-dialog__window-body > div > label:nth-child(1)")
        self.input_m = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-container > div.material-dialog__window-body > div > label:nth-child(2)")
        self.btn_select3 = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.place = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.coworking__page-dialog-follow-timeseat > div:nth-child(2) > div")
        self.pc_11 = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div.md3-list > div:nth-child(10)")
        self.btn_select4 = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.btn_book = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.btn_cancel = (By.CSS_SELECTOR, "#app > div > div.coworking > div > div.lazyscroll > div > div:nth-child(1) > div.flex.w100p.gap10.jcsb.aic > div > button.material-icon-button.baseavatar.baseavatar-error.baseavatar-small.baseavatar_close")
        self.yes_confirm = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.btn_home = (By.CSS_SELECTOR, "#app > div > div.layout > div > div > div.desktop-navigation__icons > ul > li:nth-child(1)")


    def click_checkbox_confirm(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.checkbox_confirm)).click()

    def click_btn_next(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_next)).click()

    def click_oybek_2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.oybek_2)).click()

    def click_oybek_3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.oybek_3)).click()

    def click_btn_select1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_select1)).click()

    def click_date_2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.date_2)).click()

    def click_group(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.group))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.group)).click()

    def click_qa(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.qa)).click()

    def click_btn_select2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_select2)).click()

    def click_time(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.time))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.time)).click()

    def enter_input_h(self, hour):
        wait = WebDriverWait(self.driver, 10)
        field = wait.until(EC.element_to_be_clickable(self.input_h))
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(str(hour))

    def enter_input_m(self, minute):
        wait = WebDriverWait(self.driver, 10)
        field = wait.until(EC.element_to_be_clickable(self.input_m))
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(str(minute))

    def click_btn_select3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_select3)).click()

    def click_place(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.place)).click()

    def click_pc_11(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.pc_11))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable(self.pc_11)).click()

    def click_btn_select4(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_select4)).click()

    def click_btn_book(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_book)).click()

    def click_btn_cancel(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_cancel)).click()


    def click_yes_confirm(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.yes_confirm)).click()

    def click_btn_home(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_home)).click()



