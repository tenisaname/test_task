import pytest
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
    logger.info("Переходим на страницу контактов")
    logger.info("Находим логотип тензор и нажимаем его")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME,'a')))
    links = driver.find_elements(By.TAG_NAME, "a")
    for i in links:
        href = i.get_attribute('href')
        logger.info(str(href))
        if href == "https://tensor.ru/":
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable(i))
            i.click()
            break
        
def test_contacts():
    logger.info("Проверяем надпись")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME,"a")))

    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a").click()
