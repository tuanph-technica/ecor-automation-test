import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from selenium.webdriver.support.ui import Select



class CarRegistration(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)


    CAR_MAKER_NAME_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[1]/td[2]/app-select-car-maker/nz-select/nz-select-top-control/nz-select-search/input"
    CAR_CAR_NAME_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[1]/td[4]/app-select-car-name/nz-select/nz-select-top-control/nz-select-search/input"
    CAR_MODEL_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[2]/td[2]/app-select-car-data-model/nz-select/nz-select-top-control/nz-select-search/input"
    CAR_YEAR_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[2]/td[4]/app-select-year/nz-select/nz-select-top-control/nz-select-search/input"
    CAR_BODY_TYPE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[3]/td[2]/app-select-vehicle-type/nz-select/nz-select-top-control/nz-select-search"
    CAR_BODY_TYPE_VALUE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[3]/td[2]/app-select-vehicle-type/nz-select/nz-select-top-control/nz-select-search/input"
    CAR_GRADE_FIELD =     "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[3]/td[4]/app-select-car-master-grade/nz-select/nz-select-top-control/nz-select-search"
    CAR_GRADE_VALUE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[3]/td[4]/app-select-car-master-grade/nz-select/nz-select-top-control/nz-select-search/input"
    CAR_CHASIS_NUMBER_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[4]/td[2]/nz-row/nz-col/app-input-text/input"
    CAR_MILEAGE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[4]/td[4]/app-input-number/nz-input-number/div[2]/input"
    CAR_DISPLACEMENT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[5]/td[2]/app-input-number/nz-input-number/div[2]/input"
    CAR_WEIGHT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[5]/td[4]/app-input-number/nz-input-number/div[2]/input"
    SALES_PIC_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[6]/td[4]/app-select-sale-pic/nz-select/nz-select-top-control/nz-select-search/input"
    SUPPLIER_NAME_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[6]/td[4]/app-select-sale-pic/nz-select/nz-select-top-control/nz-select-search/input"
    EVALUATION_POINT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[1]/td[2]/app-select-option-value/nz-select/nz-select-top-control/nz-select-search"
    EVALUATION_POINT_VALUE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[1]/td[2]/app-select-option-value/nz-select/nz-select-top-control/nz-select-search/input"
    EXTERIAL_CONDITION_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[2]/td[2]/app-select-option-value/nz-select/nz-select-top-control/nz-select-search"
    EXTERIAL_CONDITION_VALUE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[2]/td[2]/app-select-option-value/nz-select/nz-select-top-control/nz-select-search/input"
    REPAIR_HISTORY_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[1]/td[4]/label"
    INTERNAL_CONDITION_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[2]/td[4]/app-select-option-value/nz-select/nz-select-top-control/nz-select-search"
    INTERNAL_CONDITION_VALUE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[2]/td[4]/app-select-option-value/nz-select/nz-select-top-control/nz-select-search/input"
    IMMOVABLE_SUSPENSION_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[3]/td[2]/label"
    IMMOVABLE_ENGINE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[6]/td[2]/label"
    IMMOVABLE_ACCIDENT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[7]/td[2]/label"
    IMMOVABLE_BATTERY_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[8]/td[2]/label"
    IMMOVABLE_OTHERS_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[9]/td[2]/label"
    INTERNAL_MEMO_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[1]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-textarea-count/textarea"
    BUTTON_CANCEL = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[1]/nz-col/nz-row/nz-space/div[1]/button/span"
    BUTTON_CREATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[1]/nz-col/nz-row/nz-space/div[3]/button"
    ALL_GRADES = "/html/body/div[2]/div/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[@class = 'ant-select-item-option-content']"
    BUTTON_EXCLUDE_PART = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[1]/div/app-excluded-parts/nz-card/div[1]/div/div[2]/button"
    PART_CAREGORIES_FIELD = "/html/body/div/div[2]/div/nz-modal-container/div/div/div[2]/app-popup-edit-exclude-parts/nz-row[2]/nz-col[1]/nz-list/nz-spin/div/div"
    ELEMENT_PART_FIELD =    "/html/body/div/div[2]/div/nz-modal-container/div/div/div[2]/app-popup-edit-exclude-parts/nz-row[2]/nz-col[2]/div"
    BUTTON_SELECT_PART =    "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]"
    LANGUAGE_CONTENT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-header/app-header/div/nz-row/nz-col[4]/div/div[2]/div"
    EXCLUDE_PARTS_OK_BUTTON = "/html/body/div[2]/div[3]/div/nz-modal-container/div/div/div[2]/button[2]"
    EXCLUDE_PART_CONTENT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-registration/nz-row[2]/nz-col[1]/div/app-excluded-parts/nz-card/div[2]/div"
    def get_language_content(self):
        time.sleep(2)
        return self.find_element(By.XPATH,self.LANGUAGE_CONTENT_FIELD)

    def get_maker_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_MAKER_NAME_FIELD)
    def get_car_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_CAR_NAME_FIELD)
    def get_car_model(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_MODEL_FIELD)
    def get_car_year(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_YEAR_FIELD)
    def get_car_body(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_BODY_TYPE_FIELD)

    def get_car_grade(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_GRADE_FIELD)
    def get_car_grade_value(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.CAR_GRADE_VALUE_FIELD)
    def get_car_chasis_number(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_CHASIS_NUMBER_FIELD)
    def get_car_mileage(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_MILEAGE_FIELD)
    def get_car_displacement(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_DISPLACEMENT_FIELD)
    def get_weight(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CAR_WEIGHT_FIELD)

    def get_sales_pic(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SALES_PIC_FIELD)
    def get_supplier_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SUPPLIER_NAME_FIELD)
    def get_car_evaluation_point(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EVALUATION_POINT_FIELD)
    def get_car_external_evaluation(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXTERIAL_CONDITION_FIELD)
    def get_car_repair_history(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.REPAIR_HISTORY_FIELD)
    def get_car_internal_evaluation(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.INTERNAL_CONDITION_FIELD)
    def get_immoveable_suspension(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.IMMOVABLE_SUSPENSION_FIELD)

    def get_immoveable_engine(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.IMMOVABLE_ENGINE_FIELD)
    def get_immoveable_accident(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.IMMOVABLE_ACCIDENT_FIELD)
    def get_immoveable_battery(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.IMMOVABLE_BATTERY_FIELD)
    def get_immoveable_others(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.IMMOVABLE_OTHERS_FIELD)
    def get_car_internal_memo(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.INTERNAL_MEMO_FIELD)
    def get_button_cancel(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CANCEL)
    def get_button_suucess(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CREATE)
    def get_button_exclude_part_ok(self):
        buttons = self.find_elements(By.TAG_NAME,"button")
        return buttons[6]
    def get_button_part_exclude(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.BUTTON_EXCLUDE_PART)
    def get_exclude_part_content(self):
        return self.find_element(By.XPATH,self.EXCLUDE_PART_CONTENT_FIELD)
    def enter_car_maker(self,car_maker):
        self.get_maker_name().click()
        time.sleep(3)
        self.get_maker_name().send_keys(car_maker)
        self.get_maker_name().send_keys(Keys.ENTER)
    def enter_car_name(self,car_name):
        self.get_car_name().click()
        time.sleep(2)
        self.get_car_name().send_keys(car_name)
        self.get_car_name().send_keys(Keys.ENTER)
    def enter_car_model(self,model_name):
        self.get_car_model().click()
        time.sleep(3)
        self.get_car_model().send_keys(model_name)
        self.get_car_model().send_keys(Keys.ENTER)
    def enter_car_year(self,year):
        self.get_car_year().click()
        time.sleep(3)
        self.get_car_year().send_keys(year)
        self.get_car_year().send_keys(Keys.ENTER)
    def enter_car_grade(self,grade):
        self.get_car_grade().click()
        time.sleep(2)
        element = self.find_element(By.XPATH,self.CAR_GRADE_VALUE_FIELD)
        element.send_keys(grade)
        element.send_keys(Keys.ENTER)
    def enter_vehicle_type(self,vehicle_type):
        self.get_car_body().click()
        time.sleep(2)
        element = self.find_element(By.XPATH,self.CAR_BODY_TYPE_VALUE_FIELD)
        element.send_keys(vehicle_type)
        element.send_keys(Keys.ENTER)

    def enter_car_chasis_number(self,chasis_number):
        self.get_car_chasis_number().click()

        self.get_car_chasis_number().send_keys(Keys.CONTROL + "a")
        self.get_car_chasis_number().send_keys(Keys.DELETE)
        time.sleep(1)
        self.get_car_chasis_number().send_keys(chasis_number)
        self.get_car_chasis_number().send_keys(Keys.ENTER)
    def enter_car_mileage(self,mileage):
        self.get_car_mileage().click()
        time.sleep(3)
        self.get_car_mileage().send_keys(mileage)
        self.get_car_mileage().send_keys(Keys.ENTER)
    def enter_car_displacement(self,displacement):
        self.get_car_displacement().click()
        time.sleep(3)
        self.get_car_displacement().send_keys(Keys.CONTROL, 'a')
        self.get_car_displacement().send_keys(Keys.BACKSPACE)
        self.get_car_displacement().send_keys(displacement)
        self.get_car_displacement().send_keys(Keys.ENTER)
    def enter_car_weight(self,weight):
        self.get_weight().click()
        self.get_weight().send_keys(Keys.CONTROL + "a")
        self.get_weight().send_keys(Keys.BACK_SPACE)
        time.sleep(3)
        self.get_weight().send_keys(weight)
        self.get_weight().send_keys(Keys.ENTER)
    def enter_supplier_name(self,supplier_name):
        parent_elements = self.find_elements(By.CLASS_NAME, 'ant-descriptions-row')
        click_element = parent_elements[8]
        tds = click_element.find_elements(By.TAG_NAME, "td")
    def enter_color(self,color_index):
        parent_elements = self.find_elements(By.CLASS_NAME,'ant-descriptions-row')
        click_element = parent_elements[5]
        tds = click_element.find_elements(By.TAG_NAME,"td")
        tds[1].click()
        time.sleep(3)
        parent_options = self.find_elements(By.CLASS_NAME,"cdk-virtual-scroll-content-wrapper")
        color_options = parent_options[0].find_elements(By.TAG_NAME,"nz-option-item")
        color_index = int(color_index)
        if color_index < 12:
            color_options[color_index].click()

    def enter_minor_change(self,minor_change):
        return 0
    def enter_purpose(self,purpose):
        return 0
    def enter_supplier_type(self,supplier_type):
        return 0
    def enter_supplier_address(self,address):
        return 0
    def enter_evaluation_point(self,evaluation_point):
        self.get_car_evaluation_point().click()
        time.sleep(3)
        parent_element = self.find_element(By.TAG_NAME,"cdk-virtual-scroll-viewport")
        options = parent_element.find_elements(By.TAG_NAME,'nz-option-item')
        for option in options:
            if option.text == evaluation_point:
                option.click()
                break
    def repaire_history_checked(self,checked):
        self.get_car_repair_history().click()
        time.sleep(3)
    def enter_car_int(self,quality):
        self.get_car_internal_evaluation().click()
        time.sleep(3)
        parent_element = self.find_element(By.TAG_NAME, "cdk-virtual-scroll-viewport")
        options = parent_element.find_elements(By.TAG_NAME, 'nz-option-item')
        options[quality-1].click()

    def enter_car_ext(self,quality):
        self.get_car_external_evaluation().click()
        time.sleep(3)
        parent_element = self.find_element(By.TAG_NAME, "cdk-virtual-scroll-viewport")
        options = parent_element.find_elements(By.TAG_NAME, 'nz-option-item')
        options[quality - 1].click()
    def enter_immoveable_suspension(self,value):
        if value == 1:
            chk_boxes = self.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
            chk_boxes[1].click()
        time.sleep(2)
    def enter_immoveable_engine(self,value):
        if value == 1:
            chk_boxes = self.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
            chk_boxes[2].click()
    def enter_immoveable_accident(self,value):
        if value == 1:
            chk_boxes = self.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
            chk_boxes[3].click()
    def enter_immoveable_battery(self,value):
        if value == 1:
            chk_boxes = self.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
            chk_boxes[4].click()
        time.sleep(2)

    def enter_immoveable_others(self,value):
        if value == 1:
            chk_boxes = self.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
            chk_boxes[5].click()
    def enter_internal_memo(self,memo):
        self.get_car_internal_memo().click()
        time.sleep(2)
        self.get_car_internal_memo().send_keys(memo)
        self.get_car_internal_memo().send_keys(Keys.ENTER)
    def enter_part_exclude(self):
        self.get_button_part_exclude().click()
        time.sleep(5)
        element_checkboxes = self.find_elements(By.TAG_NAME,'nz-spin')
        child_categories = element_checkboxes[0].find_elements(By.TAG_NAME,"input")
        child_categories[0].click()
        time.sleep(2)
        child_categories[2].click()
        time.sleep(2)
        buttons = self.find_elements(By.TAG_NAME,"button")
        for button in buttons:
            if button.text == '適用':
                button.click()
                break
        time.sleep(3)
    def click_exclude_part_button(self):
        time.sleep(2)
        self.get_button_exclude_part().click()

    def click_ok_button(self):
        self.get_button_suucess().click()
    def get_page_language(self):
        element = self.get_language_content()
        language_labels = self.find_elements_from_node(element,By.TAG_NAME,'label')
        if len(language_labels) > 0:
            return language_labels[0].text
        else:
            return 'JP'
    def is_exclude_parts_presents(self):
        exclude_part_contents = self.get_exclude_part_content()
        childs = self.find_elements_from_node(exclude_part_contents,By.TAG_NAME,"button")
        if len(childs) > 0 :
            return True
        else:
            return False
    def do_registration(self,maker_name,car_name,car_model,production_year,
        chasis_no="",
        car_grade="",
        vehicle_type = "",
        displacement = "",
        car_weight = "",
        mileage = "",
        color = -1,
        minor_change = '',
        purpose = '',
        supplier_type = 1,
        supplier_name = "",
        supplier_address = '',
        evaluation_point="",
        repaire_history = "",
        int_valuation = "",
        ex_valuation = "",
        immove_suspension = "",
        immove_engine = "",
        immove_accident ="",
        immove_battery = "",
        immove_others = "",
        intenal_memo = "",
        exclude_part = False
                        ):
        try:
            self.enter_car_maker(maker_name)
            self.enter_car_name(car_name)
            self.enter_car_model(car_model)
            self.enter_car_year(production_year)
            if chasis_no != "":
                self.enter_car_chasis_number(chasis_no)
            if car_grade is not None and car_grade != "":
                self.enter_car_grade(car_grade)
            if vehicle_type != "":
                self.enter_vehicle_type(vehicle_type)
            if displacement != "":
                self.enter_car_displacement(displacement)
            if car_weight != "":
                self.enter_car_weight(car_weight)
            if mileage != "":
                self.enter_car_mileage(mileage)
            if color is not None:
                self.enter_color(color)
            if minor_change != "":
                self.enter_minor_change(minor_change)
            if purpose != "":
                self.enter_purpose(purpose)
            if supplier_type != "":
                self.enter_supplier_type(supplier_type)
            if supplier_address != "":
                self.enter_supplier_address(supplier_address)
            if supplier_name != "":
                self.enter_supplier_name(supplier_name)
            if evaluation_point != "":
                self.enter_evaluation_point(evaluation_point)
            if repaire_history != "":
                self.repaire_history_checked(repaire_history)
            if int_valuation != "":
                self.enter_car_int(int_valuation)
            if ex_valuation != "":
                self.enter_car_ext(ex_valuation)
            if immove_suspension != "":
                self.enter_immoveable_suspension(immove_suspension)
            if immove_engine != "":
                self.enter_immoveable_engine(immove_engine)
            if immove_accident != "":
                self.enter_immoveable_accident(immove_accident)
            if immove_battery != "":
                self.enter_immoveable_battery(immove_battery)
            if immove_others != "":
                self.enter_immoveable_others(immove_others)

            if intenal_memo != "":
                self.enter_internal_memo(intenal_memo)
            rnd_exclude_part = random.randint(0,1)
            if rnd_exclude_part == 1:
                exclude_part = True
            else:
                exclude_part = False
            if exclude_part == True:
                self.enter_part_exclude()
            self.click_ok_button()
            if exclude_part == False:
                self.get_button_exclude_part_ok().click()
            return 1
        except Exception as error:
            print("An exception occurred:", error)
            return 0








