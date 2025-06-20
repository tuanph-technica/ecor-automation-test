import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from base.base_driver import BaseDriver
from selenium import webdriver

from pages.ecor_home_page import EcorHomePage


class LogIn(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)


    USER_NAME_FIELD = "/html/body/app-root/app-login/div/div/form/nz-form-item[1]/nz-form-control/div/div/input"
    PASSWORD_FIELD = "/html/body/app-root/app-login/div/div/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input"
    LOGIN_BTN =      "/html/body/app-root/app-login/div/div/form/nz-form-item[4]/nz-form-control/div/div/button/span"
    def get_user_name_from_field(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.USER_NAME_FIELD)
    def get_password_from_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PASSWORD_FIELD)
    def get_login_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LOGIN_BTN)
    def enter_user_name(self,user_name):
        self.get_user_name_from_field().click()
        time.sleep(2)
        self.get_user_name_from_field().send_keys(user_name)
        self.get_user_name_from_field().send_keys(Keys.ENTER)
    def enter_password(self,password):
        self.get_password_from_field().click()
        time.sleep(2)
        self.get_password_from_field().send_keys(password)
        self.get_password_from_field().send_keys(Keys.ENTER)
    def click_login_button(self):
        login_button = self.get_login_button()

        self.driver.execute_script('arguments[0].click()', login_button)
        time.sleep(4)
    def do_login(self,user_name,password):
        self.enter_user_name(user_name)
        self.enter_password(password)
        self.click_login_button()
        hp = EcorHomePage(self.driver)
        time.sleep(5)
        return hp

        


