from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random
from base.base_driver import BaseDriver
from pages.CarAssetmentDetail import CarAssetmentDetail
class CarAssetmentList(BaseDriver):
    TAB_CONTENT_CLASS_NAME = "ant-tabs-nav-list"
    SEARCH_BY_ELEMENT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-all/div/app-car-assessment-filter/nz-row[1]/nz-col[1]/nz-input-group"
    SEARCH_INPUT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-all/div/app-car-assessment-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"

    DROPDOWN_MANAGEMENT_NUMBER_TAG = "nz-select-top-control"
    DROPDOWN_CONTENT_LIST_TAG = "cdk-virtual-scroll-viewport"
    TABLE_CONTENT_CLASS_NAME = "ant-table-content"

    # tab requested
    REQUESTED_INPUT_SEARCH = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-requested/div/app-car-assessment-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    REQUESTED_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-requested/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    REQUESTED_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-requested/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    REQUESTED_SALE_PIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-requested/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[1]/app-select-sale-pic"
    REQUESTED_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-requested/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[1]"





    #tab unaccessed
    UNASSESSED_INPUT_SEARCH = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-unassessed/div/app-car-assessment-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    UNASSESSED_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-unassessed/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    UNASSESSED_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-unassessed/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    UNASSESSED_SALE_PIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-unassessed/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[1]/app-select-sale-pic"
    UNASSESSED_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-unassessed/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[1]"
    UNASSESSED_RESET_BUTTON =  "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-unassessed/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[2]"

    #tab assessing
    ASSESSING_INPUT_SEARCH = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessing/div/app-car-assessment-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    ASSESSING_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessing/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    ASSESSING_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessing/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    ASSESSING_SALE_PIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessing/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[1]/app-select-sale-pic"
    ASSESSING_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessing/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[1]"

    # tab assessed
    ASSESSED_INPUT_SEARCH = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessed/div/app-car-assessment-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    ASSESSED_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessed/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    ASSESSED_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessed/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    ASSESSED_SALE_PIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessed/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[1]/app-select-sale-pic"
    ASSESSED_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-assessed/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[1]"

    # tab all
    ALL_INPUT_SEARCH = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-all/div/app-car-assessment-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    ALL_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-all/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    ALL_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-all/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    ALL_SALE_PIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-all/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[1]/app-select-sale-pic"
    ALL_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-list/nz-card/div/app-all/div/app-car-assessment-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[1]"

    def enter_dropdown_value(self,element,txt_value):
        element.click()
        time.sleep(1)
        dropdown_content = self.find_element(By.TAG_NAME, self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        for item in dropdown_items:
            if item.text == txt_value:
                item.click()
                break
        time.sleep(1)
    def enter_text_value(self,element,txt_value):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(txt_value)
        element.send_keys(Keys.ENTER)
    def enter_dropdown_value_in_filter(self,element,option_text):
        element.click();
        time.sleep(1)
        car_maker_dropdown = self.find_elements_from_node(element, By.TAG_NAME, "nz-select-top-control")
        car_maker_dropdown[0].click()
        dropdown_content = self.find_element(By.TAG_NAME, "cdk-virtual-scroll-viewport")
        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        for item in dropdown_items:
            if item.text == option_text:
                item.click()
                break
        time.sleep(1)
    def enter_text_value_in_filter(self,element,txt_value):
        element.click();
        time.sleep(1)
        txt_control = self.find_elements_from_node(element, By.TAG_NAME, "input")[0]
        txt_control.send_keys(Keys.CONTROL + "a")
        txt_control.send_keys(Keys.DELETE)
        txt_control.send_keys(txt_value)
        txt_control.send_keys(Keys.ENTER)
        time.sleep(1)
    def enter_text_range_values_in_filter(self,element,txt_values):
        values = txt_values.split("-")
        element.click()
        time.sleep(1)
        txt_controls = self.find_elements_from_node(element, By.TAG_NAME, "input")
        txt_controls[0].send_keys(Keys.CONTROL + "a")
        txt_controls[0].send_keys(Keys.DELETE)
        txt_controls[0].send_keys(values[0])
        txt_controls[0].send_keys(Keys.ENTER)
        txt_controls[1].send_keys(Keys.CONTROL + "a")
        txt_controls[1].send_keys(Keys.DELETE)
        txt_controls[1].send_keys(values[1])
        txt_controls[1].send_keys(Keys.ENTER)
        time.sleep(1)


    def enter_requested_dropdown_number(self, index):
        management_number_dropdown = self.find_element(By.TAG_NAME,self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
        management_number_dropdown.click()
        time.sleep(3)
        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        dropdown_items[index].click()
        time.sleep(3)
    def enter_requested_input_search(self,search_text):
        input_search = self.find_element(By.XPATH,self.REQUESTED_INPUT_SEARCH)
        self.enter_text_value(input_search,search_text)
    def enter_requested_dropdown_source(self,option_text):
        dropdown_source = self.find_element(By.XPATH,self.REQUESTED_DROPDOWN_SOURCE)
        self.enter_dropdown_value(dropdown_source,option_text)
    def enter_requested_input_date(self,input_date):
        input_date_control = self.find_element(By.XPATH,self.REQUESTED_INPUT_DATE)
        input_date_control.send_keys(input_date)
        time.sleep(3)
    def enter_requested_sale_pic_dropdown(self,option_text):
        drop_down = self.find_element(By.XPATH, self.REQUESTED_SALE_PIC)
        self.enter_dropdown_value(drop_down,option_text)
    def enter_unaccess_dropdown_number(self, index):
        management_number_dropdown = self.find_element(By.TAG_NAME,self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
        management_number_dropdown.click()
        time.sleep(3)
        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        dropdown_items[index].click()
        time.sleep(3)
    def enter_unassess_input_search(self,search_text):
        input_search = self.find_element(By.XPATH,self.UNASSESSED_INPUT_SEARCH)
        self.enter_text_value(input_search,search_text)
    def enter_unassess_dropdown_source(self,option_text):
        dropdown_source = self.find_element(By.XPATH,self.UNASSESSED_DROPDOWN_SOURCE)
        self.enter_dropdown_value(dropdown_source,option_text)
    def enter_unassess_input_date(self,input_date):
        input_date_control = self.find_element(By.XPATH,self.UNASSESSED_INPUT_DATE)
        input_date_control.send_keys(input_date)
        time.sleep(3)
    def enter_unassess_sale_pic_dropdown(self,option_text):
        drop_down = self.find_element(By.XPATH, self.UNASSESSED_SALE_PIC)
        self.enter_dropdown_value(drop_down,option_text)
    #assessing tab
    def enter_assessing_dropdown_number(self, index):
        management_number_dropdown = self.find_element(By.TAG_NAME,self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
        management_number_dropdown.click()
        time.sleep(3)
        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        dropdown_items[index].click()
        time.sleep(3)
    def enter_assessing_input_search(self,search_text):
        input_search = self.find_element(By.XPATH,self.ASSESSING_INPUT_SEARCH)
        self.enter_text_value(input_search,search_text)
    def enter_assessing_dropdown_source(self,option_text):
        dropdown_source = self.find_element(By.XPATH,self.ASSESSING_DROPDOWN_SOURCE)
        self.enter_dropdown_value(dropdown_source,option_text)
        time.sleep(1)
    def enter_assessing_input_date(self,input_date):
        input_date_control = self.find_element(By.XPATH,self.ASSESSING_INPUT_DATE)
        input_date_control.send_keys(input_date)
        time.sleep(3)
    def enter_assessing_sale_pic_dropdown(self,option_text):
        drop_down = self.find_element(By.XPATH, self.ASSESSING_SALE_PIC)
        self.enter_dropdown_value(drop_down,option_text)
    #assessed tab
    def enter_assessed_dropdown_number(self, index):
        management_number_dropdown = self.find_element(By.TAG_NAME,self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
        management_number_dropdown.click()
        time.sleep(3)
        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        dropdown_items[index].click()
        time.sleep(3)
    def enter_assessed_input_search(self,search_text):
        input_search = self.find_element(By.XPATH,self.ASSESSED_INPUT_SEARCH)
        self.enter_text_value(input_search,search_text)
    def enter_assessed_dropdown_source(self,option_text):
        dropdown_source = self.find_element(By.XPATH,self.ASSESSED_DROPDOWN_SOURCE)
        self.enter_dropdown_value(dropdown_source,option_text)
    def enter_assessed_input_date(self,input_date):
        input_date_control = self.find_element(By.XPATH,self.ASSESSED_INPUT_DATE)
        input_date_control.send_keys(input_date)
        time.sleep(3)
    def enter_assessed_sale_pic_dropdown(self,option_text):
        drop_down = self.find_element(By.XPATH, self.ASSESSED_SALE_PIC)
        self.enter_dropdown_value(drop_down,option_text)
    # tab all
    def enter_all_dropdown_number(self, index):
        management_number_dropdown = self.find_element(By.TAG_NAME,self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
        management_number_dropdown.click()
        time.sleep(3)
        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        dropdown_items[index].click()
        time.sleep(3)
    def enter_all_input_search(self,search_text):
        input_search = self.find_element(By.XPATH,self.ALL_INPUT_SEARCH)
        self.enter_text_value(input_search,search_text)
    def enter_all_dropdown_source(self,option_text):
        dropdown_source = self.find_element(By.XPATH,self.ALL_DROPDOWN_SOURCE)
        self.enter_dropdown_value(dropdown_source,option_text)
        dropdown_source.click()
    def enter_all_input_date(self,input_date):
        input_date_control = self.find_element(By.XPATH,self.ALL_INPUT_DATE)
        input_date_control.send_keys(input_date)
        time.sleep(3)
    def enter_all_sale_pic_dropdown(self,option_text):
        drop_down = self.find_element(By.XPATH, self.ALL_SALE_PIC)
        self.enter_dropdown_value(drop_down,option_text)
    def requested_search(self,management_number=-1,
                          text_search= "",
                          dropdown_source = "",
                          input_date="",
                          dropdown_person = "" ):
        if management_number != -1:
            self.enter_requested_dropdown_number(management_number)
        if text_search != "":
            self.enter_requested_input_search(text_search)
        if dropdown_source != -1:
            self.enter_requested_dropdown_source(dropdown_source)
        if input_date != "":
            self.enter_requested_input_date(input_date)
        if dropdown_person != "":
            self.enter_requested_sale_pic_dropdown(dropdown_person)
        table_content = self.find_element(By.CLASS_NAME,self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME,"tr")
        return len(elements)



    def unassessed_search(self,management_number=-1,
                          text_search= "",
                          dropdown_source="",
                          input_date="",
                          dropdown_person = "" ):
        if management_number != -1:
            self.enter_unaccess_dropdown_number(management_number)
        if text_search != "":
            self.enter_unassess_input_search(text_search)
        if dropdown_source != "":
            self.enter_unassess_dropdown_source(dropdown_source)
        if input_date != "":
            self.enter_unassess_input_date(input_date)
        if dropdown_person != "":
            self.enter_unassess_sale_pic_dropdown(dropdown_person)
        table_content = self.find_element(By.CLASS_NAME,self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME,"tr")
        return len(elements)
    def reset_unassessed_search(self):
        button = self.find_element(By.XPATH,self.UNASSESSED_RESET_BUTTON)
        button.click()

    def assessing_search(self,management_number=-1,
                          text_search= "",
                          dropdown_source="",
                          input_date="",
                          dropdown_person = "" ):
        if management_number != -1:
            self.enter_assessing_dropdown_number(management_number)
        if text_search != "":
            self.enter_assessing_input_search(text_search)
        if dropdown_source != "":
            self.enter_assessing_dropdown_source(dropdown_source)
        if input_date != "":
            self.enter_assessing_input_date(input_date)
        if dropdown_person != "":
            self.enter_assessing_sale_pic_dropdown(dropdown_person)

    def assessed_search(self,management_number=-1,
                          text_search= "",
                          dropdown_source="",
                          input_date="",
                          dropdown_person = "" ):
        if management_number != -1:
            self.enter_assessed_dropdown_number(management_number)
        if text_search != "":
            self.enter_assessed_input_search(text_search)
        if dropdown_source != "":
            self.enter_assessed_dropdown_source(dropdown_source)
        if input_date != "":
            self.enter_assessed_input_date(input_date)
        if dropdown_person != "":
            self.enter_assessed_sale_pic_dropdown(dropdown_person)

    def all_search(self,management_number=-1,
                          text_search= "",
                          dropdown_source="",
                          input_date="",
                          dropdown_person = "" ):
        if management_number != -1:
            self.enter_all_dropdown_number(management_number)
        if text_search != "":
            self.enter_all_input_search(text_search)
        if dropdown_source != "":
            self.enter_all_dropdown_source(dropdown_source)
        if input_date != "":
            self.enter_all_input_date(input_date)
        if dropdown_person != "":
            self.enter_all_sale_pic_dropdown(dropdown_person)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)
    def requested_search_using_filter(self,
                                       management_number = "",
                                       car_maker = "",
                                       car_name = "",
                                       model = "",
                                       chassis_number = "",
                                       mile_age = "",
                                       displacement= "",
                                       sale_pic = "",
                                       supplier = "",
                                       input_date = "",
                                       source = ""
                                       ):
        filter_button = self.find_element(By.XPATH,self.REQUESTED_FILTER_BUTTON)
        filter_button.click()
        time.sleep(3)
        dialog_content = self.find_element(By.TAG_NAME,"app-filter-popup")
        items = self.find_elements_from_node(dialog_content,By.XPATH,"./*")
        if management_number != "":
            self.enter_text_value_in_filter(items[0],management_number)
        if car_maker != "":
            self.enter_dropdown_value_in_filter(items[1],car_maker)
        if car_name != "":
            self.enter_dropdown_value_in_filter(items[2],car_name)
        if model != 0:
            self.enter_dropdown_value_in_filter(items[3],model)
        if chassis_number != "":
            items[4].click()
            self.enter_text_value_in_filter(items[4],chassis_number)
        if mile_age != "":
            self.enter_text_range_values_in_filter(items[5],mile_age)
        if displacement != "":
            self.enter_text_range_values_in_filter(items[6],displacement)
        if sale_pic != "" :
            self.enter_dropdown_value_in_filter(items[7],sale_pic)
        if supplier != "" :
            self.enter_dropdown_value_in_filter(items[8],supplier)
        if input_date != "":
            self.enter_text_range_values_in_filter(items[9],input_date)
        if source != "" :
            self.enter_dropdown_value_in_filter(items[10],source)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        buttons = self.find_elements_from_node(footer_area,By.TAG_NAME,"button")
        buttons[1].click()
        time.sleep(3)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)

    def unassessed_search_using_filter(self,
                                       management_number = "",
                                       car_maker = "",
                                       car_name = "",
                                       model = "",
                                       chassis_number = "",
                                       mile_age = "",
                                       displacement= "",
                                       sale_pic = "",
                                       supplier = "",
                                       input_date = "",
                                       source = ""
                                       ):
        filter_button = self.find_element(By.XPATH,self.UNASSESSED_FILTER_BUTTON)
        self.driver.execute_script("arguments[0].click();", filter_button)
        time.sleep(3)
        dialog_content = self.find_element(By.TAG_NAME,"app-filter-popup")
        items = self.find_elements_from_node(dialog_content,By.XPATH,"./*")
        if management_number != "":
            self.enter_text_value_in_filter(items[0],management_number)
        if car_maker != "":
            self.enter_dropdown_value_in_filter(items[1],car_maker)
        if car_name != "":
            self.enter_dropdown_value_in_filter(items[2],car_name)
        if model != "":
            self.enter_dropdown_value_in_filter(items[3],model)
        if chassis_number != "":
            self.enter_text_value_in_filter(items[4],chassis_number)
        if mile_age != "":
            self.enter_text_range_values_in_filter(items[5],mile_age)
        if displacement != "":
            self.enter_text_range_values_in_filter(items[6],displacement)
        if sale_pic != "" :
            self.enter_dropdown_value_in_filter(items[7],sale_pic)
        if supplier != "" :
            self.enter_dropdown_value_in_filter(items[8],supplier)
        if input_date != "":
            self.enter_text_range_values_in_filter(input_date)
        if source != "" :
            self.enter_dropdown_value_in_filter(items[10],source)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        buttons = self.find_elements_from_node(footer_area,By.TAG_NAME,"button")
        buttons[1].click()
        time.sleep(3)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)
    def assessing_search_using_filter(self,
                                       management_number = -1,
                                       car_maker = "",
                                       car_name = "",
                                       model = "",
                                       chassis_number = "",
                                       mile_age = "",
                                       displacement= "",
                                       sale_pic = "",
                                       supplier = "",
                                       input_date = "",
                                       source = ""
                                       ):
        filter_button = self.find_element(By.XPATH,self.ASSESSING_FILTER_BUTTON)
        filter_button.click()
        time.sleep(3)
        dialog_content = self.find_element(By.TAG_NAME,"app-filter-popup")
        items = self.find_elements_from_node(dialog_content,By.XPATH,"./*")
        if management_number != "":
            self.enter_text_value_in_filter(items[0],management_number)
        if car_maker != "":
            self.enter_dropdown_value_in_filter(items[1],car_maker)
        if car_name != "":
            self.enter_dropdown_value_in_filter(items[2],car_name)
        if model != "":
            self.enter_dropdown_value_in_filter(items[3],model)
        if chassis_number != "":
            self.enter_text_value_in_filter(items[4],chassis_number)
        if mile_age != "":
            self.enter_text_range_values_in_filter(items[5],mile_age)
        if displacement != "":
            self.enter_text_range_values_in_filter(items[6],displacement)
        if sale_pic != "":
            self.enter_dropdown_value_in_filter(items[7],sale_pic)
        if supplier != "" :
            self.enter_dropdown_value_in_filter(items[8],supplier)
        if input_date != "":
            self.enter_text_range_values_in_filter(items[9],input_date)
        if source != "" :
            self.enter_dropdown_value_in_filter(items[10],source)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        buttons = self.find_elements_from_node(footer_area,By.TAG_NAME,"button")
        buttons[1].click()
        time.sleep(5)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)
    def assessed_search_using_filter(self,
                                       management_number = "",
                                       car_maker = "",
                                       car_name = "",
                                       model = "",
                                       chassis_number = "",
                                       mile_age = "",
                                       displacement= "",
                                       sale_pic = "",
                                       supplier = "",
                                       input_date = "",
                                       source = ""
                                       ):
        filter_button = self.find_element(By.XPATH,self.ASSESSED_FILTER_BUTTON)
        filter_button.click()
        time.sleep(3)
        dialog_content = self.find_element(By.TAG_NAME,"app-filter-popup")
        items = self.find_elements_from_node(dialog_content,By.XPATH,"./*")
        if management_number != "":
            self.enter_text_value_in_filter(items[0],management_number)
        if car_maker != "":
            self.enter_dropdown_value_in_filter(items[1],car_maker)
        if car_name != "":
            self.enter_dropdown_value_in_filter(items[2],car_name)
        if model != "":
            self.enter_dropdown_value_in_filter(items[3],model)
        if chassis_number != "":
            self.enter_text_value_in_filter(items[4],chassis_number)
        if mile_age != "":
            self.enter_text_range_values_in_filter(items[5],mile_age)
        if displacement != "":
            self.enter_text_range_values_in_filter(items[6],displacement)
        if sale_pic != "" :
            self.enter_dropdown_value_in_filter(items[7],sale_pic)
        if supplier != "" :
            self.enter_dropdown_value_in_filter(items[8],supplier)
        if input_date != "":
            self.enter_text_range_values_in_filter(items[9],input_date)
        if source != "" :
            self.enter_dropdown_value_in_filter(items[10],source)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        buttons = self.find_elements_from_node(footer_area,By.TAG_NAME,"button")
        buttons[1].click()
        time.sleep(5)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)
    def all_search_using_filter(self,
                                       management_number = "",
                                       car_maker = "",
                                       car_name = "",
                                       model = "",
                                       chassis_number = "",
                                       mile_age = "",
                                       displacement= "",
                                       sale_pic = "",
                                       supplier = "",
                                       input_date = "",
                                       assetment_status = "",
                                       source = ""
                                       ):
        filter_button = self.find_element(By.XPATH,self.ALL_FILTER_BUTTON)
        filter_button.click()
        time.sleep(3)
        dialog_content = self.find_element(By.TAG_NAME,"app-filter-popup")
        items = self.find_elements_from_node(dialog_content,By.XPATH,"./*")
        if management_number != "":
            self.enter_text_value_in_filter(items[0],management_number)
        if car_maker != "":
            self.enter_dropdown_value_in_filter(items[1],car_maker)
        if car_name != "":
            self.enter_dropdown_value_in_filter(items[2],car_name)
        if model != "":
            self.enter_dropdown_value_in_filter(items[3],model)
        if chassis_number != "":
            self.enter_text_value_in_filter(items[4],chassis_number)
        if mile_age != "":
            self.enter_text_range_values_in_filter(items[5],mile_age)
        if displacement != "":
            self.enter_text_range_values_in_filter(items[6],displacement)
        if sale_pic != "" :
            self.enter_dropdown_value_in_filter(items[7],sale_pic)
        if supplier >= 0 :
            self.enter_dropdown_value_in_filter(items[8],supplier)
        if input_date != "":
            self.enter_text_range_values_in_filter(items[9],input_date)
        if assetment_status != "":
            self.enter_dropdown_value_in_filter(items[10],assetment_status)
        if source != "" :
            self.enter_dropdown_value_in_filter(items[11],source)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        buttons = self.find_elements_from_node(footer_area,By.TAG_NAME,"button")
        buttons[1].click()
        time.sleep(5)
    def __init__(self,driver):
        super().__init__(driver)
    def select_assetment_list_tab(self,tab_index):
        tab_content = self.find_element(By.CLASS_NAME,self.TAB_CONTENT_CLASS_NAME)
        tabs = self.find_elements_from_node(tab_content,By.TAG_NAME,"div")
        print(len(tabs))
        tabs[tab_index].click()
    def get_select_search_element(self):
        return self.find_element(By.XPATH,self.SEARCH_BY_ELEMENT_FIELD)

    def click_select_search(self):
        time.sleep(2)
        elem = self.find_elements(By.TAG_NAME,'nz-select-search')[0]
        self.driver.execute_script("arguments[0].click();", elem)
    def get_search_option_index(self,index):
        parent_node = self.find_element(By.CLASS_NAME,'cdk-virtual-scroll-content-wrapper')
        option_nodes = parent_node.find_elements(By.TAG_NAME,"nz-option-item")
        return option_nodes[index]
    def select_search_option(self,index):
        selected_node = self.get_search_option_index(index)
        selected_node.click()
    def get_search_input(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.SEARCH_INPUT_FIELD)
    def do_search(self,text_to_find):
        time.sleep(1)
        elements = self.driver.find_elements(By.TAG_NAME,'nz-input-group')
        element = elements[0]
        input_texts = element.find_elements(By.TAG_NAME,'input')
        input_text = input_texts[1]
        self.driver.execute_script("arguments[0].click();", input_text)
        input_text.send_keys(Keys.CONTROL + "a")
        input_text.send_keys(Keys.BACK_SPACE)
        input_text.send_keys(text_to_find)
        time.sleep(2)
        input_text.send_keys(Keys.ENTER)
        all_cars_assetment = self.find_element(By.TAG_NAME, "app-footer-template")
        trs = all_cars_assetment.find_elements(By.TAG_NAME, "span")
        txt = trs[1].text[0]
        num_record = int(txt)
        if num_record == 0:
            return False
        else:
            return True

    def get_car_assetment_detail(self,chassis_number=""):
        found = False
        all_cars_assetment = self.find_element(By.TAG_NAME,"tbody")
        trs = all_cars_assetment.find_elements(By.TAG_NAME,"tr")
        num_car_assetment = len(trs)
        if num_car_assetment <= 2:
            return None
        if chassis_number == "":
            index = random.randint(1,num_car_assetment-1)
            tds = trs[index].find_elements(By.TAG_NAME,"td")
            self.driver.execute_script("arguments[0].click();", tds[4])

        else:
            for tr in trs:
                tds = tr.find_elements(By.TAG_NAME,"td")
                if tds[4].text == chassis_number:
                    self.driver.execute_script("arguments[0].click();", tds[4])
                    found = True
                    break


        time.sleep(2)
        if found == True:
            car_assetment_detail_obj = CarAssetmentDetail(self.driver)
            return car_assetment_detail_obj
        return None
    def enter_unassetment_tab(self):
        parent_element = self.find_element(By.CLASS_NAME,"ant-tabs-nav-list")
        tabs_elements = parent_element.find_elements(By.CLASS_NAME,"ant-tabs-tab-btn")
        tabs_elements[0].click()
        time.sleep(3)
    def request_assetment(self):
        chkboxes = self.find_elements(By.CSS_SELECTOR,"input[type='checkbox']");
        chk_len = len(chkboxes)
        for i in range(6):
            ran_idx = random.randint(1,chk_len-1)
            chkboxes[ran_idx].click()
        panel_buttons = self.find_elements(By.TAG_NAME,"nz-table-title-footer")
        buttons = panel_buttons[0].find_elements(By.TAG_NAME,"button")
        buttons[0].click()
        time.sleep(3)
        div_modal_dialog = self.find_element(By.TAG_NAME,"app-popup-request-department-assess")
        chk_boxes = div_modal_dialog.find_elements(By.CSS_SELECTOR,"input[type='checkbox']");
        rnd_value = random.randint(0,1)
        if rnd_value == 1:
            chk_boxes[5].click()
        rnd_value = random.randint(0, 1)
        if rnd_value == 1:
            chk_boxes[6].click()
        text_memo = div_modal_dialog.find_element(By.TAG_NAME,'textarea')
        text_memo.click()
        text_memo.send_keys("automation_test")
        text_memo.send_keys(Keys.ENTER)
        div_footer = self.driver.find_elements(By.CSS_SELECTOR,"div[nz-modal-footer='']")
        buttons = div_footer[0].find_elements(By.TAG_NAME,"button")
        buttons[1].click()
        time.sleep(2)
    def do_batch_accessetment(self,number_of_cars,notes):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        if number_of_cars > len(elements):
            number_of_cars = len(elements)
        rand_nums = random.sample(range(2,len(elements)),number_of_cars)
        for rand_idx in rand_nums:
            tds = elements[rand_idx].find_elements(By.TAG_NAME,"td")
            tds[0].click()
        title_footer = self.find_element(By.TAG_NAME,"nz-table-title-footer")
        buttons = title_footer.find_elements(By.TAG_NAME,"button")
        buttons[0].click()
        time.sleep(2)
        dialog = self.find_element(By.TAG_NAME,"app-popup-request-department-assess")
        child_divs = dialog.find_elements(By.XPATH, "./div")

        checkboxes_department = child_divs[0].find_elements(By.TAG_NAME,"nz-checkbox-wrapper")
        checkboxes_department[4].click()
        p2_checkboxes = child_divs[1].find_elements(By.TAG_NAME,"input")
        p2_checkboxes[0].click()
        time.sleep(1)
        p2_checkboxes[1].click()
        txt_area = child_divs[2].find_element(By.TAG_NAME,"textarea")
        txt_area.send_keys(Keys.CONTROL + "a")
        txt_area.send_keys(Keys.DELETE)
        txt_area.send_keys(notes)
        txt_area.send_keys(Keys.ENTER)
        footer = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = footer.find_elements(By.TAG_NAME,"button")
        buttons[1].click()
    def do_purchase_batch(self,number_of_cars):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        if number_of_cars > len(elements):
            number_of_cars = len(elements)
        rand_nums = random.sample(range(2, len(elements)), number_of_cars)
        for rand_idx in rand_nums:
            tds = elements[rand_idx].find_elements(By.TAG_NAME, "td")
            tds[0].click()
        title_footer = self.find_element(By.TAG_NAME, "nz-table-title-footer")
        buttons = title_footer.find_elements(By.TAG_NAME, "button")
        buttons[2].click()
    def get_all_chasis_number_in_list(self):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME,"tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        lst_chasis_number = []
        for row in rows:
            tds = row.find_elements(By.TAG_NAME,"td")
            if tds[4].text != "":
                lst_chasis_number.append(tds[4].text)
        return lst_chasis_number
    def get_all_car_name_in_list(self):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        lst_car_name = []
        for row in rows:
            tds = row.find_elements(By.TAG_NAME, "td")
            if tds[2].text != "":
                lst_car_name.append(tds[2].text)
        return lst_car_name
    def get_all_models_in_list(self):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        lst_models = []
        for row in rows:
            tds = row.find_elements(By.TAG_NAME, "td")
            if tds[3].text != "":
                lst_models.append(tds[3].text)
        return lst_models





    def do_unpurchase_batch(self,number_of_cars):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        if number_of_cars > len(elements):
            number_of_cars = len(elements)
        rand_nums = random.sample(range(2, len(elements)), number_of_cars)
        for rand_idx in rand_nums:
            tds = elements[rand_idx].find_elements(By.TAG_NAME, "td")
            tds[0].click()
        title_footer = self.find_element(By.TAG_NAME, "nz-table-title-footer")
        buttons = title_footer.find_elements(By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(1)
        unpurchase_dialog = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        divs = unpurchase_dialog.find_elements(By.XPATH, "./div")
        ddl_sale_pic   = divs[1].find_element(By.TAG_NAME,"app-select-sale-pic")
        ddl_sale_pic.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.TAG_NAME,"cdk-virtual-scroll-viewport")
        items = dropdown_content.find_elements(By.TAG_NAME,"nz-option-item")
        items[1].click()
        table_content = divs[1].find_element(By.TAG_NAME,"tbody")
        trs = table_content.find_elements(By.TAG_NAME,"tr")
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME,"td")
            ddl_reason = tds[5].find_element(By.TAG_NAME,"app-select-option-value")
            ddl_reason.click()
            dropdown_content = self.find_element(By.TAG_NAME, "cdk-virtual-scroll-viewport")
            items = dropdown_content.find_elements(By.TAG_NAME, "nz-option-item")
            index = random.randint(0,6)
            items[index].click()
            if index == 0 or index == 1:
                txt_price_lost = tds[6].find_element(By.TAG_NAME, "input")
                txt_price_lost.send_keys(Keys.CONTROL + "a")
                txt_price_lost.send_keys(Keys.DELETE)
                price_lot = random.randint(0,100000)
                txt_price_lost.send_keys(str(price_lot))
                txt_price_lost.send_keys(Keys.ENTER)
        btn_apply = divs[2].find_elements(By.TAG_NAME, "button")[1]
        btn_apply.click()
    def get_car_from_chasis_number(self,chassis_no):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        for element in elements:
            tds = element.find_elements(By.TAG_NAME,"td")
            if len(tds) > 6 and tds[5].text == chassis_no:
                element.click()
                break
        car_assesment_detail = CarAssetmentDetail(self.driver)
        return car_assesment_detail

    def do_purchase(self,number_of_cars):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        if number_of_cars > len(elements):
            number_of_cars = len(elements)
        rand_nums = random.sample(range(2, len(elements)), number_of_cars)
        for rand_idx in rand_nums:
            tds = elements[rand_idx].find_elements(By.TAG_NAME, "td")
            tds[0].click()
        title_footer = self.find_element(By.TAG_NAME, "nz-table-title-footer")
        buttons = title_footer.find_elements(By.TAG_NAME, "button")
        buttons[2].click()
        time.sleep(1)
        purchase_dialog = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        divs = purchase_dialog.find_elements(By.XPATH, "./div")
        ddl_sale_pic = divs[1].find_element(By.TAG_NAME, "app-select-sale-pic")
        ddl_sale_pic.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.TAG_NAME, "cdk-virtual-scroll-viewport")
        items = dropdown_content.find_elements(By.TAG_NAME, "nz-option-item")
        items[1].click()
        table_content = divs[1].find_element(By.TAG_NAME, "tbody")
        trs = table_content.find_elements(By.TAG_NAME, "tr")
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME, "td")
            txt_purchase = tds[5].find_element(By.TAG_NAME, "input")
            txt_purchase.send_keys(Keys.CONTROL + "a")
            txt_purchase.send_keys(Keys.DELETE)
            price_purchase = random.randint(0, 100000)
            txt_purchase.send_keys(str(price_purchase))
            txt_purchase.send_keys(Keys.ENTER)

            txt_offer = tds[6].find_element(By.TAG_NAME, "input")
            txt_offer.send_keys(Keys.CONTROL + "a")
            txt_offer.send_keys(Keys.DELETE)
            price_offer = random.randint(0, 100000)
            txt_offer.send_keys(str(price_offer))
            txt_offer.send_keys(Keys.ENTER)


        btn_apply = divs[2].find_elements(By.TAG_NAME, "button")[1]
        btn_apply.click()




























