from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from base.base_driver import BaseDriver
from pages.PartRegistration import PartRegistration


class PartsManagement(BaseDriver):
    DROPDOWN_CONTENT_LIST_TAG = "cdk-virtual-scroll-viewport"
    TABLE_CONTENT_CLASS_NAME  = "ant-table-content"
    BUTTON_ADD_PART = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-row/nz-col/nz-space/div/button"
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
        for item in dropdown_items:
            if item.text == option_value:
                item.click()
                break

        time.sleep(2)
    def enter_web_item_button(self,button_element):
        button_element.click()
        time.sleep(2)
    def enter_text_in_modal_dialog(self, web_element,text_value):
        web_element.click();
        time.sleep(3)
        txt_element = self.find_elements_from_node(web_element, By.TAG_NAME, "input")[0]
        txt_element.send_keys(Keys.CONTROL + "a")
        txt_element.send_keys(Keys.DELETE)
        txt_element.send_keys(text_value)
        txt_element.send_keys(Keys.ENTER)
        time.sleep(2)
    def enter_dropdown_in_modal_dialog(self,web_element,option_value):
        web_element.click();
        time.sleep(3)
        car_maker_dropdown = self.find_elements_from_node(web_element, By.TAG_NAME, "nz-select-top-control")
        car_maker_dropdown[0].click()
        time.sleep(3)
        dropdown_content = self.find_element(By.TAG_NAME, "cdk-virtual-scroll-viewport")
        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        for item in dropdown_items:
            if item.text == option_value:
                item.click()
                break
        time.sleep(2)
    def enter_dropdown_in_modal(self,web_element,option_value):
        web_element.click();
        time.sleep(3)
        dropdown_content = self.find_element(By.TAG_NAME, "cdk-virtual-scroll-viewport")
        dropdown_items = dropdown_content.find_elements(By.TAG_NAME, "nz-option-item")
        for item in dropdown_items:
            if item.text == option_value:
                item.click()
                break



    def __init__(self,driver):
        super().__init__(driver=driver)
        time.sleep(2)
        tab_header_content = self.find_element(By.CLASS_NAME,"ant-tabs-nav-list")
        self.tabs = tab_header_content.find_elements(By.XPATH, "./div")
    def get_all_chasis_number_in_list(self):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME,"tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        lst_chasis_number = []
        for row in rows:
            tds = row.find_elements(By.TAG_NAME,"td")
            if tds[4].text != "":
                lst_chasis_number.append(tds[5].text)
        return lst_chasis_number
    def get_removed_tab(self):
        self.tabs[0].click()
        self.TAB_NAME = "removed"
    def get_produced_tab(self):
        self.tabs[1].click()
        self.TAB_NAME = "produced-part"
    def get_standby_tab(self):
        self.tabs[2].click()
        self.TAB_NAME = "in-production-part"
    def get_inproduction_part_tab(self):
        self.tabs[3].click()
        self.TAB_NAME = "standby-part"
    def get_request_number_dropdown(self):
        if self.TAB_NAME == "standby-part":
            element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-part-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[1]/nz-select"
        else:
            element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-product-part-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[1]/nz-select"
        request_number_ddl = self.find_element(By.XPATH,element_url)
        return request_number_ddl
    def get_txt_search(self):
        if self.TAB_NAME == "removed" or self.TAB_NAME == "produced-part":
            element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME +  "/nz-card/div/app-product-part-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
        else :
            element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-part-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
        txt_search = self.find_element(By.XPATH, element_url)
        return txt_search
    def get_priority_dropdown(self):
        element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-product-part-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
        priority_ddl = self.find_element(By.XPATH, element_url)
        return priority_ddl
    def get_production_flow_dropdown(self):
        element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-product-part-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-select-option-value"
        production_flow_ddl = self.find_element(By.XPATH, element_url)
        return production_flow_ddl
    def get_reset_button(self):
        if self.TAB_NAME == "standby-part":
            element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-part-filter/nz-row[1]/nz-col[2]/nz-row/nz-col/nz-row/nz-col[2]/button[2]"
        else:
            element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-product-part-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[2]"
        button_reset = self.find_element(By.XPATH,element_url)
        return button_reset
    def reset_search(self):
        button = self.get_reset_button()
        button.click()
        time.sleep(3)
    def get_production_status_dropdown(self):
        element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-product-part-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[1]/app-select-option-value"
        production_status_ddl = self.find_element(By.XPATH, element_url)
        return production_status_ddl
    def get_production_part_category_dropdown(self):
        element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME +  "/nz-card/div/app-part-filter/nz-row[1]/nz-col[2]/nz-row/nz-col/nz-row/nz-col[1]/app-select-option-value"
        part_category_ddl = self.find_element(By.XPATH, element_url)
        return part_category_ddl
    def get_filter_button(self):
        if self.TAB_NAME == "removed" or self.TAB_NAME == "produced-part":
            element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-product-part-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[1]"
        else:
            element_url = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-list/nz-card/div/app-" + self.TAB_NAME + "/nz-card/div/app-part-filter/nz-row[1]/nz-col[2]/nz-row/nz-col/nz-row/nz-col[2]/button[1]"
        filter_button = self.find_element(By.XPATH,element_url)
        return filter_button
    def search_part(self,request_num="",
                    search_text = "" ,
                    priority = "",
                    production_flow="",
                    production_status="",
                    part_category=""):
        if request_num != "":
            ddl_request_num = self.get_request_number_dropdown()
            self.enter_web_item_drop_down(ddl_request_num,request_num)
        if search_text != "":
            txt_search = self.get_txt_search()
            self.enter_web_item_text(txt_search,search_text)
        if priority != "":
            ddl_priority = self.get_priority_dropdown()
            self.enter_web_item_drop_down(ddl_priority,priority)
        if production_flow != "":
            ddl_production_flow = self.get_production_flow_dropdown()
            self.enter_web_item_drop_down(ddl_production_flow,production_flow)
        if production_status != "":
            ddl_status = self.get_production_status_dropdown()
            self.enter_web_item_drop_down(ddl_status,production_status)
        if part_category != "":
            ddl_part_category = self.get_production_part_category_dropdown()
            self.enter_web_item_drop_down(ddl_part_category,part_category)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        return len(rows)

    def search_parts_using_filter_button_tab_remove_produced(self,
                                                   management_num="",
                                                   chasis_num= "",
                                                   priority="",
                                                   product_flow="",
                                                   product_status="",
                                                   picup_request_num=""):
        filter_button = self.get_filter_button()
        self.driver.execute_script("arguments[0].click();", filter_button)
        time.sleep(3)
        dialog_content = self.find_element(By.TAG_NAME, "app-part-filter-popup")
        items = self.find_elements_from_node(dialog_content, By.XPATH, "./*")
        if management_num != "":
            self.enter_text_in_modal_dialog(items[0], management_num)
        if chasis_num != "":
            self.enter_text_in_modal_dialog(items[1],chasis_num)
        if priority != "":
            self.enter_dropdown_in_modal_dialog(items[2],priority)
        if product_flow != "":
            self.enter_dropdown_in_modal_dialog(items[3],product_flow)
        if product_status != "":
            self.enter_dropdown_in_modal_dialog(items[4], product_status)
        if picup_request_num != "":
            self.enter_text_in_modal_dialog(items[5], picup_request_num)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        buttons = self.find_elements_from_node(footer_area, By.TAG_NAME, "button")
        buttons[2].click()
        time.sleep(5)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        return len(rows)
    def search_parts_using_filter_button_tab_stanby_and_in_production(self,
                                                   part_code="",
                                                   part_name= "",
                                                   genuine_part_num="",
                                                   chasis_num = "",
                                                   part_category="",
                                                   part_type=""):
        filter_button = self.get_filter_button()
        self.driver.execute_script("arguments[0].click();", filter_button)
        time.sleep(3)
        dialog_content = self.find_element(By.TAG_NAME, "app-filter-popup")
        items = self.find_elements_from_node(dialog_content, By.XPATH, "./*")
        if part_code != "":
            self.enter_text_in_modal_dialog(items[0], part_code)
        if part_name != "":
            self.enter_text_in_modal_dialog(items[1],part_name)
        if genuine_part_num != "":
            self.enter_text_in_modal_dialog(items[2],genuine_part_num)
        if chasis_num != "":
            self.enter_text_in_modal_dialog(items[3],chasis_num)
        if part_category != "":
            self.enter_dropdown_in_modal(items[4],part_category)
        if part_type != "":
            self.enter_dropdown_in_modal(items[5], part_type)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        buttons = self.find_elements_from_node(footer_area, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(5)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        return len(rows)
    def add_new_part(self):
        btn_add_part = self.find_element(By.XPATH,self.BUTTON_ADD_PART)
        btn_add_part.click()
        time.sleep(2)
        part_register = PartRegistration(self.driver)
        return part_register






















