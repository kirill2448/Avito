from random import random

aplication=['Domain-Driven Design Distilled Vaughn Vernon']

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime
import pandas as pd

# %%
trhold_time = 15


# всякие функции для тыканья по кнопкам

def send_keys(driver, login_password, data):
    wait = WebDriverWait(driver, trhold_time)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_password)))
    element.send_keys(data)


def wait_click_by_xpath(driver, xpath):
    wait = WebDriverWait(driver, trhold_time)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


def wait_by_css_selector(driver, css_selector):
    wait = WebDriverWait(driver, trhold_time)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def wait_click_by_css(driver, css_selector):
    wait = WebDriverWait(driver, trhold_time)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    element.click()


def wait_load_by_xp(driver, xpath):
    wait = WebDriverWait(driver, trhold_time)
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


# %%
def create_today_folder():
    #     создает папку с сегодняшней датой
    today = str(datetime.date.today())
    path_desk = r'C:\Users\syr67\PycharmProjects'
    path = os.path.join(path_desk, today)
    if not os.path.exists(path):
        os.mkdir(path)
    path_file = os.path.join(path, f'{today}.txt')
    return path_file


def write_to_file(path, text):
    #     записать текс в файл
    with open(path, 'a') as file:
        file.write(text + '\n')


# %%
wd_path = r'C:\Users\syr67\Desktop\chromedriver.exe'  # path to Chromedriver


def get_driver(wd_path):
    #     подключение драйвера парсера
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')

    options.add_experimental_option("prefs", {
       # "download.default_directory": r'C:\Users\4268\Desktop\savs',
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(wd_path, options=options)
    return driver


# %%
def go_avito_favourites(driver):
    #     преход на авито
    time_wait=1
    url_avito = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
    driver.get(url_avito)
    for al in aplication:
        results[al] = [0, 0, 0, 0, 0]
        xp = '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button'
        wait_click_by_xpath(driver, xp)  # тык в избранное
        time.sleep(time_wait)
        path = create_today_folder()
        write_to_file(path, "from favourites")
        xp = '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span' # ищу что объявление добавилось
        wait_load_by_xp(driver, xp)
        el = driver.find_element(By.XPATH, xp)
        print(f'элемент = {el.text}')  # факт

        write_to_file(path,f'Объявление   {el.text}')
        results[al][0] = el.text




# %%
def go_avito_main_page(driver):
    #     преход на авито
    time_wait = 1
    path = create_today_folder()
    url_avito = "https://www.avito.ru"
    driver.get(url_avito)
    for al in aplication:
        results[al] = [0, 0, 0, 0, 0]
        xp = '/html/body/div[1]/div/div[3]/div[1]/div/div[1]/div[3]/div[2]/div[1]/div/div/div/label[1]/input' #ищем
        wait_load_by_xp(driver, xp)
        el = driver.find_element(By.XPATH, xp)


        for _ in range(len(al)):
            el.send_keys(Keys.BACKSPACE)  # dellete text in search window
        el.send_keys(al)

        wait_load_by_xp(driver, xp)
        el.send_keys(Keys.RETURN)

        time.sleep(time_wait)
        print(al)
        write_to_file(path, al)

        xp = '/html/body/div[1]/div/div[3]/div/div[2]/div[3]/div[3]/div[3]/div[3]/div[2]/div/div/div[2]/div[1]/div'
        wait_click_by_xpath(driver, xp)  # тык в избранное
        time.sleep(time_wait)
        write_to_file(path, "from favourites")
        xp='/html/body/div[1]/div/div[3]/div/div[2]/div[3]/div[3]/div[3]/div[3]/div[2]/div/div/div[2]/div[1]/div' #считываю избранное

        wait_load_by_xp(driver, xp)
        el = driver.find_element(By.XPATH, xp)
        print(f'элемент = {el.text}')  # факт

        write_to_file(path, f'Объявление   {el.text}')
        results[al][1] = el.text










results = {} #тянем словрь

driver = get_driver(wd_path)

go_avito_favourites(driver) # запустить сначала первую функцию потом вторую
#go_avito_main_page(driver) # запустить отдельно от первой функции 


