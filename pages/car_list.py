import random
from re import search
from numpy.lib.user_array import container
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from pages.CarDetail import CarDetail

DIV_TAG = "div"
class CarList(BaseDriver):
    #common
    CONTENT_CLASSNAME = "cdk-virtual-scroll-content-wrapper"
    DROPDOWN_LIST_TAG = "nz-select-top-control"
    TAB_CONTAINERS_CLASS_NAME = "ant-tabs-nav-list"
    DROPDOWN_CONTENT = "cdk-virtual-scroll-viewport"
    DROPDOWN_CONTENT_FILTER_POPUP = "cdk-virtual-scroll-content-wrapper"
    # tab_all
    ALL_SEARCH_INPUT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-all/app-car-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    ALL_GRID_COLUMNS_NUMBER = 14
    ALL_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-all/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"
    ALL_MULTIPLE_DELETE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-all/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-title-footer[1]/button"
    # tab Neotiating
    NEGO_SOURCE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-negotiating/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    NEGO_SEARCH_INPUT =    "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-negotiating/app-car-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    NEGO_SUPPLIER_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-negotiating/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-select-supplier"
    NEGO_SALEPIC_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-negotiating/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-sale-pic"
    NEGO_PICUP_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-negotiating/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/app-select-option-value/nz-select/nz-select-top-control/nz-select-search/input"
    NEGO_INPUT_DATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-negotiating/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[1]/app-date-picker/nz-date-picker/div/input"
    NEGO_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-negotiating/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[2]/button[1]"
    NEGO_GRID_COLUMNS_NUMBER = 10
    NEGO_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-negotiating/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"
    NEGO_RESET_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-negotiating/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[2]/button[2]"

    # tab Unstocked
    UNSTOCK_SOURCE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    UNSTOCK_SEARCH_INPUT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/app-car-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    UNSTOCK_DEADLINE_CALENDAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    UNSTOCK_SALEPIC_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-sale-pic"
    UNSTOCK_PICUP_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/app-select-option-value"
    UNSTOCK_PURPOSE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[1]/app-select-option-value"
    UNSTOCK_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[2]/button[1]"
    UNSTOCK_GRID_COLUMNS_NUMBER = 10
    UNSTOCK_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"
    UNSTOCK_GRID_COLUMNS_NUMBER = 16
    UNSTOCK_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"
    UNSTOCK_STORAGE_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-title-footer[1]/button"
    UNSTOCK_RESET_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-unstocked/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[2]/button[2]"

    #tab Storage
    STORAGE_SOURCE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    STORAGE_SEARCH_INPUT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/app-car-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    STORAGE_WHAREHOUSE_CALENDAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    STORAGE_WHAREHOUSE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-warehouse"
    STORAGE_PICUP_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/app-select-option-value"
    STORAGE_SUPPLIER_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/app-select-supplier"
    STORAGE_PURPOSE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[6]/nz-row/nz-col[1]/app-select-option-value"
    STORAGE_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[6]/nz-row/nz-col[2]/button[1]"
    STORAGE_GRID_COLUMNS_NUMBER = 12
    STORAGE_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"
    STORAGE_RESET_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-storage/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[6]/nz-row/nz-col[2]/button[2]"


    # tab Standby
    STANDBY_SOURCE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-standby/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    STANDBY_SEARCH_INPUT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-standby/app-car-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    STANDBY_WHAREHOUSE_CALENDAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-standby/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    STANDBY_CAR_MAKER_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-standby/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-car-maker"
    STANDBY_PICUP_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-standby/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/app-select-option-value"
    STANDBY_PURPOSE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-standby/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[1]/app-select-option-value"
    STANDBY_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-standby/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[2]/button[1]"
    STANDBY_GRID_COLUMNS_NUMBER = 10
    STANDBY_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-standby/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"



    # tab Inproduction
    INPRODUCTION_SOURCE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-part-production/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    INPRODUCTION_SEARCH_INPUT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-part-production/app-car-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    INPRODUCTION_PROCESSING_CALENDAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-part-production/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    INPRODUCTION_PIC_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-part-production/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-production-pic"
    INPRODUCTION_PICUP_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-part-production/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/app-select-option-value"
    INPRODUCTION_PURPOSE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-part-production/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[1]/app-select-option-value"
    INPRODUCTION_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-part-production/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[2]/button[1]"
    INPRODUCTION_GRID_COLUMNS_NUMBER = 9
    INPRODUCTION_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-part-production/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"



    # tab produced
    PRODUCED_SOURCE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-produced/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    PRODUCED_SEARCH_INPUT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-produced/app-car-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    PRODUCED_PROCESSING_CALENDAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-produced/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-date-picker/nz-date-picker/div/input"
    PRODUCED_CAR_MAKER_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-produced/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-car-maker"
    PRODUCED_PICUP_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-produced/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/app-select-option-value"
    PRODUCED_PURPOSE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-produced/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[1]/app-select-option-value"
    PRODUCED_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-produced/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[2]/button[1]"
    PRODUCED_GRID_COLUMNS_NUMBER = 9
    PRODUCED_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-produced/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"


    # tab not purchase
    NOT_PURCHASED_SOURCE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-not-purchased/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
    NOT_PURCHASED_SEARCH_INPUT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-not-purchased/app-car-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    NOT_PURCHASED_INPUT_CALENDAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-not-purchased/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[1]/app-date-picker/nz-date-picker/div/input"
    NOT_PURCHASED_SUPPLIER_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-not-purchased/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-select-supplier"
    NOT_PURCHASED_PICUP_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-not-purchased/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[4]/app-select-option-value"
    NOT_PURCHASED_SALE_PIC_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-not-purchased/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/app-select-sale-pic"
    NOT_PURCHASED_FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-not-purchased/app-car-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[5]/nz-row/nz-col[2]/button[1]"
    NOT_PURCHASED_GRID_COLUMNS_NUMBER = 11
    NOT_PURCHASED_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-not-purchased/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"

    # tab deleted
    DELETED_SEARCH_INPUT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-deleted/app-car-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    DELETED_GRID_COLUMNS_NUMBER = 11
    DELETED_TABLE_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-list/nz-card/div/app-deleted/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table"

    #popup filter
    FILTER_POPUP_TAG = "app-filter-popup"
    POPUP_CAR_FILTER_DROPDOWN = "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/app-filter-popup/div[2]/nz-collapse/nz-collapse-panel/div[2]/div/nz-row/nz-col/nz-row/nz-col/nz-form-item/app-select-car-maker"

    def __init__(self,driver):
        super().__init__(driver)
    def click_at_tab(self,index):
        tab_navigator = self.find_element(By.CLASS_NAME,self.TAB_CONTAINERS_CLASS_NAME)
        tab_headers = tab_navigator.find_elements(By.TAG_NAME,"div")
        tab_headers[index].click()
    def enter_textbox_control(self,target_control,value):
         target_control.send_keys(Keys.CONTROL + "a")
         target_control.send_keys(Keys.DELETE)
         target_control.send_keys(value)
         target_control.send_keys(Keys.ENTER)
    def enter_dropdown_by_option_value(self,element,option_value):
         element.click()
         time.sleep(3)
         dropdown_contents = self.find_element(By.TAG_NAME, self.DROPDOWN_CONTENT)
         items = self.find_elements_from_node(dropdown_contents, By.TAG_NAME, "nz-option-item")
         if isinstance(option_value,int):
            items[option_value].click()
         else:
            for item in items:
                if item.text == option_value:
                    item.click()
                    break
    def enter_textbox_in_filter_dialog(self,web_element,text_value):
        web_element.click()
        txt_management = self.find_elements_from_node(web_element, By.TAG_NAME, "input")[0]
        self.enter_textbox_control(txt_management,text_value)
        time.sleep(1)
    def enter_drop_down_in_filter_dialog(self,web_element,dropdown_value):
        web_element.click()
        time.sleep(1)
        dropdown = self.find_elements_from_node(web_element, By.TAG_NAME, "input")
        dropdown[0].send_keys(dropdown_value)
        dropdown[0].send_keys(Keys.ENTER)
        time.sleep(1)
    def enter_range_dropdown_in_filter_dialog(self,web_element,option_values):
        values = option_values.split("-")
        web_element.click()
        time.sleep(1)
        dropdowns = self.find_elements_from_node(web_element, By.TAG_NAME, "app-select-year")
        dropdowns[0].click()
        input = dropdowns[0].find_element(By.TAG_NAME, "input")
        input.send_keys(values[0])
        time.sleep(1)
        dropdowns[1].click()
        input = dropdowns[1].find_element(By.TAG_NAME, "input")
        input.send_keys(values[1])
        time.sleep(1)
    def enter_text_range_in_filter_dialog(self,web_element,text_values):
        values = text_values.split("-")
        web_element.click()
        time.sleep(3)
        inputs = self.find_elements_from_node(web_element, By.TAG_NAME, "input")
        self.enter_textbox_control(inputs[0],values[0])
        self.enter_textbox_control(inputs[1], values[1])
    def check_all_columns_number(self):
         table_content = self.find_element(By.XPATH,self.ALL_TABLE_CONTENT)
         th_elements = self.find_elements_from_node(table_content,By.TAG_NAME,"th")
         if len(th_elements) == self.ALL_GRID_COLUMNS_NUMBER:
             return True
         else:
             return False
    def enter_all_drowdown_number(self, drowdown_index):
        drop_down_all = self.find_element(By.TAG_NAME,self.DROPDOWN_LIST_TAG)
        drop_down_all.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.CLASS_NAME,self.DROPDOWN_CONTENT)
        select_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        select_items[drowdown_index].click()
        time.sleep(2)
    def enter_all_text_search(self,text):
        search_input = self.find_element(By.XPATH,self.ALL_SEARCH_INPUT)
        search_input.send_keys(Keys.CONTROL + "a")
        search_input.send_keys(Keys.DELETE)
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)
    def check_nego_columns_number(self):
         table_content = self.find_element(By.XPATH,self.NEGO_TABLE_CONTENT)
         th_elements = self.find_elements_from_node(table_content,By.TAG_NAME,"th")
         if len(th_elements) == self.NEGO_GRID_COLUMNS_NUMBER:
             return True
         else:
             return False

    def enter_nego_drowdown_number(self, drowdown_index):
        drop_down = self.find_element(By.TAG_NAME,self.DROPDOWN_LIST_TAG)
        drop_down.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.CLASS_NAME,self.DROPDOWN_CONTENT)
        select_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,DIV_TAG)
        select_items[drowdown_index].click()
        time.sleep(2)
    def enter_nego_text_search(self,text):
        search_input = self.find_element(By.XPATH,self.NEGO_SEARCH_INPUT)
        search_input.send_keys(Keys.CONTROL + "a")
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)
    def enter_nego_source_dropdown(self,index):
        source_drop_down = self.find_element(By.XPATH,self.NEGO_SOURCE_DROPDOWN)
        self.enter_dropdown_by_option_value(source_drop_down,index)
    def enter_nego_supplier_dropdown(self,index):
        supplier_dropdown = self.find_element(By.XPATH,self.NEGO_SUPPLIER_DROPDOWN)
        self.enter_dropdown_by_option_value(supplier_dropdown,option_value=index)
    def enter_nego_sale_pic(self,index):
        salepic_dropdown = self.find_element(By.XPATH,self.NEGO_SALEPIC_DROPDOWN)
        self.enter_dropdown_by_option_value(salepic_dropdown, option_value=index)
    def enter_nego_picup_dropdown(self,index):
        picup_dropdown = self.find_element(By.XPATH,self.NEGO_PICUP_DROPDOWN)
        self.enter_dropdown_by_option_value(picup_dropdown, option_value=index)
    def enter_nego_date_picker(self,date_string):
        date_input = self.find_element(By.XPATH,self.NEGO_INPUT_DATE)
        self.enter_textbox_control(date_input,date_string)
    def enter_nego_filter(self):
        filter_button = self.find_element(By.XPATH,self.NEGO_FILTER_BUTTON)
        self.driver.execute_script("arguments[0].click();", filter_button)
    def enter_nego_reset(self):
        reset_button = self.find_element(By.XPATH,self.NEGO_RESET_BUTTON)
        self.driver.execute_script("arguments[0].click();", reset_button)

    # Unstock tab
    def check_unstocked_columns_number(self):
         table_content = self.find_element(By.XPATH,self.UNSTOCK_TABLE_CONTENT)
         th_elements = self.find_elements_from_node(table_content,By.TAG_NAME,"th")
         if len(th_elements) == self.UNSTOCK_GRID_COLUMNS_NUMBER:
             return True
         else:
             return False
    def enter_unstocked_drowdown_number(self, drowdown_index):
        drop_down = self.find_element(By.TAG_NAME,self.DROPDOWN_LIST_TAG)
        drop_down.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.CLASS_NAME,self.DROPDOWN_CONTENT)
        select_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,DIV_TAG)
        select_items[drowdown_index].click()
        time.sleep(2)
    def enter_unstocked_text_search(self,text):
        search_input = self.find_element(By.XPATH,self.UNSTOCK_SEARCH_INPUT)
        self.enter_textbox_control(search_input,text)
        time.sleep(1)
    def enter_unstocked_source_dropdown(self,index):
        source_drop_down = self.find_element(By.XPATH,self.UNSTOCK_SOURCE_DROPDOWN)
        self.enter_dropdown_by_option_value(source_drop_down, option_value=index)
    def enter_unstocked_pickup_deadline(self,str_date):
        dead_line_dt = self.find_element(By.XPATH,self.UNSTOCK_DEADLINE_CALENDAR)
        self.enter_textbox_control(dead_line_dt,str_date)
    def enter_unstocked_sale_pic(self,index):
        salepic_dropdown = self.find_element(By.XPATH,self.UNSTOCK_SALEPIC_DROPDOWN)
        self.enter_dropdown_by_option_value(salepic_dropdown, option_value=index)
    def enter_unstocked_picup_dropdown(self,index):
        picup_dropdown = self.find_element(By.XPATH,self.UNSTOCK_PICUP_DROPDOWN)
        self.enter_dropdown_by_option_value(picup_dropdown,option_value=index)
    def enter_unstocked_purpose_dropdown(self,index):
        purpose_dropdown = self.find_element(By.XPATH,self.UNSTOCK_PURPOSE_DROPDOWN)
        self.enter_dropdown_by_option_value(purpose_dropdown, option_value=index)

    def enter_unstocked_filter(self):
        btn_filter = self.find_element(By.XPATH,self.UNSTOCK_FILTER_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn_filter)

    def enter_reset_unstock(self):
        btn_reset = self.find_element(By.XPATH,self.UNSTOCK_RESET_BUTTON)
        btn_reset.click()
    # storage
    def check_storage_columns_number(self):
         table_content = self.find_element(By.XPATH,self.STORAGE_TABLE_CONTENT)
         th_elements = self.find_elements_from_node(table_content,By.TAG_NAME,"th")
         if len(th_elements) == self.STORAGE_GRID_COLUMNS_NUMBER:
             return True
         else:
             return False
    def enter_storage_drowdown_number(self, drowdown_index):
        drop_down_all = self.find_element(By.TAG_NAME,self.DROPDOWN_LIST_TAG)
        drop_down_all.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.CLASS_NAME,self.DROPDOWN_CONTENT)
        select_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,DIV_TAG)
        select_items[drowdown_index].click()
        time.sleep(2)
    def enter_storage_text_search(self,text):
        search_input = self.find_element(By.XPATH,self.STORAGE_SEARCH_INPUT)
        self.enter_textbox_control(search_input,text)
        time.sleep(1)
    def enter_storage_source_dropdown(self,index):
        source_drop_down = self.find_element(By.XPATH,self.STORAGE_SOURCE_DROPDOWN)
        self.enter_dropdown_by_option_value(source_drop_down,option_value=index)
    def enter_storage_pickup_ware_house_date(self,str_date):
        dead_line_dt = self.find_element(By.XPATH,self.STORAGE_WHAREHOUSE_CALENDAR)
        self.enter_textbox_control(dead_line_dt,str_date)
    def enter_storage_whare_house_dropdown(self,index):
        salepic_dropdown = self.find_element(By.XPATH,self.STORAGE_WHAREHOUSE_DROPDOWN)
        self.enter_dropdown_by_option_value(salepic_dropdown,option_value=index)
    def enter_storage_picup_dropdown(self,index):
        picup_dropdown = self.find_element(By.XPATH,self.STORAGE_PICUP_DROPDOWN)
        self.enter_dropdown_by_option_value(picup_dropdown,option_value=index)
    def enter_storage_supplier_dropdown(self,index):
        supplier_dropdown = self.find_element(By.XPATH,self.STORAGE_SUPPLIER_DROPDOWN)
        self.enter_dropdown_by_option_value(supplier_dropdown, option_value=index)
    def enter_storage_purpose_dropdown(self,index):
        purpose_dropdown = self.find_element(By.XPATH,self.STORAGE_PURPOSE_DROPDOWN)
        self.enter_dropdown_by_option_value(purpose_dropdown, option_value=index)
    def enter_storage_filter(self):
        btn_filter = self.find_element(By.XPATH,self.STORAGE_FILTER_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn_filter)
    def enter_storage_reset(self):
        btn_reset = self.find_element(By.XPATH,self.STORAGE_RESET_BUTTON)
        btn_reset.click()
    # standby
    def check_standby_columns_number(self):
         table_content = self.find_element(By.XPATH,self.STANDBY_TABLE_CONTENT)
         th_elements = self.find_elements_from_node(table_content,By.TAG_NAME,"th")
         if len(th_elements) == self.STANDBY_GRID_COLUMNS_NUMBER:
             return True
         else:
             return False
    def enter_standby_drowdown_number(self, drowdown_index):
        drop_down = self.find_element(By.TAG_NAME,self.DROPDOWN_LIST_TAG)
        drop_down.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.CLASS_NAME,self.DROPDOWN_CONTENT)
        select_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,DIV_TAG)
        select_items[drowdown_index].click()
        time.sleep(2)
    def enter_standby_text_search(self,text):
        search_input = self.find_element(By.XPATH,self.STANDBY_SEARCH_INPUT)
        self.enter_textbox_control(search_input,text)
    def enter_standby_source_dropdown(self,index):
        source_drop_down = self.find_element(By.XPATH,self.STANDBY_SOURCE_DROPDOWN)
        self.enter_dropdown_by_option_value(source_drop_down,option_value=index)
    def enter_standby_pickup_ware_house_date(self,str_date):
        dead_line_dt = self.find_element(By.XPATH,self.STANDBY_WHAREHOUSE_CALENDAR)
        self.enter_textbox_control(dead_line_dt,str_date)
    def enter_standby_car_maker_dropdown(self,index):
        salepic_dropdown = self.find_element(By.XPATH,self.STANDBY_CAR_MAKER_DROPDOWN)
        self.enter_dropdown_by_option_value(salepic_dropdown, option_value=index)
    def enter_standby_picup_dropdown(self,index):
        picup_dropdown = self.find_element(By.XPATH,self.STANDBY_PICUP_DROPDOWN)
        self.enter_dropdown_by_option_value(picup_dropdown, option_value=index)
    def enter_standby_purpose_dropdown(self,index):
        purpose_dropdown = self.find_element(By.XPATH,self.STANDBY_PURPOSE_DROPDOWN)
        self.enter_dropdown_by_option_value(purpose_dropdown, option_value=index)
    def enter_standby_filter(self):
        btn_filter = self.find_element(By.XPATH,self.STANDBY_FILTER_BUTTON)
        btn_filter.click()
    # in production
    def check_inproduction_columns_number(self):
         table_content = self.find_element(By.XPATH,self.INPRODUCTION_TABLE_CONTENT)
         th_elements = self.find_elements_from_node(table_content,By.TAG_NAME,"th")
         if len(th_elements) == self.INPRODUCTION_GRID_COLUMNS_NUMBER:
             return True
         else:
             return False
    def enter_inproduction_drowdown_number(self, drowdown_index):
        drop_down = self.find_element(By.TAG_NAME,self.DROPDOWN_LIST_TAG)
        drop_down.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.CLASS_NAME,self.DROPDOWN_CONTENT)
        select_items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,DIV_TAG)
        select_items[drowdown_index].click()
        time.sleep(2)
    def enter_inproduction_text_search(self,text):
        search_input = self.find_element(By.XPATH,self.INPRODUCTION_SEARCH_INPUT)
        self.enter_textbox_control(search_input,text)
    def enter_inproduction_source_dropdown(self,index):
        source_drop_down = self.find_element(By.XPATH,self.INPRODUCTION_SOURCE_DROPDOWN)
        self.enter_dropdown_by_option_value(source_drop_down,option_value=index)
    def enter_inproduction_processing_date(self,str_date):
        dead_line_dt = self.find_element(By.XPATH,self.INPRODUCTION_PROCESSING_CALENDAR)
        self.enter_textbox_control(dead_line_dt,str_date)
    def enter_inproduction_pic_dropdown(self,index):
        salepic_dropdown = self.find_element(By.XPATH,self.INPRODUCTION_PIC_DROPDOWN)
        self.enter_dropdown_by_option_value(salepic_dropdown,option_value=index)
    def enter_inproduction_picup_dropdown(self,index):
        picup_dropdown = self.find_element(By.XPATH,self.INPRODUCTION_PICUP_DROPDOWN)
        self.enter_dropdown_by_option_value(picup_dropdown,option_value=index)
    def enter_inproduction_purpose_dropdown(self,index):
        purpose_dropdown = self.find_element(By.XPATH,self.INPRODUCTION_PURPOSE_DROPDOWN)
        self.enter_dropdown_by_option_value(purpose_dropdown, option_value=index)
    def enter_inproduction_filter(self):
        btn_filter = self.find_element(By.XPATH,self.INPRODUCTION_FILTER_BUTTON)
        btn_filter.click()
    # produced table
    def check_produced_columns_number(self):
         table_content = self.find_element(By.XPATH,self.PRODUCED_TABLE_CONTENT)
         th_elements = self.find_elements_from_node(table_content,By.TAG_NAME,"th")
         if len(th_elements) == self.PRODUCED_GRID_COLUMNS_NUMBER:
             return True
         else:
             return False
    def enter_produced_drowdown_number(self, drowdown_index):
        drop_down = self.find_element(By.TAG_NAME, self.DROPDOWN_LIST_TAG)
        drop_down.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.CLASS_NAME, self.DROPDOWN_CONTENT)
        select_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, DIV_TAG)
        select_items[drowdown_index].click()
        time.sleep(2)
    def enter_produced_text_search(self, text):
        search_input = self.find_element(By.XPATH, self.PRODUCED_SEARCH_INPUT)
        self.enter_textbox_control(search_input,text)
    def enter_produced_source_dropdown(self, index):
        source_drop_down = self.find_element(By.XPATH, self.PRODUCED_SOURCE_DROPDOWN)
        self.enter_dropdown_by_option_value(source_drop_down,option_value=index)
    def enter_produced_processing_date(self, str_date):
        dead_line_dt = self.find_element(By.XPATH, self.PRODUCED_PROCESSING_CALENDAR)
        self.enter_textbox_control(dead_line_dt,str_date)
    def enter_produced_car_maker_dropdown(self, index):
        salepic_dropdown = self.find_element(By.XPATH, self.PRODUCED_CAR_MAKER_DROPDOWN)
        self.enter_dropdown_by_option_value(salepic_dropdown,option_value=index)
    def enter_produced_picup_dropdown(self, index):
        picup_dropdown = self.find_element(By.XPATH, self.PRODUCED_PICUP_DROPDOWN)
        self.enter_dropdown_by_option_value(picup_dropdown, option_value=index)
    def enter_produced_purpose_dropdown(self, index):
        purpose_dropdown = self.find_element(By.XPATH, self.PRODUCED_PURPOSE_DROPDOWN)
        self.enter_dropdown_by_option_value(purpose_dropdown, option_value=index)
    def enter_produced_filter(self):
        btn_filter = self.find_element(By.XPATH, self.PRODUCED_FILTER_BUTTON)
        btn_filter.click()
    # not purchase tab
    def check_not_perchase_columns_number(self):
         table_content = self.find_element(By.XPATH,self.NOT_PURCHASED_TABLE_CONTENT)
         th_elements = self.find_elements_from_node(table_content,By.TAG_NAME,"th")
         if len(th_elements) == self.NOT_PURCHASED_GRID_COLUMNS_NUMBER:
             return True
         else:
             return False
    def enter_not_purchased_drowdown_number(self, drowdown_index):
        drop_down = self.find_element(By.TAG_NAME, self.DROPDOWN_LIST_TAG)
        drop_down.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.CLASS_NAME, self.DROPDOWN_CONTENT)
        select_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, DIV_TAG)
        select_items[drowdown_index].click()
        time.sleep(2)

    def enter_not_purchased_text_search(self, text):
        search_input = self.find_element(By.XPATH, self.NOT_PURCHASED_SEARCH_INPUT)
        self.enter_textbox_control(search_input,text)
    def enter_not_purchased_source_dropdown(self, index):
        source_drop_down = self.find_element(By.XPATH, self.NOT_PURCHASED_SOURCE_DROPDOWN)
        self.enter_dropdown_by_option_value(source_drop_down,option_value=index)
    def enter_not_purchased_input_date(self, str_date):
        dead_line_dt = self.find_element(By.XPATH, self.NOT_PURCHASED_INPUT_CALENDAR)
        self.enter_textbox_control(dead_line_dt,str_date)
    def enter_not_purchased_supplier_dropdown(self, index):
        salepic_dropdown = self.find_element(By.XPATH, self.NOT_PURCHASED_SUPPLIER_DROPDOWN)
        self.enter_dropdown_by_option_value(salepic_dropdown,option_value=index)
    def enter_not_purchased_picup_dropdown(self, index):
        picup_dropdown = self.find_element(By.XPATH, self.NOT_PURCHASED_PICUP_DROPDOWN)
        self.enter_dropdown_by_option_value(picup_dropdown,option_value=index)
    def enter_not_purchased_sale_pic_dropdown(self, index):
        purpose_dropdown = self.find_element(By.XPATH, self.NOT_PURCHASED_SALE_PIC_DROPDOWN)
        self.enter_dropdown_by_option_value(purpose_dropdown,option_value=index)
    def enter_not_purchased_filter(self):
        btn_filter = self.find_element(By.XPATH, self.NOT_PURCHASED_FILTER_BUTTON)
        btn_filter.click()
    #deleted tab
    def check_deleted_columns_number(self):
         table_content = self.find_element(By.XPATH,self.DELETED_TABLE_CONTENT)
         th_elements = self.find_elements_from_node(table_content,By.TAG_NAME,"th")
         if len(th_elements) == self.DELETED_GRID_COLUMNS_NUMBER:
             return True
         else:
             return False
    def enter_deleted_drowdown_number(self, drowdown_index):
        drop_down = self.find_element(By.TAG_NAME, self.DROPDOWN_LIST_TAG)
        drop_down.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.CLASS_NAME, self.DROPDOWN_CONTENT)
        select_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, DIV_TAG)
        select_items[drowdown_index].click()
        time.sleep(2)
    def enter_deleted_text_search(self, text):
        search_input = self.find_element(By.XPATH, self.DELETED_SEARCH_INPUT)
        self.enter_textbox_control(search_input,text)
    # popup method
    def all_search(self,request_number=-1,search_text="",expected_record_num_result=0):
        if request_number != -1:
            self.enter_all_drowdown_number(request_number)
        self.enter_all_text_search(search_text)
        table_content = self.find_element(By.XPATH,self.ALL_TABLE_CONTENT)
        rows = self.find_elements_from_node(table_content,By.TAG_NAME,"tr")
        if len(rows) == expected_record_num_result:
            return True
        else:
            return False
    def negotiating_search(self,
                           request_number=-1,
                           text_search="",
                           source=-1,
                           supplier=-1,
                           sale_person=-1,
                           picup_type=-1,
                           input_date=""):
        self.click_at_tab(3)
        if request_number >=1:
            self.enter_nego_drowdown_number(request_number)
        if text_search != "":
            self.enter_nego_text_search(text_search)
        if source != -1:
            self.enter_nego_source_dropdown(source)
        if supplier != -1:
            self.enter_nego_supplier_dropdown(supplier)
        if sale_person != -1:
            self.enter_nego_sale_pic(sale_person)
        if picup_type != -1:
            self.enter_nego_picup_dropdown(picup_type)
        if input_date != "":
            self.enter_nego_date_picker(input_date)
        table_content = self.find_element(By.XPATH, self.NEGO_TABLE_CONTENT)
        table_body = table_content.find_element(By.TAG_NAME,"tbody")
        rows = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        return len(rows)

    def unstock_search(self,
                           request_number=-1,
                           text_search="",
                           source=-1,
                           supplier=-1,
                           sale_person=-1,
                           picup_type=-1,
                           purpose=-1):
        self.click_at_tab(5)
        if request_number >= 1:
            self.enter_unstocked_drowdown_number(request_number)
        if text_search != "":
            self.enter_unstocked_text_search(text_search)
        if source != -1:
            self.enter_unstocked_source_dropdown(source)
        if supplier != -1:
            self.enter_unstocked_supplier_dropdown(supplier)
        if sale_person != -1:
            self.enter_unstocked_sale_pic(sale_person)
        if picup_type != -1:
            self.enter_unstocked_picup_dropdown(picup_type)
        if purpose != -1:
            self.enter_unstocked_purpose_dropdown(purpose)
        table_content = self.find_element(By.XPATH, self.UNSTOCK_TABLE_CONTENT)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        return len(rows)

    def storage_search(self,
                           request_number=-1,
                           text_search="",
                           source=-1,
                           warehouse_entering_date="",
                           warehouse =-1,
                           picup_type=-1,
                           supplier=-1,
                           purpose=-1):
        self.click_at_tab(7)
        if request_number >= 1:
            self.enter_storage_drowdown_number(request_number)
        if text_search != "":
            self.enter_storage_text_search(text_search)
        if source != -1:
            self.enter_storage_source_dropdown(source)
        if supplier != -1:
            self.enter_storage_supplier_dropdown(supplier)
        if picup_type != -1:
            self.enter_storage_picup_dropdown(picup_type)
        if warehouse_entering_date != "":
            self.enter_storage_pickup_ware_house_date(warehouse_entering_date)
        if warehouse != -1:
            self.enter_storage_whare_house_dropdown(warehouse)
        if purpose != -1:
            self.enter_storage_purpose_dropdown(purpose)
        table_content = self.find_element(By.XPATH, self.STORAGE_TABLE_CONTENT)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        return len(rows)
    def standby_search(self,
                           request_number=-1,
                           text_search="",
                           source=-1,
                           warehouse_leaving_date="",
                           car_maker = -1,
                           picup_type=-1,
                           purpose=-1):
        self.click_at_tab(9)
        if request_number >= 1:
            self.enter_standby_drowdown_number(request_number)
        if text_search != "":
            self.enter_standby_text_search(text_search)
        if source != -1:
            self.enter_standby_source_dropdown(source)
        if car_maker != -1:
            self.enter_standby_car_maker_dropdown(car_maker)
        if picup_type != -1:
            self.enter_standby_picup_dropdown(picup_type)
        if warehouse_leaving_date != "":
            self.enter_standby_pickup_ware_house_date(warehouse_leaving_date)
        if purpose != -1:
            self.enter_standby_purpose_dropdown(purpose)

    def inproduction_search(self,
                           request_number=-1,
                           text_search="",
                           source=-1,
                           processing_date="",
                           production_pic =-1,
                           picup_type=-1,
                           purpose=-1):
        self.click_at_tab(11)
        if request_number >= 1:
            self.enter_inproduction_drowdown_number(request_number)
        if text_search != "":
            self.enter_inproduction_text_search(text_search)
        if source != -1:
            self.enter_inproduction_source_dropdown(source)
        if processing_date != "":
            self.enter_inproduction_processing_date(processing_date)
        if production_pic != -1:
            self.enter_inproduction_pic_dropdown(production_pic)
        if picup_type != -1:
            self.enter_inproduction_picup_dropdown(picup_type)
        if purpose != -1:
            self.enter_inproduction_purpose_dropdown(purpose)

    def produced_search(self,
                           request_number=-1,
                           text_search="",
                           source=-1,
                           processing_date="",
                           car_maker =-1,
                           picup_type=-1,
                           purpose=-1):
        self.click_at_tab(13)
        if request_number >= 1:
            self.enter_produced_drowdown_number(request_number)
        if text_search != "":
            self.enter_produced_text_search(text_search)
        if source != -1:
            self.enter_produced_source_dropdown(source)
        if processing_date != "":
            self.enter_produced_processing_date(processing_date)
        if car_maker != -1:
            self.enter_produced_car_maker_dropdown(car_maker)
        if picup_type != -1:
            self.enter_produced_picup_dropdown(picup_type)
        if purpose != -1:
            self.enter_produced_purpose_dropdown(purpose)
    def not_purchased_search(self,
                           request_number=-1,
                           text_search="",
                           source=-1,
                           supplier  = -1,
                           sale_picker =-1,
                           picup_type=-1,
                           input_date=""):
        self.click_at_tab(15)
        if request_number >= 1:
            self.enter_not_purchased_drowdown_number(request_number)
        if text_search != "":
            self.enter_not_purchased_text_search(text_search)
        if source != -1:
            self.enter_not_purchased_source_dropdown(source)
        if supplier != -1:
            self.enter_not_purchased_supplier_dropdown(supplier)
        if sale_picker != -1:
            self.enter_not_purchased_sale_pic_dropdown(sale_picker)
        if picup_type != -1:
            self.enter_not_purchased_picup_dropdown(picup_type)
        if input_date != "":
            self.enter_not_purchased_input_date(input_date)
        table_content = self.find_element(By.XPATH, self.NOT_PURCHASED_TABLE_CONTENT)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        return len(rows)
    def deleted_search(self,request_number=-1,text_search=""):
        self.click_at_tab(17)
        if request_number >= 1:
            self.enter_deleted_drowdown_number(request_number)
        if str(text_search) != "":
            self.enter_deleted_text_search(str(text_search))
        time.sleep(2)
        table_content = self.find_element(By.XPATH, self.DELETED_TABLE_CONTENT)
        table_body = table_content.find_element(By.TAG_NAME, "tbody")
        rows = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        return len(rows)




    def negotiating_search_with_popup_filter(self,
                                             management_number="",
                                             car_maker="",
                                             car_name="",
                                             model="",
                                             year="",
                                             chasis_number="",
                                             mile_age = "",
                                             diplacement="",
                                             sale_pic="",
                                             supplier="",
                                             input_date="",
                                             picup_type=""
                                             ):
        time.sleep(1)
        self.enter_nego_filter()
        filter_poup = self.find_element(By.TAG_NAME, self.FILTER_POPUP_TAG)
        div_elements = filter_poup.find_elements(By.XPATH, "./*")
        if management_number != "" :
            self.enter_textbox_in_filter_dialog(div_elements[0],management_number)
        if car_maker != "":
            self.enter_drop_down_in_filter_dialog(div_elements[1],car_maker)
        if car_name != "":
            self.enter_drop_down_in_filter_dialog(div_elements[2], car_name)
        if model != "":
            self.enter_drop_down_in_filter_dialog(div_elements[3],model)
        if year != "":
            self.enter_range_dropdown_in_filter_dialog(div_elements[4],year)
        if chasis_number != "":
            self.enter_textbox_in_filter_dialog(div_elements[5],chasis_number)
        if mile_age != "":
            self.enter_text_range_in_filter_dialog(div_elements[6],mile_age)
        if diplacement != "":
            self.enter_text_range_in_filter_dialog(div_elements[7], diplacement)
        if sale_pic != "":
            self.enter_dropdown_by_option_value(div_elements[8],sale_pic)
        if supplier != "":
            self.enter_dropdown_by_option_value(div_elements[9], supplier)
        if input_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[10],input_date)
        if picup_type != "":
            self.enter_dropdown_by_option_value(div_elements[11], picup_type)
        element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(element, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(4)
        table_content = self.find_element(By.XPATH, self.NEGO_TABLE_CONTENT)
        rows = self.find_elements_from_node(table_content, By.TAG_NAME, "tr")
        return len(rows)
    def unstocked_search_with_popup_filter(self,
                                             management_number="",
                                             car_maker="",
                                             car_name="",
                                             model="",
                                             year="",
                                             chasis_number="",
                                             mile_age = "",
                                             diplacement="",
                                             sale_pic="",
                                             supplier="",
                                             picup_deadline="",
                                             transfer_request_date="",
                                             picup_request_number="",
                                             dismanting_certificate_required="",
                                             purpose="",
                                             warehouse = "",
                                             purchase_price = "",
                                             weight_tax="",
                                             input_date = "",
                                             picup_type=""

                                             ):
        time.sleep(1)
        self.enter_unstocked_filter()
        filter_poup = self.find_element(By.TAG_NAME, self.FILTER_POPUP_TAG)
        div_elements = filter_poup.find_elements(By.XPATH, "./*")
        if management_number != "" :
            self.enter_textbox_in_filter_dialog(div_elements[0], management_number)
        if car_maker != "":
            self.enter_drop_down_in_filter_dialog(div_elements[1], car_maker)
        if car_name != "":
            self.enter_drop_down_in_filter_dialog(div_elements[2], car_name)
        if model != "":
            self.enter_drop_down_in_filter_dialog(div_elements[3], model)
        if year != "":
            self.enter_range_dropdown_in_filter_dialog(div_elements[4],year)
        if chasis_number != "":
            self.enter_textbox_in_filter_dialog(div_elements[5],chasis_number)
        if mile_age != "":
            self.enter_text_range_in_filter_dialog(div_elements[6], mile_age)
        if diplacement != "":
            self.enter_text_range_in_filter_dialog(div_elements[7], diplacement)
        if sale_pic != "":
            self.enter_drop_down_in_filter_dialog(div_elements[8], sale_pic)
        if supplier != "":
            self.enter_drop_down_in_filter_dialog(div_elements[9], supplier)
        if picup_deadline != "":
            self.enter_text_range_in_filter_dialog(div_elements[10],picup_deadline)
        if transfer_request_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[11],transfer_request_date)
        if picup_request_number != "":
            self.enter_textbox_in_filter_dialog(div_elements[12],picup_request_number)
        if dismanting_certificate_required != "":
            self.enter_textbox_in_filter_dialog(div_elements[13], dismanting_certificate_required)
        if purpose != "":
            self.enter_textbox_in_filter_dialog(div_elements[14],purpose)
        if warehouse != "":
            self.enter_textbox_in_filter_dialog(div_elements[15],warehouse)
        if purchase_price != "":
            self.enter_text_range_in_filter_dialog(div_elements[16],purchase_price)
        if weight_tax != "":
            self.enter_text_range_in_filter_dialog(div_elements[17], weight_tax)
        if input_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[18], input_date)
        if picup_type != "":
            self.enter_drop_down_in_filter_dialog(div_elements[19],picup_type)
        element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(element, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(3)
        table_content = self.find_element(By.XPATH, self.UNSTOCK_TABLE_CONTENT)
        rows = self.find_elements_from_node(table_content, By.TAG_NAME, "tr")
        return len(rows)
    def storage_search_with_popup_filter(self,
                                             management_number="",
                                             car_maker="",
                                             car_name="",
                                             model="",
                                             year="",
                                             chasis_number="",
                                             mile_age = "",
                                             diplacement="",
                                             sale_pic="",
                                             supplier="",
                                             purpose="",
                                             warehouse = "",
                                             purchase_price = "",
                                             weight_tax="",
                                             freon_removed="",
                                             air_bag_removed="",
                                             input_date = "",
                                             ware_house_entering_date="",
                                             picup_type=""

                                             ):
        time.sleep(1)
        self.enter_storage_filter()
        filter_poup = self.find_element(By.TAG_NAME, self.FILTER_POPUP_TAG)
        div_elements = filter_poup.find_elements(By.XPATH, "./*")
        if management_number != "" :
            self.enter_textbox_in_filter_dialog(div_elements[0],management_number)
        if car_maker != "":
            self.enter_drop_down_in_filter_dialog(div_elements[1],car_maker)
        if car_name != "":
            self.enter_drop_down_in_filter_dialog(div_elements[2], car_name)
        if model != "":
            self.enter_drop_down_in_filter_dialog(div_elements[3], model)
        if year != "":
            self.enter_range_dropdown_in_filter_dialog(div_elements[4],year)
        if chasis_number != "":
            self.enter_textbox_in_filter_dialog(div_elements[5],chasis_number)
        if mile_age != "":
            self.enter_text_range_in_filter_dialog(div_elements[6],mile_age)
        if diplacement != "":
            self.enter_text_range_in_filter_dialog(div_elements[7], diplacement)
        if sale_pic != "":
            self.enter_drop_down_in_filter_dialog(div_elements[8], sale_pic)
        if supplier != "":
            self.enter_drop_down_in_filter_dialog(div_elements[9], supplier)
        if purpose != "":
            self.enter_drop_down_in_filter_dialog(div_elements[10], purpose)
        if warehouse != "":
            self.enter_drop_down_in_filter_dialog(div_elements[11], warehouse)
        if purchase_price != "":
            self.enter_text_range_in_filter_dialog(div_elements[12], purchase_price)
        if weight_tax != "":
            self.enter_text_range_in_filter_dialog(div_elements[13], weight_tax)
        if freon_removed != "":
            self.enter_drop_down_in_filter_dialog(div_elements[14],freon_removed)
        if air_bag_removed != "":
            self.enter_drop_down_in_filter_dialog(div_elements[15], freon_removed)
        if input_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[16],input_date)
        if ware_house_entering_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[17], ware_house_entering_date)
        if picup_type != "":
            self.enter_drop_down_in_filter_dialog(div_elements[18],picup_type)
        element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(element, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(2)
        table_content = self.find_element(By.XPATH, self.STORAGE_TABLE_CONTENT)
        rows = self.find_elements_from_node(table_content, By.TAG_NAME, "tr")
        return len(rows)

    def standby_search_with_popup_filter(self,
                                             management_number="",
                                             car_maker="",
                                             car_name="",
                                             model="",
                                             year="",
                                             chasis_number="",
                                             mile_age = "",
                                             diplacement="",
                                             sale_pic="",
                                             supplier="",
                                             purpose="",
                                             warehouse = "",
                                             purchase_price = "",
                                             freon_removed="",
                                             air_bag_removed="",
                                             input_date = "",
                                             ware_house_entering_date="",
                                             ware_house_leaving_date="",
                                             picup_type=""

                                             ):
        time.sleep(1)
        self.enter_standby_filter()
        filter_poup = self.find_element(By.TAG_NAME, self.FILTER_POPUP_TAG)
        div_elements = filter_poup.find_elements(By.XPATH, "./*")
        if management_number != "" :
            self.enter_textbox_in_filter_dialog(div_elements[0],management_number)
        if car_maker != "":
            self.enter_drop_down_in_filter_dialog(div_elements[1],car_maker)
        if car_name != "":
            self.enter_drop_down_in_filter_dialog(div_elements[2], car_name)
        if model != "":
            self.enter_drop_down_in_filter_dialog(div_elements[3], model)
        if year != "":
            self.enter_range_dropdown_in_filter_dialog(div_elements[4],year)
        if chasis_number != "":
            self.enter_textbox_in_filter_dialog(div_elements[5], chasis_number)
        if mile_age != "":
            self.enter_text_range_in_filter_dialog(div_elements[6],mile_age)
        if diplacement != "":
            self.enter_text_range_in_filter_dialog(div_elements[7], diplacement)
        if sale_pic != "":
            self.enter_drop_down_in_filter_dialog(div_elements[8], sale_pic)
        if supplier != "":
            self.enter_drop_down_in_filter_dialog(div_elements[9], supplier)
        if purpose != "":
            self.enter_textbox_in_filter_dialog(div_elements[10], purpose)
        if warehouse != "":
            self.enter_textbox_in_filter_dialog(div_elements[11], warehouse)
        if purchase_price != "":
            self.enter_text_range_in_filter_dialog(div_elements[12], purchase_price)
        if freon_removed != "":
            self.enter_drop_down_in_filter_dialog(div_elements[13], freon_removed)
        if air_bag_removed != "":
            self.enter_drop_down_in_filter_dialog(div_elements[14], air_bag_removed)
        if input_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[15],input_date)
        if ware_house_entering_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[16], ware_house_entering_date)
        if ware_house_leaving_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[17], ware_house_leaving_date)
        if picup_type != "":
            self.enter_drop_down_in_filter_dialog(div_elements[18],picup_type)
        element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(element, By.TAG_NAME, "button")
        buttons[1].click()
    def inproduction_search_with_popup_filter(self,
                                             management_number="",
                                             car_maker="",
                                             car_name="",
                                             model="",
                                             year="",
                                             chasis_number="",
                                             mile_age = "",
                                             diplacement="",
                                             purpose="",
                                             input_date = "",
                                             warehouse_leaving_date = "",
                                             processing_date = "",
                                             picup_type=""
                                             ):
        time.sleep(1)
        self.enter_inproduction_filter()
        filter_poup = self.find_element(By.TAG_NAME, self.FILTER_POPUP_TAG)
        div_elements = filter_poup.find_elements(By.XPATH, "./*")
        if management_number != "" :
            self.enter_textbox_in_filter_dialog(div_elements[0], management_number)
        if car_maker != "":
            self.enter_drop_down_in_filter_dialog(div_elements[1],car_maker)
        if car_name != "":
            self.enter_drop_down_in_filter_dialog(div_elements[2], car_name)
        if model != "":
            self.enter_drop_down_in_filter_dialog(div_elements[3], model)
        if year != "":
            self.enter_range_dropdown_in_filter_dialog(div_elements[4],year)
        if chasis_number != "":
            self.enter_textbox_in_filter_dialog(div_elements[5],chasis_number)
        if mile_age != "":
            self.enter_text_range_in_filter_dialog(div_elements[6],mile_age)
        if diplacement != "":
            self.enter_text_range_in_filter_dialog(div_elements[7], diplacement)
        if purpose != "":
            self.enter_textbox_in_filter_dialog(div_elements[8],purpose)
        if input_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[9],input_date)
        if warehouse_leaving_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[10], warehouse_leaving_date)
        if processing_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[11], processing_date)
        if picup_type != "":
            self.enter_drop_down_in_filter_dialog(div_elements[12],picup_type)
        element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(element, By.TAG_NAME, "button")
        buttons[1].click()

    def produced_search_with_popup_filter(self,
                                             management_number="",
                                             car_maker="",
                                             car_name="",
                                             model="",
                                             year="",
                                             chasis_number="",
                                             mile_age = "",
                                             diplacement="",
                                             purpose="",
                                             input_date = "",
                                             processing_date = "",
                                             picup_type=""
                                             ):
        time.sleep(1)
        self.enter_produced_filter()
        filter_poup = self.find_element(By.TAG_NAME, self.FILTER_POPUP_TAG)
        div_elements = filter_poup.find_elements(By.XPATH, "./*")
        if management_number != "" :
            self.enter_textbox_in_filter_dialog(div_elements[0],management_number)
        if car_maker != "":
            self.enter_drop_down_in_filter_dialog(div_elements[1],car_maker)
        if car_name != "":
            self.enter_drop_down_in_filter_dialog(div_elements[2], car_name)
        if model != "":
            self.enter_drop_down_in_filter_dialog(div_elements[3], model)
        if year != "":
            self.enter_range_dropdown_in_filter_dialog(div_elements[4],year)
        if chasis_number != "":
            self.enter_textbox_in_filter_dialog(div_elements[5], chasis_number)
        if mile_age != "":
            self.enter_text_range_in_filter_dialog(div_elements[6],mile_age)
        if diplacement != "":
            self.enter_text_range_in_filter_dialog(div_elements[7], diplacement)
        if purpose != "":
            self.enter_textbox_in_filter_dialog(div_elements[8],purpose)
        if input_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[9], input_date)
        if processing_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[10], processing_date)
        if picup_type != "":
            self.enter_drop_down_in_filter_dialog(div_elements[11],picup_type)
        element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(element, By.TAG_NAME, "button")
        buttons[1].click()
    def not_purchase_search_with_popup_filter(self,
                                             management_number="",
                                             car_maker="",
                                             car_name="",
                                             model="",
                                             year="",
                                             chasis_number="",
                                             mile_age = "",
                                             diplacement="",
                                             sale_pic="",
                                             supplier="",
                                             purpose="",
                                             input_date = "",
                                             picup_type=""
                                             ):
        time.sleep(1)
        self.enter_not_purchased_filter()
        filter_poup = self.find_element(By.TAG_NAME, self.FILTER_POPUP_TAG)
        div_elements = filter_poup.find_elements(By.XPATH, "./*")
        if management_number != "" :
            self.enter_textbox_in_filter_dialog(div_elements[0],management_number)
        if car_maker != "":
            self.enter_drop_down_in_filter_dialog(div_elements[1],car_maker)
        if car_name != "":
            self.enter_drop_down_in_filter_dialog(div_elements[2], car_name)
        if model != "":
            self.enter_drop_down_in_filter_dialog(div_elements[3], model)
        if year != "":
            self.enter_range_dropdown_in_filter_dialog(div_elements[4],year)
        if chasis_number != "":
            self.enter_textbox_in_filter_dialog(div_elements[5],chasis_number)
        if mile_age != "":
            self.enter_text_range_in_filter_dialog(div_elements[6],mile_age)
        if diplacement != "":
            self.enter_text_range_in_filter_dialog(div_elements[7], diplacement)
        if sale_pic != "":
            self.enter_drop_down_in_filter_dialog(div_elements[8], sale_pic)
        if supplier != "":
            self.enter_drop_down_in_filter_dialog(div_elements[9], supplier)
        if purpose != "":
            self.enter_textbox_in_filter_dialog(div_elements[10],purpose)
        if input_date != "":
            self.enter_text_range_in_filter_dialog(div_elements[11], input_date)
        if picup_type != "":
            self.enter_drop_down_in_filter_dialog(div_elements[9], picup_type)
        element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(element, By.TAG_NAME, "button")
        buttons[0].click()
        buttons[1].click()
    def get_car_detail(self,index=-1,chasis_number="",chasis_column_num=8):
        table_content_element = self.find_element(By.XPATH,"//*[contains(@class, 'ant-table-content')]")
        table_body = self.find_elements_from_node(table_content_element,By.TAG_NAME,"tbody")[0]
        items = self.find_elements_from_node(table_body,By.TAG_NAME,"tr")
        if index > 0:
            items[index].click()
        else:
            for item in items:
                tds = self.find_elements_from_node(item,By.TAG_NAME,"td")
                if tds[chasis_column_num].text.find(str(chasis_number))>=0:
                    item.click()
                    time.sleep(3)
                    break
        car_detail = CarDetail(self.driver)
        return car_detail
    def delete_multi_car_selection(self,num_car_delete):
        table_content_element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-table-content')]")
        table_body = self.find_elements_from_node(table_content_element, By.TAG_NAME, "tbody")[0]
        items = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        if num_car_delete > len(items):
            num_car_delete = len(items)
        for i in range(num_car_delete):
            delete_index = random.randint(1,num_car_delete-1)
            tds = items[delete_index].find_elements(By.TAG_NAME,"td")
            tds[0].click()

        delete_button = self.find_element(By.XPATH,self.ALL_MULTIPLE_DELETE)
        delete_button.click()
        div_content = self.find_element(By.CLASS_NAME,"ant-popover-buttons")
        buttons = div_content.find_elements(By.TAG_NAME,"button")
        buttons[0].click()
    def storage_batch(self,number_of_car):
        self.click_at_tab(5)
        table_content_element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-table-content')]")
        table_body = self.find_elements_from_node(table_content_element, By.TAG_NAME, "tbody")[0]
        items = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        if number_of_car > len(items):
            number_of_car = len(items)
        for i in range(number_of_car):
            delete_index = random.randint(1,number_of_car-1)
            tds = items[delete_index].find_elements(By.TAG_NAME,"td")
            tds[0].click()
        storage_button = self.find_element(By.XPATH,self.UNSTOCK_STORAGE_BUTTON)
        storage_button.click()
        footer = self.find_element(By.XPATH, "//div[contains(@class, 'ant-modal-footer')]")
        buttons = footer.find_elements(By.TAG_NAME,"button")
        buttons[1].click()
    def storage_car(self,chasis_number):
        self.click_at_tab(5)
        table_content_element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-table-content')]")
        table_body = self.find_elements_from_node(table_content_element, By.TAG_NAME, "tbody")[0]
        trs = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME,"td")
            if tds[6].text == chasis_number:
                check_box = tds[0].find_element(By.TAG_NAME,"input")
                check_box.click()
                break
        storage_button = self.find_element(By.XPATH, self.UNSTOCK_STORAGE_BUTTON)
        storage_button.click()
        footer = self.find_element(By.XPATH, "//div[contains(@class, 'ant-modal-footer')]")
        buttons = footer.find_elements(By.TAG_NAME, "button")
        buttons[1].click()
    def do_document_car(self,chasis_number,reason_for_process,transfer_date=""):

        table_content_element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-table-content')]")
        table_body = self.find_elements_from_node(table_content_element, By.TAG_NAME, "tbody")[0]
        trs = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME, "td")
            if tds[6].text == chasis_number:
                check_box = tds[0].find_element(By.TAG_NAME, "input")
                check_box.click()
                break
        title_footer = self.find_element(By.TAG_NAME,"nz-table-title-footer")
        button = title_footer.find_element(By.TAG_NAME,"button")
        button.click()
        time.sleep(1)
        popup_window = self.find_element(By.TAG_NAME,"app-popup-document-complete")
        drop_down_reason = popup_window.find_element(By.TAG_NAME,"app-select-option-value")
        drop_down_reason.click()
        input = drop_down_reason.find_element(By.TAG_NAME,"input")
        input.send_keys(reason_for_process)
        input.send_keys(Keys.ENTER)
        if transfer_date != "":
            app_date_picker = popup_window.find_element(By.TAG_NAME,"app-date-picker")
            input = app_date_picker.find_element(By.TAG_NAME,"input")
            input.send_keys(transfer_date)
            input.send_keys(Keys.ENTER)
        footer = self.find_element(By.XPATH, "//div[contains(@class, 'ant-modal-footer')]")
        buttons = footer.find_elements(By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(2)
        popup_confirm = self.find_element(By.XPATH, "//div[contains(@class, 'ant-modal-content')]")
        buttons = popup_confirm.find_elements(By.TAG_NAME, "button")
        self.driver.execute_script("arguments[0].click();",buttons[1])






















