from framework.page_objects.wrapper import SeleniumWrapper
from selenium.webdriver.common.by import By
from framework.utils.element_locator import ElementLocator as el
from allure_commons._allure import step


class LoginPage(SeleniumWrapper):

    signin_box_btn = el(By.XPATH, "//span[contains(text(),'Sign in')]")
    username_txtbox = el(By.ID, "username-pulldown")
    password_txtbox = el(By.ID, "password-pulldown")
    login_btn = el(By.XPATH, "//input[@id='login-pulldown']")
    post_login_title = el(By.PARTIAL_LINK_TEXT, "OpenProject ")

    def __init__(self, driver):
        self.driver = driver

    @step("open OpenProjectSite signin box")
    def open_signin_box(self):
        self.click(self.signin_box_btn)

    @step("enter user name")
    def set_user_name(self, username):
        self.send_keys(self.username_txtbox, username)

    @step("enter password")
    def set_password(self, password):
        self.send_keys(self.password_txtbox, password)

    @step("click login button")
    def click_login_button(self):
        self.click(self.login_btn)

    @step("checking page title to verify login success")
    def get_page_title_after_login(self):
        return self.get_text(self.post_login_title)

