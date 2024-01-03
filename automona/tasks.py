import os
from time import sleep
from typing import Type

from dotenv import dotenv_values
from drivers import HandleDriver


class Login:
    def __init__(self, handle_driver: Type[HandleDriver]):
        self.handle_driver = handle_driver
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

    def start(self):
        self.handle_driver.start(self.url)
        self.select_internal_user()
        self.insert_user()
        self.insert_password()
        self.click_login()

    def select_internal_user(self):
        self.handle_driver.click(
            '/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div/div[2]'
        )

    def insert_user(self):
        self.handle_driver.send_keys(
            '/html/body/div[1]/div/div/main/div/div[2]/div/div[3]/form/div/label[1]/div/div[1]/div[2]/input',
            self.user,
        )

    def insert_password(self):
        self.handle_driver.send_keys(
            '/html/body/div[1]/div/div/main/div/div[2]/div/div[3]/form/div/label[2]/div/div[1]/div[2]/input',
            self.password,
        )

    def click_login(self):
        self.handle_driver.click(
            '/html/body/div[1]/div/div/main/div/div[2]/div/div[3]/form/div/div/div[1]/div/button/span[2]'
        )


if __name__ == '__main__':
    Login(HandleDriver())
