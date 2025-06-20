from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from base.base_driver import BaseDriver
from pages.CarValuationDetail import CarValuationDetail
from pages.CarWaitingList import CarWaitingList
from pages.ProductPlaneDetail import ProductPlaneDetail


class CarProductionList(BaseDriver):
    PRODUCTION_PLANNING = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-plan-list"
    CARD_BODY_CLASSNAME = "ant-card-body"
    PRODUCTION_DATE_INPUT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-plan-list/nz-card[2]/div/nz-row[2]/nz-col[1]/app-date-picker/nz-date-picker/div/input"
    DROPDOWNLIST_DEPARTMENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-plan-list/nz-card[2]/div/nz-row[2]/nz-col[2]/nz-row/nz-col[1]/app-select-department-by-product-plan"
    PRODUCTION_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-plan-list/nz-card[2]/div/nz-tabset/div/div/div[2]/app-plan-list-history/nz-row[1]/nz-col[1]/app-date-picker/nz-date-picker/div/input"
    DDL_DEPARTMENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-plan-list/nz-card[2]/div/nz-tabset/div/div/div[2]/app-plan-list-history/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-department-by-product-plan"
    DROPDOWN_CONTENT_LIST_TAG = "cdk-virtual-scroll-viewport"
    RESET_SEARCH_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-plan-list/nz-card[2]/div/nz-tabset/div/div/div[2]/app-plan-list-history/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/button"
    TAB_HISTORY = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-plan-list/nz-card[2]/div/nz-tabset/nz-tabs-nav/div/div/div[2]"
    def get_product_domestic(self):
        production_planning = self.find_element(By.XPATH,self.PRODUCTION_PLANNING)
        waiting_list = self.find_elements_from_node(production_planning,By.CLASS_NAME,self.CARD_BODY_CLASSNAME)[0]
        table_content = self.find_elements_from_node(waiting_list,By.CLASS_NAME,"ant-table-content")[0]
        table_body = self.find_elements_from_node(table_content,By.TAG_NAME,"tbody")[0]
        department_list = self.find_elements_from_node(table_body,By.TAG_NAME,"tr")
        department_list[0].click()
        car_domestic_list = CarWaitingList(self.driver,"domestic")
        return car_domestic_list
    def get_product_export(self):
        production_planning = self.find_element(By.XPATH,self.PRODUCTION_PLANNING)
        waiting_list = self.find_elements_from_node(production_planning,By.CLASS_NAME,self.CARD_BODY_CLASSNAME)[0]
        table_content = self.find_elements_from_node(waiting_list,By.CLASS_NAME,"ant-table-content")[0]
        table_body = self.find_elements_from_node(table_content,By.TAG_NAME,"tbody")[0]
        department_list = self.find_elements_from_node(table_body,By.TAG_NAME,"tr")
        department_list[1].click()
        car_export_list = CarWaitingList(self.driver, "export")
        return car_export_list
    def get_product_agp(self):
        production_planning = self.find_element(By.XPATH,self.PRODUCTION_PLANNING)
        waiting_list = self.find_elements_from_node(production_planning,By.CLASS_NAME,self.CARD_BODY_CLASSNAME)[0]
        table_content = self.find_elements_from_node(waiting_list,By.CLASS_NAME,"ant-table-content")[0]
        table_body = self.find_elements_from_node(table_content,By.TAG_NAME,"tbody")[0]
        department_list = self.find_elements_from_node(table_body,By.TAG_NAME,"tr")
        department_list[2].click()
        car_agp_list = CarWaitingList(self.driver, "agp")
        return car_agp_list
    def get_product_material(self):
        production_planning = self.find_element(By.XPATH,self.PRODUCTION_PLANNING)
        waiting_list = self.find_elements_from_node(production_planning,By.CLASS_NAME,self.CARD_BODY_CLASSNAME)[0]
        table_content = self.find_elements_from_node(waiting_list,By.CLASS_NAME,"ant-table-content")[0]
        table_body = self.find_elements_from_node(table_content,By.TAG_NAME,"tbody")[0]
        department_list = self.find_elements_from_node(table_body,By.TAG_NAME,"tr")
        department_list[3].click()
        car_material_list = CarWaitingList(self.driver, "material")
        return car_material_list

    def search_plan(self, production_date="",department_index=""):
        if production_date != "":
            production_date_element = self.find_element(By.XPATH, self.PRODUCTION_DATE_INPUT)
            self.enter_web_item_text(production_date_element, production_date)
        if department_index != "":
            dropdown_department = self.find_element(By.XPATH, self.DROPDOWNLIST_DEPARTMENT)
            self.enter_web_item_drop_down(dropdown_department, department_index)
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
                if item.text == option_value:
                    item.click()
                    break
            time.sleep(2)
    def enter_web_item_button(self,button_element):
        button_element.click()
        time.sleep(2)
    def search_plan_list(self,production_date="",department_index=-1):
        if production_date != "":
            tab_history = self.find_element(By.XPATH,self.TAB_HISTORY)
            tab_history.click()
            date_picker = self.find_element(By.XPATH,self.PRODUCTION_DATE)
            self.enter_web_item_text(date_picker,production_date)
            time.sleep(1)
        if department_index != -1:
            ddl_department = self.find_element(By.XPATH,self.DDL_DEPARTMENT)
            self.enter_web_item_drop_down(ddl_department,department_index)
            time.sleep(1)
        plan_history = self.find_element(By.TAG_NAME,"app-plan-list-history")
        tab_body = plan_history.find_element(By.TAG_NAME,"tbody")
        trs = tab_body.find_elements(By.TAG_NAME,"tr")
        return len(trs)
    def enter_reset_search_button(self):
        button = self.find_element(By.XPATH,self.RESET_SEARCH_BUTTON)
        button.click()
        time.sleep(2)

    def select_plan_in_list(self,most_recent=True):
        production_planning = self.find_element(By.XPATH, self.PRODUCTION_PLANNING)
        plan_list = self.find_elements_from_node(production_planning, By.CLASS_NAME, self.CARD_BODY_CLASSNAME)[1]
        table_content = self.find_elements_from_node(plan_list, By.CLASS_NAME, "ant-table-content")[0]
        table_body = self.find_elements_from_node(table_content, By.TAG_NAME, "tbody")[0]
        plans = table_body.find_elements(By.TAG_NAME,"tr")
        plan_index = 1
        if not most_recent  :
            plan_index = random.randint(1,len(plans)-1)
        plans[plan_index].click()
        plan_detail = ProductPlaneDetail(self.driver)
        time.sleep(2)
        return plan_detail
    def get_plan_for_make_production_list(self,production_date="",dep_name=""):
        production_planning = self.find_element(By.XPATH, self.PRODUCTION_PLANNING)
        plan_list = self.find_elements_from_node(production_planning, By.CLASS_NAME, self.CARD_BODY_CLASSNAME)[1]
        table_content = self.find_elements_from_node(plan_list, By.CLASS_NAME, "ant-table-content")[0]
        table_body = self.find_elements_from_node(table_content, By.TAG_NAME, "tbody")[0]
        trs = table_body.find_elements(By.TAG_NAME, "tr")
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME,"td")
            if len(tds) == 11:
                date_str = tds[0].text
                department_name = tds[1].text
            else:
                department_name = tds[0].text
            if date_str.find(production_date) >= 0 and department_name.find(dep_name) >= 0:
                tds[1].click()
                plan_detail = ProductPlaneDetail(self.driver)
                time.sleep(2)
                return plan_detail
        return None













