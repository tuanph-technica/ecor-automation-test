from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from base.base_driver import BaseDriver
from pages.ProductCarManagementDetail import ProductCarManagementDetail, ProductOutComeDetail


class CarProductManager(BaseDriver):
    PARENT_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-product-management/app-outcome-list"
    DROPDOWN_CONTENT_LIST_TAG = "cdk-virtual-scroll-viewport"
    def enter_web_item_text(self, text_element, text_value):
         text_element.send_keys(Keys.CONTROL + "a")
         text_element.send_keys(Keys.DELETE)
         text_element.send_keys(text_value)
         text_element.send_keys(Keys.ENTER)
         time.sleep(2)
    def enter_web_item_drop_down(self,dropdown_element,option_value):
        time.sleep(2)
        dropdown_element.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.TAG_NAME, self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        if isinstance(option_value,int):
            dropdown_items[option_value].click()
        else:
            for item in dropdown_items:
                if item.text.find(option_value) >= 0:
                    item.click()
                    break
        time.sleep(2)
    def enter_web_item_button(self,button_element):
        button_element.click()
        time.sleep(2)


    def get_products_from_list(self,product_index):
        parent_content = self.find_element(By.XPATH,self.PARENT_CONTENT)
        nz_cards = parent_content.find_elements(By.TAG_NAME,"nz-card")
        table_body = nz_cards[0].find_elements(By.TAG_NAME,"tbody")[0]
        production_list = table_body.find_elements(By.TAG_NAME,"tr")
        production_list[product_index].click()
        time.sleep(2)
        car_production_detail = ProductCarManagementDetail(self.driver)
        return car_production_detail
    def get_production_plan_from_date(self,production_date=""):
        parent_content = self.find_element(By.XPATH, self.PARENT_CONTENT)
        nz_cards = parent_content.find_elements(By.TAG_NAME, "nz-card")
        table_body = nz_cards[0].find_elements(By.TAG_NAME, "tbody")[0]
        trs = table_body.find_elements(By.TAG_NAME, "tr")
        for tr in trs:
            td = tr.find_elements(By.TAG_NAME,"td")
            if td[0].text == production_date:
                tr.click()
                time.sleep(2)
                car_production_detail = ProductCarManagementDetail(self.driver)
                return car_production_detail









    def search_outcome(self,production_date = "", department = ""):
        parent_content = self.find_element(By.XPATH, self.PARENT_CONTENT)
        nz_cards = parent_content.find_elements(By.TAG_NAME, "nz-card")
        card_body = nz_cards[1].find_element(By.CLASS_NAME,"ant-card-body")
        nz_rows = card_body.find_elements(By.XPATH,"./nz-row")
        nz_cols = nz_rows[1].find_elements(By.XPATH,"./nz-col")
        if production_date != "":
            txt_input_date = nz_cols[0].find_element(By.TAG_NAME,"input")
            self.enter_web_item_text(txt_input_date,production_date)
        if department != "":
            ddl_department = nz_cols[1].find_element(By.TAG_NAME,"app-select-department-by-product-plan")
            self.enter_web_item_drop_down(ddl_department,department)
        table_body = nz_cards[1].find_elements(By.TAG_NAME, "tbody")[0]
        outcome_list = table_body.find_elements(By.TAG_NAME, "tr")
        return len(outcome_list)
    def reset_outcome_list_search(self):
         parent_content = self.find_element(By.XPATH, self.PARENT_CONTENT)
         nz_cards = parent_content.find_elements(By.TAG_NAME, "nz-card")
         button = nz_cards[1].find_element(By.TAG_NAME,"button")
         button.click()
         time.sleep(2)
    def get_product_outcome_from_list(self,outcome_index):
        parent_content = self.find_element(By.XPATH, self.PARENT_CONTENT)
        nz_cards = parent_content.find_elements(By.TAG_NAME, "nz-card")
        table_body = nz_cards[1].find_elements(By.TAG_NAME, "tbody")[0]
        outcome_list = table_body.find_elements(By.TAG_NAME, "tr")
        outcome_list[outcome_index].click()
        time.sleep(2)
        outcome_detail = ProductOutComeDetail(self.driver)
        return outcome_detail
    def get_number_product_from_list(self):
        parent_content = self.find_element(By.XPATH, self.PARENT_CONTENT)
        nz_cards = parent_content.find_elements(By.TAG_NAME, "nz-card")
        table_body = nz_cards[0].find_elements(By.TAG_NAME, "tbody")[0]
        production_list = table_body.find_elements(By.TAG_NAME, "tr")
        return len(production_list)
    def get_production_manager_column_counts(self):
        parent_content = self.find_element(By.XPATH, self.PARENT_CONTENT)
        nz_cards = parent_content.find_elements(By.TAG_NAME, "nz-card")
        table = nz_cards[0].find_elements(By.TAG_NAME, "table")[0]
        column_list = table.find_elements(By.TAG_NAME, "th")
        return len(column_list)
    def get_outcome_number_from_list(self):
        parent_content = self.find_element(By.XPATH, self.PARENT_CONTENT)
        nz_cards = parent_content.find_elements(By.TAG_NAME, "nz-card")
        table_body = nz_cards[1].find_elements(By.TAG_NAME, "tbody")[0]
        outcome_list = table_body.find_elements(By.TAG_NAME, "tr")
        return len(outcome_list)










