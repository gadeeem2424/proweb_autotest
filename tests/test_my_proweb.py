import time
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.video_page import VideoPage
from pages.coworking_page import CoworkingPage

def test_my_proweb_chrome(driver_chrome):
    driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    login_page = LoginPage(driver_chrome)
    login_page.change_language_ru()
    time.sleep(3)
    login_page.enter_login('998503018868')
    time.sleep(3)
    login_page.click_btn_enter()
    time.sleep(3)
    login_page.enter_password('hohol_08')
    time.sleep(3)
    login_page.click_btn_login()
    time.sleep(5)
    try:
        login_page.click_device_1()
        time.sleep(5)
        login_page.click_confirm_1()
        time.sleep(5)
    except (TimeoutException, NoSuchElementException):
        pass

    main_page = MainPage(driver_chrome)
    main_page.click_coworking_booking()
    time.sleep(5)

    coworking_page = CoworkingPage(driver_chrome)
    coworking_page.click_checkbox_confirm()
    time.sleep(5)
    coworking_page.click_btn_next()
    time.sleep(3)
    coworking_page.click_oybek_2()
    time.sleep(3)
    coworking_page.click_oybek_3()
    time.sleep(3)
    coworking_page.click_btn_select1()
    time.sleep(3)
    coworking_page.click_date_2()
    time.sleep(3)
    coworking_page.click_group()
    time.sleep(3)
    coworking_page.click_qa()
    time.sleep(3)
    coworking_page.click_btn_select2()
    time.sleep(3)
    coworking_page.click_time()
    time.sleep(3)
    coworking_page.enter_input_h(14)
    time.sleep(3)
    coworking_page.enter_input_m(40)
    time.sleep(3)
    coworking_page.click_btn_select3()
    time.sleep(3)
    coworking_page.click_place()
    time.sleep(3)
    coworking_page.click_pc_11()
    time.sleep(3)
    coworking_page.click_btn_select4()
    time.sleep(3)
    coworking_page.click_btn_book()
    time.sleep(3)

    main_page.click_see_coworking()
    time.sleep(3)

    coworking_page.click_btn_cancel()
    time.sleep(3)
    coworking_page.click_yes_confirm()
    time.sleep(3)
    coworking_page.click_btn_home()
    time.sleep(3)

    main_page.click_watch_more()
    time.sleep(3)
    main_page.click_lesson_29()
    time.sleep(3)

    video_page = VideoPage(driver_chrome)
    video_page.click_btn_play()
    time.sleep(2)
    video_page.click_btn_fullscreen()
    time.sleep(15)
    video_page.resume_if_paused()
    time.sleep(15)
    # video_page.click_screen()
    # time.sleep(3)
    video_page.click_btn_pause()
    time.sleep(3)
    video_page.click_btn_collapse()
    time.sleep(3)
    try:
        video_page.click_star_5()
        time.sleep(3)
        video_page.click_btn_send()
        time.sleep(3)
    except (TimeoutException, NoSuchElementException,
        ElementClickInterceptedException, ElementNotInteractableException):
        pass

    video_page.click_btn_leave()
    time.sleep(3)
    video_page.click_logo_home()
    time.sleep(3)

    main_page.click_btn_profile()
    time.sleep(4)
    main_page.click_btn_exit()
    time.sleep(4)
    main_page.click_btn_confirm()
    time.sleep(4)

def test_invalid_my_proweb_chrome(driver_chrome):
    driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    login_page = LoginPage(driver_chrome)
    login_page.change_language_ru()
    time.sleep(3)
    login_page.enter_login('998503018868')
    time.sleep(3)
    login_page.click_btn_enter()
    time.sleep(3)
    login_page.enter_password('hohol')
    time.sleep(3)
    login_page.click_btn_login()
    time.sleep(3)


def test_my_proweb_edge(driver_edge):
    driver_edge.get('https://my.proweb.uz/log-in?q=/home')
    login_page = LoginPage(driver_edge)
    login_page.change_language_ru()
    time.sleep(3)
    login_page.enter_login('998503018868')
    time.sleep(3)
    login_page.click_btn_enter()
    time.sleep(3)
    login_page.enter_password('hohol_08')
    time.sleep(3)
    login_page.click_btn_login()
    time.sleep(3)
    try:
        login_page.click_device_1()
        time.sleep(3)
        login_page.click_confirm_1()
        time.sleep(3)
    except (TimeoutException, NoSuchElementException):
        pass

    main_page = MainPage(driver_edge)
    main_page.click_coworking_booking()
    time.sleep(3)

    coworking_page = CoworkingPage(driver_edge)
    coworking_page.click_checkbox_confirm()
    time.sleep(3)
    coworking_page.click_btn_next()
    time.sleep(3)
    coworking_page.click_oybek_2()
    time.sleep(3)
    coworking_page.click_oybek_3()
    time.sleep(3)
    coworking_page.click_btn_select1()
    time.sleep(3)
    coworking_page.click_date_2()
    time.sleep(3)
    coworking_page.click_group()
    time.sleep(3)
    coworking_page.click_qa()
    time.sleep(3)
    coworking_page.click_btn_select2()
    time.sleep(3)
    coworking_page.click_time()
    time.sleep(3)
    coworking_page.enter_input_h(14)
    time.sleep(3)
    coworking_page.enter_input_m(45)
    time.sleep(3)
    coworking_page.click_btn_select3()
    time.sleep(3)
    coworking_page.click_place()
    time.sleep(3)
    coworking_page.click_pc_11()
    time.sleep(3)
    coworking_page.click_btn_select4()
    time.sleep(3)
    coworking_page.click_btn_book()
    time.sleep(3)

    main_page.click_see_coworking()
    time.sleep(3)

    coworking_page.click_btn_cancel()
    time.sleep(3)
    coworking_page.click_yes_confirm()
    time.sleep(3)
    coworking_page.click_btn_home()
    time.sleep(3)

    main_page.click_watch_more()
    time.sleep(3)
    main_page.click_lesson_29()
    time.sleep(3)

    video_page = VideoPage(driver_edge)
    video_page.click_btn_play()
    time.sleep(2)
    video_page.click_btn_fullscreen()
    time.sleep(15)
    video_page.resume_if_paused()
    time.sleep(15)
    # video_page.click_screen()
    # time.sleep(3)
    video_page.click_btn_pause()
    time.sleep(3)
    video_page.click_btn_collapse()
    time.sleep(3)
    try:
        video_page.click_star_5()
        time.sleep(3)
        video_page.click_btn_send()
        time.sleep(3)
    except (TimeoutException, NoSuchElementException,
            ElementClickInterceptedException, ElementNotInteractableException):
        pass

    video_page.click_btn_leave()
    time.sleep(3)
    video_page.click_logo_home()
    time.sleep(3)

    main_page.click_btn_profile()
    time.sleep(4)
    main_page.click_btn_exit()
    time.sleep(4)
    main_page.click_btn_confirm()
    time.sleep(4)


def test_invalid_my_proweb_edge(driver_edge):
    driver_edge.get('https://my.proweb.uz/log-in?q=/home')
    login_page = LoginPage(driver_edge)
    login_page.change_language_ru()
    time.sleep(3)
    login_page.enter_login('998503018868')
    time.sleep(3)
    login_page.click_btn_enter()
    time.sleep(3)
    login_page.enter_password('hohol')
    time.sleep(3)
    login_page.click_btn_login()
    time.sleep(3)




