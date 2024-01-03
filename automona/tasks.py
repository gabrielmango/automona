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
        self.start()

    def __get_env(self):
        config = dotenv_values('.env')
        self.user = config['USER']
        self.password = config['PASSWORD']
        self.url = config['URL']

    def start(self, _time=3):
        self.handle_driver.start(self.url)
        self.select_internal_user()
        self.insert_user()
        self.insert_password()
        self.click_login()
        sleep(_time)

    def select_internal_user(self):
        self.handle_driver.click('//main/div/div[2]/div/div[1]/div/div[2]')

    def insert_user(self):
        self.handle_driver.send_keys(
            '//main/div/div[2]/div/div[3]/form/div/label[1]/div/div[1]/div[2]/input',
            self.user,
        )

    def insert_password(self):
        self.handle_driver.send_keys(
            '//main/div/div[2]/div/div[3]/form/div/label[2]/div/div[1]/div[2]/input',
            self.password,
        )

    def click_login(self):
        self.handle_driver.click(
            '//main/div/div[2]/div/div[3]/form/div/div/div[1]/div/button/span[2]'
        )


class Productivity:
    def __init__(self, handle_driver: Type[HandleDriver]):
        self.handle_driver = handle_driver()
        self.start()

    def start(self):
        login = Login(HandleDriver)
        self.click_menu()

    def click_menu(self):
        self.handle_driver.click(
            '/html/body/div[1]/div/header/div[1]/button[1]'
        )


if __name__ == '__main__':
    Productivity(HandleDriver)
