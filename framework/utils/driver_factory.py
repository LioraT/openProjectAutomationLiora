from selenium import webdriver
import pytest


class DriverFactory:

    @staticmethod
    def create(browser) -> webdriver:

        if browser == 'Chrome':
            # driver = webdriver.Chrome(executable_path="/drivers/chromedriver.exe")
            driver = webdriver.Chrome(executable_path="C:/Users/ltwig/PycharmProject/SeleniumProjectLiora/drivers/chromedriver.exe")
            return driver

        elif browser == 'Firefox':
            # driver = webdriver.Firefox(executable_path="/drivers/geckodriver.exe")
            driver = webdriver.Chrome(executable_path="C:/Users/ltwig/PycharmProject/SeleniumProjectLiora/drivers/geckodriver.exe")
            return driver