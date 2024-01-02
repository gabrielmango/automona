from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class HandleDriver:
    def __init__(self, url: str, background: bool = False):
        self.url = url
        self.background = background
        self.driver = None

    def __create_drive(self):
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        if self.background:
            options.add_argument('--headless=new')
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            self.driver = webdriver.Chrome(service=service)
        
        