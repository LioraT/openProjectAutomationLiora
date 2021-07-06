from framework.page_objects.wrapper import SeleniumWrapper
from framework.page_objects.login_page import LoginPage
from utils.read_properties import ReadConfig
from tests.ui.conf_test import setup

username = ReadConfig.getUserEmail()
password = ReadConfig.getPassword()


class SharedSteps(SeleniumWrapper):

    @staticmethod
    def login_steps(driver):
        driver.maximize_window()
        login_page = LoginPage(driver)
        login_page.open_signin_box()
        login_page.set_user_name(username)
        login_page.set_password(password)
        login_page.click_login_button()
        act_title = login_page.get_page_title_after_login()
        assert act_title == "OpenProject " + username.capitalize(), "Login to open project "
