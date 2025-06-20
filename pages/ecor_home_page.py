from selenium.webdriver.common.by import By
import time
from base.base_driver import BaseDriver
from pages.CarProductManagement import CarProductManager
from pages.CarProductionList import CarProductionList
from pages.CarValuationList import CarValuationList
from pages.PartsManagement import PartsManagement
from pages.car_list import CarList
from pages.car_registration import CarRegistration
from pages.CarAssetmentList import CarAssetmentList


class EcorHomePage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)

    MENU_CAR_CLASS_NAME = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-sider/div/app-menu-bar/ul/li[1]/div/div/img"
    BUTTON_ADD_NEW = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-row/nz-col/nz-space/div/button"
    MENU_CAR_ASSETMENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-sider/div/app-menu-bar/ul/li[2]/div/div/img"

    MENU_SYS = "/html/body/app-root/app-home/nz-layout/nz-header/app-header/div/nz-row/nz-col[4]/div/div[4]/span"
    LOG_OUT_MENU = "/html/body/div[2]/div/div/div/div/div[2]/div/div/div"
    APP_MENU_BAR_TAG_NAME = "app-menu-bar"
    def get_car_menu(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MENU_CAR_CLASS_NAME)
    def get_car_valuation_menu(self):
        menu_bar = self.find_element(By.TAG_NAME,self.APP_MENU_BAR_TAG_NAME)
        li_menus =  self.find_elements_from_node(menu_bar,By.TAG_NAME,"li")
        return li_menus[2]
    def get_car_production_menu(self):
        menu_bar = self.find_element(By.TAG_NAME,self.APP_MENU_BAR_TAG_NAME)
        li_menus =  self.find_elements_from_node(menu_bar,By.TAG_NAME,"li")
        return li_menus[3]
    def get_car_production_menu_from_apg_user(self):
        menu_bar = self.find_element(By.TAG_NAME,self.APP_MENU_BAR_TAG_NAME)
        li_menus =  self.find_elements_from_node(menu_bar,By.TAG_NAME,"li")
        return li_menus[0]
    def get_car_production_management_menu(self):
        menu_bar = self.find_element(By.TAG_NAME, self.APP_MENU_BAR_TAG_NAME)
        li_menus = self.find_elements_from_node(menu_bar, By.TAG_NAME, "li")
        return li_menus[5]
    def get_car_production_management_menu_from_apg_user(self):
        menu_bar = self.find_element(By.TAG_NAME, self.APP_MENU_BAR_TAG_NAME)
        li_menus = self.find_elements_from_node(menu_bar, By.TAG_NAME, "li")
        return li_menus[1]

    def get_part_code_management_menu(self):
        menu_bar = self.find_element(By.TAG_NAME, self.APP_MENU_BAR_TAG_NAME)
        li_menus = self.find_elements_from_node(menu_bar, By.TAG_NAME, "li")
        return li_menus[6]
    def get_add_new_button(self):
        time.sleep(7)
        parent_element = self.driver.find_elements(By.TAG_NAME,"app-car-list")
        buttons = parent_element[0].find_elements(By.TAG_NAME,'button')
        return buttons[0]
    def get_car_assetment_menu(self):
        return  self.wait_until_element_is_clickable(By.XPATH,self.MENU_CAR_ASSETMENT)
    def get_menu_system(self):
        menu = self.find_elements(By.XPATH,self.MENU_SYS)
        return menu[0]

    def get_menu_logout(self):
        time.sleep(2)
        menu_parent = self.find_element(By.XPATH,"//div[contains(@class, 'ant-popover-inner')]")
        menu_items = menu_parent.find_elements(By.CLASS_NAME,"item-content")
        return menu_items[-1]


    def click_menu_log_out(self):
        time.sleep(2)
        self.driver.execute_script
        self.get_menu_logout().click()
    def click_menu_system(self):
        time.sleep(5)
        menu_system = self.get_menu_system()
        self.driver.execute_script("arguments[0].click();", menu_system)
    def click_car_menu(self):
        self.get_car_menu().click()
    def click_add_car(self):
        add_button = self.get_add_new_button()
        self.driver.execute_script("arguments[0].click();", add_button)
    def get_car_list(self):
        time.sleep(3)
        menu = self.get_car_menu()
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(2)
        car_list = CarList(self.driver)
        return car_list
    def get_car_valuation_list(self):
        time.sleep(3)
        menu = self.get_car_valuation_menu()
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(2)
        car_list = CarValuationList(self.driver)
        return car_list
    def get_car_production_list(self):
        time.sleep(3)
        menu = self.get_car_production_menu()
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(2)
        car_production_list = CarProductionList(self.driver)
        return car_production_list
    def get_car_production_list_from_agp_user(self):
        time.sleep(3)
        menu = self.get_car_production_menu_from_apg_user()
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(2)
        car_production_list = CarProductionList(self.driver)
        return car_production_list
    def get_car_production_manager(self):
        time.sleep(3)
        menu = self.get_car_production_management_menu()
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(2)
        car_production_manager = CarProductManager(self.driver)
        return car_production_manager
    def get_car_production_manager_from_apg_user(self):
        time.sleep(3)
        menu = self.get_car_production_management_menu_from_apg_user()
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(2)
        car_production_manager = CarProductManager(self.driver)
        return car_production_manager
    def get_part_management(self):
        time.sleep(2)
        part_menu = self.get_part_code_management_menu()
        self.driver.execute_script("arguments[0].click();", part_menu)
        time.sleep(2)
        part_management_obj = PartsManagement(self.driver)
        return part_management_obj






    def registration_car(self):
        time.sleep(3)
        self.click_car_menu()
        time.sleep(3)
        self.click_add_car()
        time.sleep(2)
        registration = CarRegistration(self.driver)
        return registration
    def assessment_car(self):
        time.sleep(3)
        menu = self.get_car_assetment_menu()
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(2)
        car_assetment = CarAssetmentList(self.driver)
        return car_assetment
    def logout(self):
        self.click_menu_system()
        time.sleep(2)
        logout_menu = self.get_menu_logout()
        self.driver.execute_script("arguments[0].click();",logout_menu )