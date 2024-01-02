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
        self.__create_drive()
        self.__open_website()

    def __create_drive(self):
        """Create a instance of selenium webdrive."""
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        if self.background:
            options.add_argument('--headless=new')
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            self.driver = webdriver.Chrome(service=service)

    def __wait_to_load_element(self, xpath_value, timeout=0.5):
        """Wait for an element to be present in the DOM."""
        while True:
            sleep(timeout)
            if driver.find_element(By.XPATH, xpath_value):
                return driver.find_element(By.XPATH, xpath_value)

    def __open_website(self):
        """Open website with url."""
        self.driver.get(self.url)

    def click(self, xpath):
        """Click on selenium webdriver element."""
        element = self.__wait_to_load_element(xpath)
        element.click()

    def send_keys(self, xpath, keys):
        """Send keys to selenium webdriver element."""
        element = self.__wait_to_load_element(xpath)
        element.send_keys(keys)

    def get_url(self, value):
        """Set a new url."""
        self.url = value

    def close(self):
        """Close selenium webdriver."""
        self.driver.quit()