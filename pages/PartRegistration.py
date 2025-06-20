from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains
class PartRegistration(BaseDriver):
    BUTTON_CREATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[1]/nz-col/nz-row/nz-space/div[2]/button"
    BUTTON_CANCEL = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[1]/nz-col/nz-row/nz-space/div[1]/button"
    DROPDOWN_CONTENT_LIST_TAG = "cdk-virtual-scroll-viewport"
    TABLE_SPECIFICATION = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody"
    TXT_DEFECT_SCORE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row[1]/nz-col[1]/nz-form-item/nz-col[2]/app-input-number/nz-input-number/div[2]/input"
    TXT_DEFECT_NOTE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row[2]/nz-col[1]/nz-form-item/nz-col[2]/nz-textarea-count/textarea"
    TXT_NOTE_1 = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row[2]/nz-col[2]/nz-form-item/nz-col[2]/nz-textarea-count/textarea"
    TXT_NOTE_2 = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row[3]/nz-col/nz-form-item/nz-col[2]/nz-textarea-count/textarea"
    TXT_SEARCH_CAR_BASIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[2]/nz-col[2]/nz-card[3]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[1]/td[2]/nz-input-group/span/input"
    BTN_SEARCH_CAR_BASIC = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[2]/nz-col[2]/nz-card[3]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[1]/td[2]/nz-input-group/span/span/button"
    TABLE_INVENTORY = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody"
    TABLE_TRANSACTION_INFO = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-part-registration/nz-row[2]/nz-col[2]/nz-card[5]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody"
    def do_create_part(self):
        button_create = self.find_element(By.XPATH,self.BUTTON_CREATE)
        button_create.click()
    def do_cancel_create_part(self):
        button_cancel = self.find_element(By.XPATH,self.BUTTON_CANCEL)
        button_cancel.click()
    def enter_dropdown_in_td(self,element,dropdown_index):
        element.click()
        time.sleep(2)

        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_LIST_TAG)
        items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        items[dropdown_index].click()
        time.sleep(2)
    def enter_checkbox_in_td(self,element,check_value):
        element.click()
    def enter_text_in_td(self,element,value):
        input_text = element.find_element(By.TAG_NAME,"input")
        input_text.send_keys(Keys.CLEAR)
        input_text.send_keys(value)
        input_text.send_keys(Keys.ENTER)
    def enter_text_in_element(self,element,txt_value):
        element.send_keys(Keys.CLEAR)
        element.send_keys(txt_value)
        element.send_keys(Keys.ENTER)

    def fill_info_specification(self,
                                part_type=-1,
                                part_category=-1,
                                part_code=-1,color="",
                                manufact_part_num= "",
                                genuine_part_num= "",
                                subsitute_num = "",
                                part_maker = ""):
        table_body = self.find_element(By.XPATH,self.TABLE_SPECIFICATION)

        trs = table_body.find_elements(By.TAG_NAME,"tr")
        tds = trs[0].find_elements(By.TAG_NAME,"td")
        if part_type != -1:
            self.enter_dropdown_in_td(tds[1],part_type)
        if part_category != -1:
            self.enter_dropdown_in_td(tds[3], part_category)
        tds = trs[1].find_elements(By.TAG_NAME,"td")
        if part_code != -1:
            self.enter_dropdown_in_td(tds[1], part_code)
        tds = trs[2].find_elements(By.TAG_NAME, "td")
        if color != "":
            self.enter_text_in_td(tds[1],color)
        if manufact_part_num != "":
            self.enter_text_in_td(tds[3], manufact_part_num)
        tds = trs[3].find_elements(By.TAG_NAME, "td")
        if genuine_part_num != "":
            self.enter_text_in_td(tds[1],genuine_part_num)
        if subsitute_num != "":
            self.enter_text_in_td(tds[3], subsitute_num)
        tds = trs[4].find_elements(By.TAG_NAME, "td")
        if part_maker != "":
            self.enter_text_in_td(tds[1], part_maker)
    def fill_info_condition(self,defect_score="",defect_note="",note_1="",note_2=""):
        if defect_score != "":
            txt_defect_score = self.find_element(By.XPATH,self.TXT_DEFECT_SCORE)
            self.enter_text_in_element(txt_defect_score,defect_score)
        if defect_note != "":
            txt_defect_note = self.find_element(By.XPATH,self.TXT_DEFECT_NOTE)
            self.enter_text_in_element(txt_defect_note,defect_note)
        if note_1 != "":
            txt_note_1 = self.find_element(By.XPATH, self.TXT_NOTE_1)
            self.enter_text_in_element(txt_note_1, note_1)
        if note_2 != "":
            txt_note_2 = self.find_element(By.XPATH, self.TXT_NOTE_2)
            self.enter_text_in_element(txt_note_2, note_2)
    def search_and_fill_basic_car_info(self,management_num=""):
        txt_search = self.find_element(By.XPATH,self.TXT_SEARCH_CAR_BASIC)
        self.enter_text_in_element(txt_search,management_num)
        btn_search = self.find_element(By.XPATH,self.BTN_SEARCH_CAR_BASIC )
        btn_search.click()
    def fill_inventory_and_processing(self,
                                      ware_house=-1,
                                      production_pic=-1,
                                      quantity="",
                                      status=-1,
                                      aquisition_route=-1):
        table_body = self.find_element(By.XPATH,self.TABLE_INVENTORY)
        trs = table_body.find_elements(By.TAG_NAME,"tr")
        tds = trs[0].find_elements(By.TAG_NAME,"td")
        if ware_house != -1:
            self.enter_dropdown_in_td(tds[1],ware_house)
        if production_pic != -1:
            self.enter_dropdown_in_td(tds[3],production_pic)
        tds = trs[1].find_elements(By.TAG_NAME, "td")
        if quantity != "":
            self.enter_text_in_td(tds[1],quantity)
        if status != -1:
            self.enter_dropdown_in_td(tds[3],status)
        tds = trs[2].find_elements(By.TAG_NAME, "td")
        if aquisition_route != -1:
            self.enter_dropdown_in_td(tds[1],aquisition_route)
    def fill_transaction_info(self,
                              is_published=-1,
                              price = "",
                              retail_price="",
                              brand_new_price="",
                              transport_parttern = -1,
                              transport_classification=-1,
                              transport_fee=""):

        table_body = self.find_element(By.XPATH, self.TABLE_TRANSACTION_INFO)
        trs = table_body.find_elements(By.TAG_NAME, "tr")
        tds = trs[0].find_elements(By.TAG_NAME, "td")
        if is_published != -1:
            self.enter_checkbox_in_td(tds[1],0)
        if price != "":
            self.enter_text_in_td(tds[3], price)
        tds = trs[1].find_elements(By.TAG_NAME, "td")
        if retail_price != "":
            self.enter_text_in_td(tds[1], retail_price)
        if brand_new_price != -1:
            self.enter_text_in_td(tds[3], brand_new_price)
        tds = trs[2].find_elements(By.TAG_NAME, "td")
        if transport_parttern != -1:
            self.enter_dropdown_in_td(tds[1], transport_parttern)
        if transport_classification != -1:
            self.enter_dropdown_in_td(tds[3], transport_classification)
        tds = trs[3].find_elements(By.TAG_NAME, "td")
        if transport_fee != "":
            self.enter_text_in_td(tds[1], transport_fee)















