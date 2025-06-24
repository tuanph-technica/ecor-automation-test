import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains




class ProductPlaneDetail(BaseDriver):
    BUTTON_CREATE_DOMESTIC_PRODUCTION_LIST = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-product-plan-detail/app-product-plan-detail-domestic/nz-row/nz-col/nz-space/button"
    BUTTON_CREATE_EXPORT_PRODUCTION_LIST =   "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-product-plan-detail/app-product-plan-detail-export/nz-row/nz-col/nz-space/button"
    BUTTON_CREATE_MATERIAL_PRODUCTION_LIST = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-product-plan-detail/app-product-plan-detail-material/nz-row/nz-col/nz-space/button"
    CREATE_PRODUCTION_CONFIRM_DIALOG = "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/app-popup-confirm-create-production-list"
    def create_domestic_production_list(self):
        btn_create_production_list = self.find_element(By.XPATH,self.BUTTON_CREATE_DOMESTIC_PRODUCTION_LIST)
        btn_create_production_list.click()
        time.sleep(2)
        popup_confirm = self.driver.find_element(By.XPATH,"//*[contains(@class, 'ant-modal-content')]")
        buttons = popup_confirm.find_elements(By.TAG_NAME,"button")
        buttons[1].click()
    def create_export_production_list(self):
        btn_create = self.find_element(By.XPATH,self.BUTTON_CREATE_EXPORT_PRODUCTION_LIST)
        btn_create.click()
        time.sleep(2)
        popup_confirm = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-body')]")
        buttons = popup_confirm.find_elements(By.TAG_NAME, "button")
        buttons[1].click()
    def create_material_production_list(self):
        btn_create = self.find_element(By.XPATH, self.BUTTON_CREATE_MATERIAL_PRODUCTION_LIST)
        btn_create.click()
        time.sleep(2)
        popup_confirm = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-body')]")
        buttons = popup_confirm.find_elements(By.TAG_NAME, "button")
        buttons[1].click()



