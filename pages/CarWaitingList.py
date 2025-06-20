from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from base.base_driver import BaseDriver
from pages.CarValuationDetail import CarValuationDetail
from pages.ProductPlaneDetail import CreateProductPlan


class CarWaitingList(BaseDriver):
    DROPDOWN_CONTENT_LIST_TAG = "cdk-virtual-scroll-viewport"
    TABLE_CONTENT_CLASS_NAME = "ant-table-content"


    def __init__(self,driver,department_name):
        super().__init__(driver)
        self.department_name = department_name
        self.PICKUP_REQUEST_NUMBER = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name +"/nz-card/div/app-waiting-list-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[1]/nz-select/nz-select-top-control"
        self.INPUT_TEXT_SEARCH = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-card/div/app-waiting-list-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
        self.PRODUCTION_FLOW_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-card/div/app-waiting-list-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[1]/app-select-option-value"
        self.PRODUCTION_STATUS_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-card/div/app-waiting-list-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-select-option-value"
        self.WAREHOUSE_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-card/div/app-waiting-list-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[2]/app-select-option-value"
        self.FILTER_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-card/div/app-waiting-list-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[1]"
        self.RESET_BUTTON =  "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-card/div/app-waiting-list-filter/nz-row[1]/nz-col[2]/nz-row/nz-col[3]/nz-row/nz-col[2]/button[2]"
        self.BACK_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-header/app-header/div/nz-row/nz-col[2]/button"
        if department_name == "domestic":
            self.BUTTON_CREATE_PLAN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-row/nz-col/nz-space/button"
        elif department_name == "export":
            self.BUTTON_CREATE_PLAN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-row/nz-col/nz-space/div/button"
        elif department_name == "agp":
            self.BUTTON_CREATE_PLAN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-row/nz-col/nz-space/div/button"
        elif department_name == "material":
            self.BUTTON_CREATE_PLAN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-waiting-list/app-waiting-list-" + department_name + "/nz-row/nz-col/nz-space/div/button"
    def enter_web_item_text(self, text_element, text_value):
         text_element.send_keys(Keys.CONTROL + "a")  # Select all
         text_element.send_keys(Keys.DELETE)  # Delete selected text
         text_element.send_keys(text_value)
         text_element.send_keys(Keys.ENTER)
         time.sleep(2)
    def enter_web_item_drop_down(self,dropdown_element,option_text):
        time.sleep(2)
        dropdown_element.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.TAG_NAME, self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        if isinstance(option_text,int):
            dropdown_items[option_text].click()
        else:
            for item in dropdown_items:
                if item.text == option_text:
                    item.click()
                    break

        time.sleep(2)
    def enter_web_item_drop_down_random(self,dropdown_element,option_index):
        time.sleep(2)
        dropdown_element.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.TAG_NAME, self.DROPDOWN_CONTENT_LIST_TAG)
        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        dropdown_items[option_index].click()
        time.sleep(2)


    def enter_web_item_button(self,button_element):
        button_element.click()
        time.sleep(2)
    def search_waiting_list(self, management="",
                            text_search="",
                            production_flow="",
                            production_status="",
                            ware_house=""):
        if management != "":
            requestment_dropdown = self.find_element(By.XPATH,self.PICKUP_REQUEST_NUMBER)
            self.enter_web_item_drop_down(requestment_dropdown,management)
        if text_search != "":
            text_search_element = self.find_element(By.XPATH,self.INPUT_TEXT_SEARCH)
            self.enter_web_item_text(text_search_element,text_search)
        if production_flow != "":
            production_dropdown = self.find_element(By.XPATH,self.PRODUCTION_FLOW_DROPDOWN)
            self.enter_web_item_drop_down(production_dropdown,production_flow)
        if production_status != "":
            production_status_dropdown = self.find_element(By.XPATH,self.PRODUCTION_STATUS_DROPDOWN)
            self.enter_web_item_drop_down(production_status_dropdown, production_status)


        time.sleep(1)
        table = self.find_element(By.XPATH, "//*[contains(@class, 'ant-table-content')]")
        table_body = table.find_element(By.TAG_NAME, "tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        return len(rows)
    def go_back_to_plan(self):
        back_button = self.find_element(By.XPATH,self.BACK_BUTTON)
        self.enter_web_item_button(back_button)
    def enter_text_in_modal_dialog(self, web_element,text_value):
        web_element.click();
        time.sleep(3)
        txt_element = self.find_elements_from_node(web_element, By.TAG_NAME, "input")[0]
        txt_element.send_keys(Keys.CLEAR)
        txt_element.send_keys(text_value)
        txt_element.send_keys(Keys.ENTER)
        time.sleep(2)
    def enter_dropdown_in_modal_dialog(self,web_element,option_value):
        web_element.click();
        time.sleep(2)
        car_maker_dropdown = self.find_elements_from_node(web_element, By.TAG_NAME, "nz-select-top-control")
        car_maker_dropdown[0].click()
        dropdown_content = self.find_element(By.TAG_NAME, "cdk-virtual-scroll-viewport")
        dropdown_items = self.find_elements_from_node(dropdown_content, By.TAG_NAME, "nz-option-item")
        for item in dropdown_items:
            if item.text == option_value:
                item.click()
                break

        time.sleep(2)
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
    def search_waiting_list_using_filter(self,management_number="",
                                         chasis_number="",
                                         car_maker="",
                                         car_name = "",
                                         model="",
                                         year="",
                                         category="",
                                         ware_house ="",
                                         ware_house_date = "",
                                         production_flow = "",
                                         production_status = "",
                                         buyer = -1,
                                         production_method = "",
                                         picup_reuest_num = ""):
        header = self.find_element(By.TAG_NAME,"app-waiting-list-filter")
        buttons = header.find_elements(By.TAG_NAME,"button")
        buttons[0].click()
        time.sleep(3)
        dialog_content = self.find_element(By.TAG_NAME, "app-filter-popup")
        items = self.find_elements_from_node(dialog_content, By.XPATH, "./*")
        if management_number != "":
            self.enter_text_in_modal_dialog(items[0], management_number)
        if chasis_number != "":
            self.enter_text_in_modal_dialog(items[1], chasis_number)
        if car_maker != "":
            self.enter_dropdown_in_modal_dialog(items[2], car_maker)
        if car_name != "":
            self.enter_dropdown_in_modal_dialog(items[3], car_name)
        if model != "":
            self.enter_dropdown_in_modal_dialog(items[4], model)
        if year != "":
            self.enter_range_textbox_dialog(items[5], year)
        if category != "" :
            self.enter_dropdown_in_modal_dialog(items[6], category)
        if ware_house != "":
            self.enter_dropdown_in_modal_dialog(items[7], ware_house)
        if ware_house_date != "":
            self.enter_range_textbox_dialog(items[8], ware_house_date)
        if production_flow != "":
            self.enter_dropdown_in_modal_dialog(items[9], production_flow)
        if production_status != "" :
            self.enter_dropdown_in_modal_dialog(items[10], production_status)
        if picup_reuest_num != "":
            if self.department_name == "domestic" or self.department_name == "agp":
                self.enter_text_in_modal_dialog(items[11], picup_reuest_num)
            else:
                self.enter_text_in_modal_dialog(items[12], picup_reuest_num)
        if buyer >= 0:
            if self.department_name == "export":
                self.enter_dropdown_in_modal_dialog(items[11], production_flow)
        if production_method != "":
            if self.department_name == "material":
                self.enter_dropdown_in_modal_dialog(items[11],production_method)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(footer_area, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(2)
        table = self.find_element(By.XPATH, "//*[contains(@class, 'ant-table-content')]")
        table_body = table.find_element(By.TAG_NAME, "tbody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        return len(rows)

    def select_item_from_waiting_list(self,waiting_index):
        table_content_element = self.find_element(By.CLASS_NAME, self.TABLE_CONTENT_CLASS_NAME)
        table_body = self.find_elements_from_node(table_content_element, By.TAG_NAME, "tbody")[0]
        tr_elements = self.find_elements_from_node(table_body, By.TAG_NAME, "tr")
        tr_elements[waiting_index].click()
        time.sleep(3)
    def do_reset_search(self):
        header = self.find_element(By.TAG_NAME,"app-waiting-list-filter")
        buttons = header.find_elements(By.TAG_NAME,"button")
        button_reset = buttons[-1]
        button_reset.click()
        time.sleep(2)
    def create_new_plan_domestic(self, working_date = "", working_persons ="", working_hours=-1,working_minutes=-1):

            create_plan_button = self.find_element(By.XPATH,self.BUTTON_CREATE_PLAN)
            create_plan_button.click()
            time.sleep(3)
            body_content = self.find_element(By.TAG_NAME,"app-popup-working-persons-time-domestic")
            if working_date != "":
                date_picker = body_content.find_element(By.TAG_NAME,"app-date-picker-create-plan")
                txt_date = date_picker.find_element(By.TAG_NAME,"input")
                self.enter_web_item_text(txt_date,working_date)


            if working_persons != "":
                div_worker = body_content.find_element(By.TAG_NAME,"app-input-number")
                txt_worker = div_worker.find_element(By.TAG_NAME,"input")
                self.enter_web_item_text(txt_worker,working_persons)
            if working_hours != -1:
                ddl_working_hours = body_content.find_elements(By.TAG_NAME,"app-select-option-value")[0]
                ddl_working_hours.click()
                time.sleep(3)
                self.enter_dropdown_in_modal_dialog(ddl_working_hours, working_hours)


            if working_minutes != -1:
                ddl_working_minutes = body_content.find_elements(By.TAG_NAME,"app-select-option-value")[1]
                ddl_working_minutes.click()
                time.sleep(3)
                self.enter_dropdown_in_modal_dialog(ddl_working_minutes, working_minutes)
            footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
            buttons = self.find_elements_from_node(footer_area, By.TAG_NAME, "button")
            buttons[1].click()
            time.sleep(2)
            createProductPlan = CreateProductPlan(self.driver,self.department_name)
            return createProductPlan
    def create_new_plan_export(self,
                               plan_date = "",
                               AGP=False,
                               DB=False,
                               JOR=False,
                               PG1=False,
                               KABIR=False,
                               CEBU=False,
                               DOM=False,
                               BKK=False,
                               TI_GBE=False,
                               Other=False):
        create_plan_button = self.find_element(By.XPATH, self.BUTTON_CREATE_PLAN)
        create_plan_button.click()
        time.sleep(3)
        body_content = self.find_element(By.TAG_NAME, "app-popup-working-persons-time-export")
        if plan_date != "":
            dt_working_date = body_content.find_element(By.TAG_NAME,"app-date-picker-create-plan")
            input_date = dt_working_date.find_element(By.TAG_NAME,"input")
            self.enter_web_item_text(input_date, plan_date)
        table_body = body_content.find_element(By.TAG_NAME,"tbody")
        trs = table_body.find_elements(By.TAG_NAME,"tr")
        if AGP:
            tds = trs[1].find_elements(By.TAG_NAME,"td")
            work_person_input = tds[1].find_elements(By.TAG_NAME,"input")[0]
            self.enter_web_item_text(work_person_input,str(random.randint(1,5)))
            dropdowns = tds[2].find_elements(By.TAG_NAME,"app-select-option-value")
            self.enter_web_item_drop_down_random(dropdowns[0],random.randint(1,11))
            self.enter_web_item_drop_down_random(dropdowns[1], random.randint(1, 3))
        if DB:
            tds = trs[2].find_elements(By.TAG_NAME, "td")
            work_person_input = tds[1].find_elements(By.TAG_NAME, "input")[0]
            self.enter_web_item_text(work_person_input, str(random.randint(1, 5)))
            dropdowns = tds[2].find_elements(By.TAG_NAME, "app-select-option-value")
            self.enter_web_item_drop_down_random(dropdowns[0], random.randint(1, 11))
            self.enter_web_item_drop_down_random(dropdowns[1], random.randint(1, 3))
        if JOR:
            tds = trs[3].find_elements(By.TAG_NAME, "td")
            work_person_input = tds[1].find_elements(By.TAG_NAME, "input")[0]
            self.enter_web_item_text(work_person_input, str(random.randint(1, 5)))
            dropdowns = tds[2].find_elements(By.TAG_NAME, "app-select-option-value")
            self.enter_web_item_drop_down_random(dropdowns[0], random.randint(1, 11))
            self.enter_web_item_drop_down_random(dropdowns[1], random.randint(1, 3))
        if PG1:
            tds = trs[4].find_elements(By.TAG_NAME, "td")
            work_person_input = tds[1].find_elements(By.TAG_NAME, "input")[0]
            self.enter_web_item_text(work_person_input, str(random.randint(1, 5)))
            dropdowns = tds[2].find_elements(By.TAG_NAME, "app-select-option-value")
            self.enter_web_item_drop_down_random(dropdowns[0], random.randint(1, 11))
            self.enter_web_item_drop_down_random(dropdowns[1], random.randint(1, 3))
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(footer_area, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(2)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(footer_area, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(2)
        createProductPlan = CreateProductPlan(self.driver,self.department_name)
        return createProductPlan
    def get_all_car_chasis_number(self):
        table = self.find_element(By.XPATH,"//*[contains(@class, 'ant-table-content')]")
        table_body =  table.find_element(By.TAG_NAME,"tbody")
        rows = table_body.find_elements(By.TAG_NAME,"tr")
        chasis_num_column_index = 3
        lst_chasis_number = []
        for row in rows:
            tds = row.find_elements(By.TAG_NAME, "td")
            if len(tds) > chasis_num_column_index:
                if tds[chasis_num_column_index].text != "":
                    lst_chasis_number.append(tds[chasis_num_column_index].text)
        return lst_chasis_number

    def create_new_plan_material(self,working_date = "", working_persons ="", working_hours=-1,working_minutes=-1):
        create_plan_button = self.find_element(By.XPATH, self.BUTTON_CREATE_PLAN)
        create_plan_button.click()
        time.sleep(3)
        body_content = self.find_element(By.TAG_NAME, "app-popup-working-persons-time-material")
        if working_date != "":
            date_picker = body_content.find_element(By.TAG_NAME, "app-date-picker-create-plan")
            txt_date = date_picker.find_element(By.TAG_NAME, "input")
            self.enter_web_item_text(txt_date, working_date)
        if working_persons != "":
            div_worker = body_content.find_element(By.TAG_NAME, "app-input-number")
            txt_worker = div_worker.find_element(By.TAG_NAME, "input")
            self.enter_web_item_text(txt_worker, working_persons)
        if working_hours != -1:
            ddl_working_hours = body_content.find_elements(By.TAG_NAME, "app-select-option-value")[0]

            time.sleep(1)
            self.enter_dropdown_in_modal_dialog(ddl_working_hours, working_hours)

        if working_minutes != -1:
            ddl_working_minutes = body_content.find_elements(By.TAG_NAME, "app-select-option-value")[1]

            time.sleep(1)
            self.enter_dropdown_in_modal_dialog(ddl_working_minutes, working_minutes)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(footer_area, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(2)
        createProductPlan = CreateProductPlan(self.driver, self.department_name)
        return createProductPlan
    def create_new_plan_agp(self,working_date = ""):
        create_plan_button = self.find_element(By.XPATH, self.BUTTON_CREATE_PLAN)
        create_plan_button.click()
        time.sleep(3)
        body_content = self.find_element(By.TAG_NAME, "app-popup-working-persons-time-agp")
        if working_date != "":
            date_picker = body_content.find_element(By.TAG_NAME, "app-date-picker")
            txt_date = date_picker.find_element(By.TAG_NAME, "input")
            self.enter_web_item_text(txt_date, working_date)
        footer_area = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = self.find_elements_from_node(footer_area, By.TAG_NAME, "button")
        buttons[1].click()
        time.sleep(2)
        createProductPlan = CreateProductPlan(self.driver, self.department_name)
        return createProductPlan




















