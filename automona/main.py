from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

URL = 'https://gerais.defensoria.mg.def.br/sistemas/scsdp/'

driver.get(URL)

# click on DPMG INTERNO
driver.find_element(
    By.XPATH, '//*[@id="dpmg-container-login"]/div/div[1]/div/div[2]'
).click()

sleep(2)
driver.close()