class CreateProductPlan(BaseDriver):
    POPUP_ADD_CAR_TAG_NAME = "app-popup-add-car"
    WAITING_LIST_FILTER_TAG_NAME = "app-waiting-list-filter"
    DROPDOWN_CONTENT_LIST_TAG = "cdk-virtual-scroll-viewport"
    def __init__(self,driver,department_name):
        super().__init__(driver)
        self.BUTTON_CONFIRM_PRODUCT_PLAN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-create-product-plan/app-create-product-plan-" + department_name + "/nz-row/nz-col/nz-space/div[2]/button"
        self.BUTTON_CANCEL_PRODUCT_PLAN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-create-product-plan/app-create-product-plan-" + department_name + "/nz-row/nz-col/nz-space/div[1]/button"
        self.BUTTON_ADD_CAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-create-product-plan/app-create-product-plan-" + department_name + "/nz-card[2]/div[1]/div/div[2]/button"
        self.BUTTON_REMOVE_CAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-create-product-plan/app-create-product-plan-" + department_name  + "/nz-card[2]/div[2]/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-title-footer[1]/nz-space/div/button"


    def enter_web_item_text(self, text_element, text_value):
         text_element.send_keys(Keys.CLEAR)
         text_element.send_keys(text_value)
         text_element.send_keys(Keys.ENTER)
         time.sleep(2)
    def enter_web_item_drop_down(self,dropdown_element,option_value):
        time.sleep(2)
        dropdown_element.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.TAG_NAME, self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        for item in dropdown_items:
            if item.text == option_value:
                item.click()
                break

        time.sleep(2)
    def confirm_product_plan(self):
        confirm_button = self.find_element(By.XPATH,self.BUTTON_CONFIRM_PRODUCT_PLAN)
        confirm_button.click()
    def cancel_product_plan(self):
        cancel_button = self.find_element(By.XPATH,self.BUTTON_CANCEL_PRODUCT_PLAN)
        cancel_button.click()
    def add_cars_by_chasis_number(self,chasis_numbers=[]):
        btn_add_car = self.find_element(By.XPATH, self.BUTTON_ADD_CAR)
        btn_add_car.click()
        time.sleep(2)
        dialog_content = self.find_element(By.TAG_NAME, self.POPUP_ADD_CAR_TAG_NAME)
        table_body = dialog_content.find_element(By.TAG_NAME, "tbody")
        car_items = table_body.find_elements(By.TAG_NAME, "tr")
        if len(car_items) <= 2:
            buttons = dialog_content.find_elements(By.TAG_NAME, "button")
            button_cancel = buttons[3]
            button_cancel.click()
            time.sleep(2)
            return
        for car_item in car_items:
            columns = car_item.find_elements(By.TAG_NAME,"td")
            chasis_num = columns[4].text
            if chasis_num in chasis_numbers:
                input = columns[0].find_element(By.TAG_NAME,"input")
                input.click()
        button_add = dialog_content.find_elements(By.TAG_NAME, "button")[1]
        button_add.click()
        time.sleep(3)
    def removed_car_by_chasis_numbers(self,chasis_numbers=[]):
        nz_table = self.find_element(By.TAG_NAME, "nz-table")
        table_body = nz_table.find_element(By.TAG_NAME, "tbody")
        car_items = table_body.find_elements(By.TAG_NAME, "tr")
        for car_item in car_items:
            columns = car_item.find_elements(By.TAG_NAME,"td")
            if columns[4].text in chasis_numbers:
                input = columns[0].find_element(By.TAG_NAME,"input")
                input.click()
        title_footer = nz_table.find_element(By.TAG_NAME,"nz-table-title-footer")
        button_remove = title_footer.find_elements(By.TAG_NAME,"button")
        if len(button_remove) > 0:
            button_remove[0].click()





    def add_cars_by_select_in_list(self,number_of_cars):
        btn_add_car = self.find_element(By.XPATH,self.BUTTON_ADD_CAR)
        btn_add_car.click()
        time.sleep(4)
        dialog_content = self.find_element(By.TAG_NAME,self.POPUP_ADD_CAR_TAG_NAME)
        table_body = dialog_content.find_element(By.TAG_NAME,"tbody")
        car_items = table_body.find_elements(By.TAG_NAME,"tr")
        if number_of_cars > len(car_items):
            number_of_cars = len(car_items)-1
        for i in range(number_of_cars):
            random_idx = random.randint(1,len(car_items)-1)
            car_item = car_items[random_idx]
            tds = car_item.find_elements(By.TAG_NAME,"td")
            checkbox = tds[0].find_elements(By.TAG_NAME,"input")
            time.sleep(2)
            checkbox[0].click()
        button_add = dialog_content.find_elements(By.TAG_NAME,"button")[1]
        button_add.click()
        time.sleep(3)
    def add_car_by_filter(self,request_num="",search_text="",production_flow="",
                          production_status="",
                          warehouse=""):
        btn_add_car = self.find_element(By.XPATH, self.BUTTON_ADD_CAR)
        btn_add_car.click()
        time.sleep(4)
        waiting_filter_list = self.find_element(By.TAG_NAME, self.WAITING_LIST_FILTER_TAG_NAME)
        if request_num != "":
            ddl_request_num = waiting_filter_list.find_elements(By.TAG_NAME,"nz-select")[0]
            self.enter_web_item_drop_down(ddl_request_num,request_num)
            time.sleep(2)
        if search_text != "":
            txt_search = waiting_filter_list.find_elements(By.TAG_NAME,"input")
            self.enter_web_item_text(txt_search[1],search_text)
            time.sleep(1)
        if production_flow != "":
            ddl_production_flow = waiting_filter_list.find_elements(By.TAG_NAME, "nz-select")[1]
            self.enter_web_item_drop_down(ddl_production_flow, production_flow)
            time.sleep(2)
        if production_status != "":
            ddl_production_status = waiting_filter_list.find_elements(By.TAG_NAME, "nz-select")[2]
            self.enter_web_item_drop_down(ddl_production_status, production_status)
            time.sleep(2)
        if warehouse != "":
            ddl_warehouse = waiting_filter_list.find_elements(By.TAG_NAME, "nz-select")[3]
            self.enter_web_item_drop_down(ddl_warehouse, warehouse)
            time.sleep(2)
        app_popup_addcar = self.find_element(By.TAG_NAME,"app-popup-add-car")
        body_tab = app_popup_addcar.find_element(By.TAG_NAME,"tbody")
        trs = body_tab.find_elements(By.TAG_NAME,"tr")
        num_rec = len(trs)-1
        num_car_add = random.randint(1,num_rec-1)
        indexes = random.sample(range(1,num_rec),num_car_add)
        for index in indexes:
            tds = trs[index].find_elements(By.TAG_NAME,"td")
            tds[0].click()
        buttons = app_popup_addcar.find_elements(By.TAG_NAME,"button")
        buttons[-1].click()
        time.sleep(3)


    def remove_batch_cars(self, num_car_remove):
        nz_table = self.find_element(By.TAG_NAME,"nz-table")
        table_body = nz_table.find_element(By.TAG_NAME,"tbody")
        car_items = table_body.find_elements(By.TAG_NAME,"tr")
        num_car = len(car_items)
        if num_car_remove > num_car:
            num_car_remove = num_car
        for i in range(num_car_remove):
            car_index = random.randint(1,num_car-2)
            tds = car_items[car_index].find_elements(By.TAG_NAME,"td")
            checkbox = tds[0].find_elements(By.TAG_NAME, "input")
            time.sleep(2)
            checkbox[0].click()

        remove_button = nz_table.find_elements(By.TAG_NAME,"button")[0]
        remove_button.click()
    def remove_car_from_table(self):
        nz_table = self.find_element(By.TAG_NAME, "nz-table")
        table_body = nz_table.find_element(By.TAG_NAME, "tbody")
        car_items = table_body.find_elements(By.TAG_NAME, "tr")
        num_car = len(car_items)
        car_index = random.randint(1,num_car)
        image = car_items[car_index].find_elements(By.TAG_NAME,"img")[0]
        image.click()
    def create_production_list(self):
        button_create_product_list = self.find_element(By.XPATH,"/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-product-plan-detail/app-product-plan-detail-domestic/nz-row/nz-col/nz-space/button")
        button_create_product_list.click()
        time.sleep(2)











