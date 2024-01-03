import os
from time import sleep
from typing import Type

from dotenv import dotenv_values
from drivers import HandleDriver


class Login:
    def __init__(self, handle_driver: Type[HandleDriver]):
        self.handle_driver = handle_driver()
        self.user = None
        self.password = None
        self.url = None
        self.__get_env()
        self.__login()
        sleep(1)
        self.handle_driver.load_page()

    def __get_env(self):
        config = dotenv_values('.env')
        self.user = config['USER']
        self.password = config['PASSWORD']
        self.url = config['URL']

    def __login(self):
        self.handle_driver.start(self.url)
        self.__select_internal_user()
        self.__insert_user()
        self.__insert_password()
        self.__click_login()
        self.handle_driver.load_page()

    def __select_internal_user(self):
        self.handle_driver.click(
            '//main/div/div[2]/div/div[1]/div/div[2]'
        )

    def __insert_user(self):
        self.handle_driver.send_keys(
            '//main/div/div[2]/div/div[3]/form/div/label[1]/div/div[1]/div[2]/input',
            self.user,
        )

    def __insert_password(self):
        self.handle_driver.send_keys(
            '//main/div/div[2]/div/div[3]/form/div/label[2]/div/div[1]/div[2]/input',
            self.password,
        )

    def __click_login(self):
        self.handle_driver.click(
            '//main/div/div[2]/div/div[3]/form/div/div/div[1]/div/button/span[2]'
        )


class Productivity(Login):
    def __init__(self, handle_driver: Type[HandleDriver]):
        super().__init__(handle_driver)
        sleep(3)
        self.start()

    def start(self):
        self.general_menu()
        self.sti_menu()
        self.sgp_menu()
        self.handle_driver.load_page()
        self.new_productivity()
        sleep(5)

    def general_menu(self):
        self.handle_driver.click(
            '/html/body/div[1]/div/header/div[1]/button[1]'
        )
    
    def sti_menu(self): 
        self.handle_driver.click(
            '/html/body/div[3]/div/div[2]/div/nav/ul/li[6]/i'
        )
    
    def sgp_menu(self):
        self.handle_driver.click(
            '/html/body/div[4]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[3]/div'
        )
    
    def new_productivity(self):
        self.handle_driver.click(
            '/html/body/div[1]/div/div/main/div[1]/div/div[1]/div[2]/div/div/button'
        )


if __name__ == '__main__':
    Productivity(HandleDriver)
