from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class HandleDriver:
    def __init__(self, background: bool = False):
        self.background = background
        self.driver = None

    def create_drive(self):
        """Create a instance of selenium webdrive."""
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )
        if self.background:
            options.add_argument('--headless=new')
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            self.driver = webdriver.Chrome(service=service)

    def wait_element(self, xpath_value, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath_value))
        )
        return self.driver.find_element(By.XPATH, xpath_value)

    def load_page(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, '/html/body'))
        )

    def open_website(self):
        """Open website with url."""
        self.driver.get(self.url)
        self.load_page()

    def start(self, url):
        self.get_url(url)
        self.create_drive()
        self.open_website()

    def click(self, xpath):
        """Click on selenium webdriver element."""
        self.wait_element(xpath).click()

    def send_keys(self, xpath, keys):
        """Send keys to selenium webdriver element."""
        self.wait_element(xpath).send_keys(keys)

    def get_url(self, value):
        """Set a new url."""
        self.url = value

    def close(self):
        """Close selenium webdriver."""
        self.driver.quit()
