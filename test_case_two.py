import pytest
import time
from loguru import logger
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_setup():
    logger.add("file_1.log")
    logger.info('Настройка драйвера')
    global driver 
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(60)
    driver.maximize_window()

def test_main():
    logger.info("Открываем сайт")
    driver.get("https://sbis.ru/")
    logger.info("Ожидаем загрузки страницы и нажимаем на контакты")
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]"))).click()
    logger.info("Нажимаем на еще 841 офис")
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]"))).click()
    region_check_first  = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span").text
    logger.info("Проверяем город")
    assert region_check_first == "Тюменская обл." 
    region_check_second = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/div/div[2]/a").text
    logger.info("Проверяем еще раз город")
    assert "tyumen" in region_check_second
    logger.info("Выбираем Камчатский край")
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span").click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable,((By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span")))
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span"))).text
    time.sleep(3)
    region_check  = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span"))).text
    assert region_check == "Камчатский край" 
    region_check_second = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/div/div[2]/a").text
    logger.info("Проверяем еще раз город")
    assert "kamchatka" in region_check_second
    current_url = driver.current_url
    logger.info("Проверяем ссылку")
    assert "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients" == current_url