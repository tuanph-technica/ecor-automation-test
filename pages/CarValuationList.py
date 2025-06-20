from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from base.base_driver import BaseDriver
from pages.CarOnValuation import CarOnValuation
from pages.CarValuationDetail import CarValuationDetail
from selenium.webdriver.support.ui import Select


class CarValuationList(BaseDriver):
    TABLE_CONTENT_CLASS_NAME = "ant-table-content"
    TAB_CONTENT_CLASS_NAME = "ant-tabs-nav-list"

    DROPDOWN_MANAGEMENT_NUMBER_TAG = "nz-select-top-control"
    DROPDOWN_CONTENT_LIST_TAG = "cdk-virtual-scroll-viewport"

    # tab requested
    REQUESTED_SEARCH_TEXT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-requested/div/app-valuation-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    REQUESTED_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-requested/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    REQUESTED_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-requested/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    REQUESTED_DROPDOWN_PICUPTYPE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-requested/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-option-value"
    REQUESTED_DROPDOWN_SALEPIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-requested/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[1]/app-select-sale-pic"
    REQUESTED_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-requested/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[1]"
    REQUESTED_RESET_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-requested/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[2]"
    # tab unvalueated
    UNVALUATE_SEARCH_TEXT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-un-valuated/div/app-valuation-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    UNVALUATE_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-requested/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    UNVALUATE_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-un-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    UNVALUATE_DROPDOWN_PICUPTYPE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-un-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-option-value"
    UNVALUATE_DROPDOWN_SALEPIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-un-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[1]/app-select-sale-pic"
    UNVALUATE_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-un-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[1]"

    #tab valuating
    VALUATING_SEARCH_TEXT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuating/div/app-valuation-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    VALUATING_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuating/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    VALUATING_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuating/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    VALUATING_DROPDOWN_PICUPTYPE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuating/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-option-value"
    VALUATING_DROPDOWN_SALEPIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuating/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[1]/app-select-sale-pic"
    VALUATING_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuating/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[1]"
    VALUATING_RESET_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuating/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[2]"
    # tab valuated
    VALUATED_SEARCH_TEXT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuated/div/app-valuation-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    VALUATED_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    VALUATED_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    VALUATED_DROPDOWN_PICUPTYPE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-option-value"
    VALUATED_DROPDOWN_SALEPIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[1]/app-select-sale-pic"
    VALUATED_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[1]"
    VALUATED_RESET_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-valuated/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[2]"


    # tab assorted
    ASSORTED_SEARCH_TEXT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-assorted/div/app-valuation-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    ASSORTED_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-assorted/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    ASSORTED_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-assorted/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    ASSORTED_DROPDOWN_PICUPTYPE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-assorted/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-option-value"
    ASSORTED_DROPDOWN_SALEPIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-assorted/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[1]/app-select-sale-pic"
    ASSORTED_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-assorted/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[1]"
    ASSORTED_RESET_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-assorted/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[2]"


    # tab assorted
    ALL_SEARCH_TEXT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-all/div/app-valuation-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    ALL_DROPDOWN_SOURCE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-all/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    ALL_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-all/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-date-picker/nz-date-picker/div/input"
    ALL_VALIDATION_STATUS = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-all/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-select-option-value"
    ALL_DROPDOWN_PICUPTYPE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-all/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/app-select-option-value"
    ALL_DROPDOWN_SALEPIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-all/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[1]/app-select-sale-pic"
    ALL_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-list/nz-card/div/app-all/div/app-valuation-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/nz-row/nz-col[2]/button[1]"
    def enter_web_item_text(self, text_element, text_value):
         text_element.send_keys(Keys.CLEAR)
         text_element.send_keys(text_value)
         text_element.send_keys(Keys.ENTER)
         time.sleep(2)
    def enter_web_item_drop_down(self,dropdown_element,option_value):
        dropdown_element.click()
        time.sleep(1)
        dropdown_content = self.find_element(By.TAG_NAME, self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        if isinstance(option_value,int):
            dropdown_items[option_value].click()
        else:
            for item in dropdown_items:
                if item.text == option_value:
                    item.click()
                    break

        time.sleep(1)
    def enter_web_item_button(self,button_element):
        button_element.click()
        time.sleep(2)




    def select_valuation_list_tab(self,tab_index):
        tab_content = self.find_element(By.CLASS_NAME,self.TAB_CONTENT_CLASS_NAME)
        tabs = self.find_elements_from_node(tab_content,By.TAG_NAME,"div")
        print(len(tabs))
        tabs[tab_index].click()
    def enter_dropdown_number(self, index):
        management_number_dropdown = self.find_element(By.TAG_NAME,self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
        management_number_dropdown.click()
        time.sleep(3)
        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        dropdown_items[index].click()
        time.sleep(3)
    def search_requested(self,management_number="",
                         search_text="",
                         source="",
                         input_date="",
                         picup_type="",
                         sale_pic=""):
        if management_number != "":
            management_number_dropdown = self.find_element(By.TAG_NAME, self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
            self.enter_web_item_drop_down(management_number_dropdown,management_number)
        if search_text != "":
            search_item = self.find_element(By.XPATH,self.REQUESTED_SEARCH_TEXT)
            self.enter_web_item_text(search_item,search_text)
        if source != "":
            dropdown_source = self.find_element(By.XPATH,self.REQUESTED_DROPDOWN_SOURCE)
            self.enter_web_item_drop_down(dropdown_source,source)
        if input_date != "":
            input_date_element = self.find_element(By.XPATH,self.REQUESTED_INPUT_DATE)
            self.enter_web_item_text(input_date_element,input_date)
        if picup_type != "":
            dropdown_picup_type = self.find_element(By.XPATH,self.REQUESTED_DROPDOWN_PICUPTYPE)
            self.enter_web_item_drop_down(dropdown_picup_type,picup_type)
        if sale_pic != "":
            dropdown_sale_pic = self.find_element(By.XPATH,self.REQUESTED_DROPDOWN_SALEPIC)
            self.enter_web_item_drop_down(dropdown_sale_pic,sale_pic)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)
    def enter_reset_requested_button(self):
        button = self.find_element(By.XPATH,self.REQUESTED_RESET_BUTTON)
        button.click()
    def search_unvaluate(self,management_number="",
                         search_text="",
                         source="",
                         input_date="",
                         picup_type="",
                         sale_pic=""):
        if management_number != "":
            management_number_dropdown = self.find_element(By.TAG_NAME, self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
            self.enter_web_item_drop_down(management_number_dropdown,management_number)
        if search_text != "":
            search_item = self.find_element(By.XPATH,self.UNVALUATE_SEARCH_TEXT)
            self.enter_web_item_text(search_item,search_text)
        if source != "":
            dropdown_source = self.find_element(By.XPATH,self.UNVALUATE_DROPDOWN_SOURCE)
            self.enter_web_item_drop_down(dropdown_source,source)
        if input_date != "":
            input_date_element = self.find_element(By.XPATH,self.UNVALUATE_INPUT_DATE)
            self.enter_web_item_text(input_date_element,input_date)
        if picup_type != "":
            dropdown_picup_type = self.find_element(By.XPATH,self.UNVALUATE_DROPDOWN_PICUPTYPE)
            self.enter_web_item_drop_down(dropdown_picup_type,picup_type)
        if sale_pic != "":
            dropdown_sale_pic = self.find_element(By.XPATH,self.UNVALUATE_DROPDOWN_SALEPIC)
            self.enter_web_item_drop_down(dropdown_sale_pic,sale_pic)
    def search_valuating(self,management_number="",
                         search_text="",
                         source="",
                         input_date="",
                         picup_type="",
                         sale_pic=""):
        if management_number != "":
            management_number_dropdown = self.find_element(By.TAG_NAME, self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
            self.enter_web_item_drop_down(management_number_dropdown,management_number)
        if search_text != "":
            search_item = self.find_element(By.XPATH,self.VALUATING_SEARCH_TEXT)
            self.enter_web_item_text(search_item,search_text)
        if source != "":
            dropdown_source = self.find_element(By.XPATH,self.VALUATING_DROPDOWN_SOURCE)
            self.enter_web_item_drop_down(dropdown_source,source)
        if input_date != "":
            input_date_element = self.find_element(By.XPATH,self.VALUATING_INPUT_DATE)
            self.enter_web_item_text(input_date_element,input_date)
        if picup_type != "":
            dropdown_picup_type = self.find_element(By.XPATH,self.VALUATING_DROPDOWN_PICUPTYPE)
            self.enter_web_item_drop_down(dropdown_picup_type,picup_type)
        if sale_pic != "":
            dropdown_sale_pic = self.find_element(By.XPATH,self.VALUATING_DROPDOWN_SALEPIC)
            self.enter_web_item_drop_down(dropdown_sale_pic,sale_pic)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)

    def enter_reset_valuating(self):
        button = self.find_element(By.XPATH,self.VALUATING_RESET_BUTTON)
        button.click()
        time.sleep(2)
    def search_valuated(self,management_number="",
                         search_text="",
                         source="",
                         input_date="",
                         picup_type="",
                         sale_pic=""):
        if management_number != "":
            management_number_dropdown = self.find_element(By.TAG_NAME, self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
            self.enter_web_item_drop_down(management_number_dropdown,management_number)
        if search_text != "":
            search_item = self.find_element(By.XPATH,self.VALUATED_SEARCH_TEXT)
            self.enter_web_item_text(search_item,search_text)
        if source != "":
            dropdown_source = self.find_element(By.XPATH,self.VALUATING_DROPDOWN_SOURCE)
            self.enter_web_item_drop_down(dropdown_source,source)
        if input_date != "":
            input_date_element = self.find_element(By.XPATH,self.VALUATED_INPUT_DATE)
            self.enter_web_item_text(input_date_element,input_date)
        if picup_type != "":
            dropdown_picup_type = self.find_element(By.XPATH,self.VALUATED_DROPDOWN_PICUPTYPE)
            self.enter_web_item_drop_down(dropdown_picup_type,picup_type)
        if sale_pic != "":
            dropdown_sale_pic = self.find_element(By.XPATH,self.VALUATED_DROPDOWN_SALEPIC)
            self.enter_web_item_drop_down(dropdown_sale_pic,sale_pic)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)
    def enter_reset_valuated(self):
        button = self.find_element(By.XPATH,self.VALUATED_RESET_BUTTON)
        button.click()


    def search_assorted(self,management_number="",
                         search_text="",
                         source="",
                         input_date="",
                         picup_type="",
                         sale_pic=""):
        if management_number != "":
            management_number_dropdown = self.find_element(By.TAG_NAME, self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
            self.enter_web_item_drop_down(management_number_dropdown,management_number)
        if search_text != "":
            search_item = self.find_element(By.XPATH,self.ASSORTED_SEARCH_TEXT)
            self.enter_web_item_text(search_item,search_text)
        if source != "":
            dropdown_source = self.find_element(By.XPATH,self.ASSORTED_DROPDOWN_SOURCE)
            self.enter_web_item_drop_down(dropdown_source,source)
        if input_date != "":
            input_date_element = self.find_element(By.XPATH,self.ASSORTED_INPUT_DATE)
            self.enter_web_item_text(input_date_element,input_date)
        if picup_type != "":
            dropdown_picup_type = self.find_element(By.XPATH,self.ASSORTED_DROPDOWN_PICUPTYPE)
            self.enter_web_item_drop_down(dropdown_picup_type,picup_type)
        if sale_pic != "":
            dropdown_sale_pic = self.find_element(By.XPATH,self.ASSORTED_DROPDOWN_SALEPIC)
            self.enter_web_item_drop_down(dropdown_sale_pic,sale_pic)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)
    def enter_reset_assorted(self):
        button = self.find_element(By.XPATH,self.ASSORTED_RESET_BUTTON)
        button.click()
    def search_all(self,management_number="",
                         search_text="",
                         source="",
                         validation_status="",
                         input_date="",
                         picup_type="",
                         sale_pic=""):
        if management_number != "":
            management_number_dropdown = self.find_element(By.TAG_NAME, self.DROPDOWN_MANAGEMENT_NUMBER_TAG)
            self.enter_web_item_drop_down(management_number_dropdown,management_number)
        if search_text != "":
            search_item = self.find_element(By.XPATH,self.ALL_SEARCH_TEXT)
            self.enter_web_item_text(search_item,search_text)
        if source != "":
            dropdown_source = self.find_element(By.XPATH,self.ALL_DROPDOWN_SOURCE)
            self.enter_web_item_drop_down(dropdown_source,source)
        if validation_status != "":
            dropdown_status = self.find_element(By.XPATH, self.ALL_VALIDATION_STATUS)
            self.enter_web_item_drop_down(dropdown_status, validation_status)
        if input_date != "":
            input_date_element = self.find_element(By.XPATH,self.ALL_INPUT_DATE)
            self.enter_web_item_text(input_date_element,input_date)
        if picup_type != "":
            dropdown_picup_type = self.find_element(By.XPATH,self.ALL_DROPDOWN_PICUPTYPE)
            self.enter_web_item_drop_down(dropdown_picup_type,picup_type)
        if sale_pic != "":
            dropdown_sale_pic = self.find_element(By.XPATH,self.ALL_DROPDOWN_SALEPIC)
            self.enter_web_item_drop_down(dropdown_sale_pic,sale_pic)
    def enter_text_in_modal_dialog(self, web_element,text_value):
        web_element.click();
        time.sleep(3)
        txt_element = self.find_elements_from_node(web_element, By.TAG_NAME, "input")[0]
        txt_element.send_keys(Keys.CONTROL + "a")
        txt_element.send_keys(Keys.DELETE)
        txt_element.send_keys(text_value)
        txt_element.send_keys(Keys.ENTER)
        time.sleep(2)
    def enter_dropdown_in_modal_dialog(self,web_element,option_text):
        web_element.click();
        time.sleep(3)
        car_maker_dropdown = self.find_elements_from_node(web_element, By.TAG_NAME, "nz-select-top-control")
        self.driver.execute_script("arguments[0].click();",car_maker_dropdown[0])


        dropdown_content = self.find_element(By.TAG_NAME, "cdk-virtual-scroll-viewport")

        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        if isinstance(option_text,int):
            dropdown_items[option_text].click()
        else:
            input = car_maker_dropdown[0].find_element(By.TAG_NAME,"input")
            input.send_keys(option_text)
            input.send_keys(Keys.ENTER)
    def enter_range_textbox_dialog(self,web_element,text_values):
        values = text_values.split("-")
        web_element.click()
        time.sleep(3)
        textboxes = self.find_elements_from_node(web_element, By.TAG_NAME, "input")
        textboxes[0].send_keys(Keys.CLEAR)
        textboxes[0].send_keys(values[0])
        textboxes[1].send_keys(Keys.CLEAR)
        textboxes[1].send_keys(values[1])
        time.sleep(3)
    def search_using_filter(self,
                            tab_index = 0,
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
                                       validation_status = "",
                                       source = "",
                                       picup_request_number = "",
                                       picup_type = ""
                                       ):
        if tab_index == 1:
            filter_button = self.find_element(By.XPATH,self.REQUESTED_FILTER_BUTTON)
        elif tab_index == 3:
            filter_button = self.find_element(By.XPATH, self.UNVALUATE_FILTER_BUTTON)
        elif tab_index == 5:
            filter_button = self.find_element(By.XPATH, self.VALUATING_FILTER_BUTTON)
        elif tab_index == 7:
            filter_button = self.find_element(By.XPATH, self.VALUATED_FILTER_BUTTON)

        elif tab_index == 9:
            filter_button = self.find_element(By.XPATH, self.ASSORTED_FILTER_BUTTON)
        elif tab_index == 11:
            filter_button = self.find_element(By.XPATH, self.ALL_FILTER_BUTTON)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", filter_button)
        time.sleep(1)
        dialog_content = self.find_element(By.TAG_NAME,"app-popup-filter-valuation")
        items = self.find_elements_from_node(dialog_content,By.XPATH,"./*")
        if management_number != "":
            self.enter_text_in_modal_dialog(items[0],management_number)
        if car_maker != "":
            self.enter_dropdown_in_modal_dialog(items[1],car_maker)
        if car_name != "":
            self.enter_dropdown_in_modal_dialog(items[2], car_name)
        if model != "":
            self.enter_dropdown_in_modal_dialog(items[3], model)
        if chassis_number != "":
            self.enter_text_in_modal_dialog(items[4],chassis_number)
        if mile_age != "":
            self.enter_range_textbox_dialog(items[5],mile_age)
        if displacement != "":
            self.enter_range_textbox_dialog(items[6], displacement)
        if sale_pic != "" :
            self.enter_dropdown_in_modal_dialog(items[7],sale_pic)
        if supplier !="" :
            self.enter_dropdown_in_modal_dialog(items[8], supplier)
        if input_date != "":
            self.enter_range_textbox_dialog(items[9],input_date)
        if validation_status != "":
            self.enter_dropdown_in_modal_dialog(items[10],validation_status)
        if source !=  "" :
            self.enter_dropdown_in_modal_dialog(items[11],source)
        if picup_request_number != "":
            self.enter_text_in_modal_dialog(items[12], picup_request_number)
        if picup_type != "":
            self.enter_dropdown_in_modal_dialog(items[13], picup_type)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        buttons = self.find_elements_from_node(footer_area,By.TAG_NAME,"button")
        buttons[1].click()
        time.sleep(3)
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        elements = table_content.find_elements(By.TAG_NAME, "tr")
        return len(elements)
    def select_car_valuation(self):
        table_content_element = self.find_element(By.CLASS_NAME,self.TABLE_CONTENT_CLASS_NAME)
        table_body = self.find_elements_from_node(table_content_element,By.TAG_NAME,"tbody")[0]
        tr_elements = self.find_elements_from_node(table_body,By.TAG_NAME,"tr")
        car_valuation_index = random.randint(1,len(tr_elements)-1)
        tr_elements[car_valuation_index].click()
        time.sleep(3)
        car_valuation_detail = CarValuationDetail(self.driver)
        time.sleep(3)
        return car_valuation_detail
    def get_all_chasis_number_in_list(self,tab_index):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME,"tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        chasis_num_column_index = 7
        if tab_index == 1:
            chasis_num_column_index = 7
        elif tab_index == 5:
            chasis_num_column_index = 6
        elif tab_index == 9:
            chasis_num_column_index = 6
        lst_chasis_number = []
        for row in rows:
            tds = row.find_elements(By.TAG_NAME,"td")
            if tds[chasis_num_column_index].text != "":
                lst_chasis_number.append(tds[chasis_num_column_index].text)
        return lst_chasis_number
    def do_valuate_item_in_list(self,chasis_number = ""):
        table_content_element = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = self.find_elements_from_node(table_content_element, By.TAG_NAME, "tbody")[0]
        tr_elements = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        tr_elements = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        if chasis_number == "":
            car_valuation_index = random.randint(0,len(tr_elements)-1)
            tds = self.find_elements_from_node(tr_elements[car_valuation_index],By.TAG_NAME,"td")
            buttons = self.find_elements_from_node(tds[15], By.TAG_NAME, "button")
            buttons[0].click()
            car_on_validation = CarOnValuation(self.driver)
            return car_on_validation
        else:
            for tr in tr_elements:
                tds = tr.find_elements(By.TAG_NAME,"td")
                if tds[7].text == chasis_number:
                    buttons = self.find_elements_from_node(tds[15], By.TAG_NAME, "button")
                    buttons[0].click()
                    car_on_validation = CarOnValuation(self.driver)
                    return car_on_validation
                    break


    def do_reject_item_in_list(self,car_valuation_index):
        table_content_element = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = self.find_elements_from_node(table_content_element, By.TAG_NAME, "tbody")[0]
        tr_elements = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        tds = self.find_elements_from_node(tr_elements[car_valuation_index],By.TAG_NAME,"td")
        buttons = self.find_elements_from_node(tds[15], By.TAG_NAME, "button")
        buttons[1].click()
    def do_assort_part(self):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        num_record = len(rows)
        row_index = random.randint(1,num_record-1)
        columns = rows[row_index].find_elements(By.TAG_NAME,"td")
        buttons = columns[-1].find_elements(By.TAG_NAME,"button")
        buttons[0].click()
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(footer_area, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(2)
    def do_auto_assort(self,chasis_number=""):
        table_content = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        if chasis_number == "":
            num_record = len(rows)
            row_index = random.randint(1,num_record-1)
            columns = rows[row_index].find_elements(By.TAG_NAME, "td")
            buttons = columns[-1].find_elements(By.TAG_NAME, "button")
            buttons[1].click()
            footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-popover-buttons')]")
            buttons = footer_area.find_elements(By.TAG_NAME, "button")
            buttons[1].click()
            time.sleep(2)
        else:
            for row in rows:
                columns = row.find_elements(By.TAG_NAME,"td")
                if columns[7].text == chasis_number:
                    buttons = columns[-1].find_elements(By.TAG_NAME, "button")
                    buttons[2].click()
                    break
            footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-popover-buttons')]")
            buttons = footer_area.find_elements(By.TAG_NAME, "button")
            buttons[1].click()
            time.sleep(2)















