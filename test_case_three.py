import pytest
import time
import os
from loguru import logger
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def latest_download_file():
      download_dir = "C:\\Users\\ETenkin\\Desktop\\test_2"
      os.chdir(download_dir)
      files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
      latest_f = files[-1]
      return latest_f

def test_setup():
    logger.add("file_1.log")
    logger.info('Настройка драйвера')
    global driver 
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    prefs = {
    "download.default_directory": "C:\\Users\\ETenkin\\Desktop\\test_2", 
    "download.prompt_for_download": False,  
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    }   
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(60)
    driver.maximize_window()

def test_main():
    logger.info("Открываем сайт")
    driver.get("https://sbis.ru/")
    logger.info("Нажимаем Скачать локальные версии")
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a"))).click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/a"))).click()
    has_crdownload = True
    while has_crdownload:
        time.sleep(.6)
        newest_file = latest_download_file()
        if not "crdownload" in newest_file:
            has_crdownload = False
    size_check = os.stat('C:\\Users\\ETenkin\\Desktop\\test_2\\sbisplugin-setup-web.exe').st_size
    logger.info(f"Проверяем размер {size_check}")
    driver.close()
    assert 12039392 == int(size_check)
