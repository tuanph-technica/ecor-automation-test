from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains
class CarDetail(BaseDriver):
    BACK_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-header/app-header/div/nz-row/nz-col[2]/button"
    DELETE_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[1]/nz-col[2]/nz-row/nz-space/div/button"
    CONFIRM_DELETE_BUTTON = "/html/body/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]"
    BUTTON_CONDITION_PATH = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[1]/div[2]/button"
    DROPDOWN_CONTENT_TAG = "cdk-virtual-scroll-viewport"

    EVALUATION_POINT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[1]/td[2]/app-select-option-value"
    REPAIRE_HISTORY = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[1]/td[4]/label/span[1]/input"
    EXTERNAL_CONDITION = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[2]/td[2]/app-select-option-value"
    INTERNAL_CONDITION = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[2]/td[4]/app-select-option-value"
    IMMOVABLE_SUSPENSE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[3]/td[2]/label/span[1]/input"
    IMMOVABLE_ENGINE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[3]/td[4]/label/span[1]/input"
    IMMOVABLE_ACCIDENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[4]/td[2]/label/span[1]/input"
    IMMOVABLE_BATTERY = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[4]/td[4]/label/span[1]/input"
    IMMOVABLE_OTHERS = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr[5]/td[2]/label/span[1]/input"
    SAVE_CONDITION_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-detail/nz-row[2]/nz-col[2]/nz-card[4]/div/nz-collapse/nz-collapse-panel/div[1]/div[2]/nz-space/div[1]/button"

    # frame general infomation
    def get_checkbox_value_from_td_tag(self,td_element):
        check_box = self.find_elements_from_node(td_element,By.TAG_NAME,"input")[0]
        return check_box.is_selected()



    def __init__(self,driver):
        super().__init__(driver)
        app_car_detail = self.find_element(By.TAG_NAME, "app-car-detail")
        time.sleep(3)
        self.cards = self.find_elements_from_node(app_car_detail,By.TAG_NAME,"nz-card")

    def enter_back_button(self):
        back_button = self.find_element(By.XPATH,self.BACK_BUTTON)
        back_button.click()
    def delete_car(self):
        delete_button = self.find_element(By.XPATH,self.DELETE_BUTTON)
        delete_button.click()
        modal_dialog = self.find_element(By.XPATH,"//*[contains(@class, 'ant-popover-buttons')]")
        time.sleep(1)
        confirm_delete_button = modal_dialog.find_elements(By.TAG_NAME,"button")[1]
        confirm_delete_button.click()
    def enter_dropdown_in_td(self,element,option_text):
        element.click()
        time.sleep(1)

        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_TAG)
        items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        for item in items:
            if item.text == option_text:
                item.click()
                break

        time.sleep(1)
    def enter_checkbox_in_td(self,element,check_value):

        element.click()
        time.sleep(2)





    def get_general_infomation(self):
        body_content = self.cards[0].find_element(By.XPATH,"//*[contains(@class,'ant-descriptions-view')]")
        trs = self.find_elements_from_node(body_content,By.TAG_NAME,"tr")
        first_line = trs[0]
        second_line = trs[1]
        tds = self.find_elements_from_node(first_line,By.TAG_NAME,"td")
        ret = dict()
        ret['total_purchase_code'] = tds[1].text
        ret['total_estimated_value'] = tds[3].text
        tds = self.find_elements_from_node(second_line, By.TAG_NAME, "td")
        ret['sold_amount'] = tds[1].text
        ret['inventory'] = tds[3].text
        return ret

    def get_car_basic_infomation(self):
        ret = dict()
        body_content = self.cards[1].find_element(By.XPATH, "//*[contains(@class,'ant-descriptions-view')]")
        trs = self.find_elements_from_node(body_content, By.TAG_NAME, "tr")
        tds = self.find_elements_from_node(trs[0], By.TAG_NAME, "td")
        ret['management_number'] = tds[1].text
        ret['input_date'] = tds[3].text

        tds = self.find_elements_from_node(trs[1], By.TAG_NAME, "td")
        ret['car_maker'] = tds[1].text
        ret['car_name'] =  tds[3].text

        tds = self.find_elements_from_node(trs[2], By.TAG_NAME, "td")
        ret['model'] = tds[1].text
        ret['year'] = tds[3].text

        tds = self.find_elements_from_node(trs[3], By.TAG_NAME, "td")
        ret['body_type'] = tds[1].text
        ret['grade'] = tds[3].text

        tds = self.find_elements_from_node(trs[4], By.TAG_NAME, "td")
        ret['chasis_number'] = tds[1].text
        ret['mile_age'] = tds[3].text

        tds = self.find_elements_from_node(trs[5], By.TAG_NAME, "td")
        ret['displcement'] = tds[1].text
        ret['weight'] = tds[3].text

        tds = self.find_elements_from_node(trs[6], By.TAG_NAME, "td")
        ret['color'] = tds[1].text
        ret['sale_pic'] = tds[3].text

        tds = self.find_elements_from_node(trs[7], By.TAG_NAME, "td")
        ret['remain_inspection'] = tds[1].text
        ret['supplier_type'] = tds[3].text

        tds = self.find_elements_from_node(trs[8], By.TAG_NAME, "td")
        ret['supplier_name'] = tds[1].text
        ret['supplier_address'] = tds[3].text
    def get_car_additional_infor(self):
        ret = dict()
        body_content = self.cards[2].find_element(By.XPATH, "//*[contains(@class,'ant-descriptions-view')]")
        trs = self.find_elements_from_node(body_content, By.TAG_NAME, "tr")
        tds = self.find_elements_from_node(trs[0], By.TAG_NAME, "td")
        ret['karte_no'] = tds[1].text
        ret['freon_removed'] = self.get_checkbox_value_from_td_tag(tds[3])

        tds = self.find_elements_from_node(trs[1], By.TAG_NAME, "td")
        ret['airbag_removed'] = self.get_checkbox_value_from_td_tag(tds[1])
        ret['minor_change'] = tds[3].text

        tds = self.find_elements_from_node(trs[2], By.TAG_NAME, "td")
        ret['body_color'] = tds[1].text
        ret['color_no'] = tds[3].text

        tds = self.find_elements_from_node(trs[3], By.TAG_NAME, "td")
        ret['trim_no'] = tds[1].text
        ret['engine_model'] = tds[3].text

        tds = self.find_elements_from_node(trs[4], By.TAG_NAME, "td")
        ret['purpose'] = tds[1].text
        ret['sale_category'] = tds[3].text

        tds = self.find_elements_from_node(trs[5], By.TAG_NAME, "td")
        ret['production_category'] = tds[1].text
        ret['production_method'] = tds[3].text
    def get_car_condition(self):
        ret = dict()
        body_content = self.cards[3].find_element(By.XPATH, "//*[contains(@class,'ant-descriptions-view')]")
        trs = self.find_elements_from_node(body_content, By.TAG_NAME, "tr")
        tds = self.find_elements_from_node(trs[0], By.TAG_NAME, "td")
        ret['evaluation_point'] = tds[1].text
        ret['repaire_history'] = self.get_checkbox_value_from_td_tag(tds[3])

        tds = self.find_elements_from_node(trs[1], By.TAG_NAME, "td")
        ret['exterior_condition'] = tds[1]
        ret['interior_condition'] = tds[3].text

        tds = self.find_elements_from_node(trs[2], By.TAG_NAME, "td")
        ret['immovatible_suspension'] = self.get_checkbox_value_from_td_tag(tds[1])
        ret['immovative_engine'] = self.get_checkbox_value_from_td_tag(tds[3])

        tds = self.find_elements_from_node(trs[3], By.TAG_NAME, "td")
        ret['accident'] = self.get_checkbox_value_from_td_tag(tds[1])
        ret['battery'] = self.get_checkbox_value_from_td_tag(tds[3])


        tds = self.find_elements_from_node(trs[4], By.TAG_NAME, "td")
        ret['immovative_other'] = tds[1].text
    def get_confirmmation_document(self):
        ret = dict()
        collapse = self.find_elements_from_node(self.cards[4], By.TAG_NAME, "nz-collapse")[0]
        collapse.click()
        body_content = self.find_elements_from_node(collapse,By.TAG_NAME,"tbody")[0]
        trs = self.find_elements_from_node(body_content, By.TAG_NAME, "tr")
        tds = self.find_elements_from_node(trs[0], By.TAG_NAME, "td")
        ret['document_type'] = tds[1].text
        ret['original_unavaiable'] = self.get_checkbox_value_from_td_tag(tds[3])

        tds = self.find_elements_from_node(trs[1], By.TAG_NAME, "td")
        ret['confirmed'] = self.get_checkbox_value_from_td_tag(tds[1])
        ret['transfer_permision'] = self.get_checkbox_value_from_td_tag(tds[3])

        tds = self.find_elements_from_node(trs[2], By.TAG_NAME, "td")
        ret['expected_docu_delivery_date'] = tds[1].text
        ret['docu_delivery_date'] = tds[3].text

        tds = self.find_elements_from_node(trs[3], By.TAG_NAME, "td")
        ret['docu_delivery_user'] = tds[1].text
        ret['docu_storage_place'] = tds[3].text
    def edit_car_condition(self,evaluation_point="",
                           repare_history = "-1",
                           external_cond = "",
                           interior_cond="",
                           immovable_suspense=-1,
                           immovable_engine = -1,
                           immovable_accident=-1,
                           immovable_battery=-1,
                           immovable_other=-1
        ):

        button = self.find_element(By.XPATH,self.BUTTON_CONDITION_PATH)
        button.click()
        time.sleep(3)

        if evaluation_point != "":
            dropdown_evaluation = self.find_element(By.XPATH,self.EVALUATION_POINT)
            self.enter_dropdown_in_td(dropdown_evaluation,evaluation_point)
        if repare_history != -1:
            chk_repaire = self.find_element(By.XPATH,self.REPAIRE_HISTORY)
            self.enter_checkbox_in_td(chk_repaire,True)
        if external_cond != "":
            dropdown_ext = self.find_element(By.XPATH,self.EXTERNAL_CONDITION)
            self.enter_dropdown_in_td(dropdown_ext, external_cond)
        if interior_cond != "":
            dropdown_int = self.find_element(By.XPATH,self.INTERNAL_CONDITION)
            self.enter_dropdown_in_td(dropdown_int, interior_cond)
        if immovable_suspense >= 0:
            chk_immo_suspense = self.find_element(By.XPATH,self.IMMOVABLE_SUSPENSE)
            self.enter_checkbox_in_td(chk_immo_suspense,immovable_suspense)
        if immovable_engine >= 0:
            chk_immo_engine = self.find_element(By.XPATH,self.IMMOVABLE_ENGINE)
            self.enter_checkbox_in_td(chk_immo_engine,immovable_suspense)
        if immovable_accident >= 0:
            chk_immo_accident = self.find_element(By.XPATH,self.IMMOVABLE_ACCIDENT)
            self.enter_checkbox_in_td(chk_immo_accident,immovable_accident)
        if immovable_battery >= 0:
            chk_immo_battery = self.find_element(By.XPATH,self.IMMOVABLE_BATTERY)
            self.enter_checkbox_in_td(chk_immo_battery,immovable_battery)
        if immovable_other >= 0:
            chk_immo_other = self.find_element(By.XPATH,self.IMMOVABLE_OTHERS)
            self.enter_checkbox_in_td(chk_immo_other,immovable_other)
        time.sleep(2)
        save_button = self.find_element(By.XPATH,self.SAVE_CONDITION_BUTTON)
        save_button.click()

























