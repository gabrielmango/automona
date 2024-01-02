from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)


URL = 'https://gerais.defensoria.mg.def.br/sistemas/scsdp/'


def wait_to_load_element(xpath_value, timeout=0.5):
    """Wait for an element to be present in the DOM."""
    while True:
        sleep(timeout)
        if driver.find_element(By.XPATH, xpath_value):
            return driver.find_element(By.XPATH, xpath_value)


def click(element):
    """Click on element selenium driver."""
    element.click()


driver.get(URL)

click(
    wait_to_load_element(
        '//*[@id="dpmg-container-login"]/div/div[1]/div/div[2]'
    )
)

sleep(2)
driver.close()
