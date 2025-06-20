from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains

from pages.ProductionParts import ProductionParts


class ProductCarManagementDetail(BaseDriver):
    CREATE_OUTCOME_PRODUCTION_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-production-car-list/app-production-car-list-domestic/nz-row/nz-col/nz-space/div/button"
    CREATE_OUTCOME_EXPORT_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-production-car-list/app-production-car-list-export/nz-row/nz-col/nz-space/div/button"
    CREATE_OUTCOME_MATERIAL_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-production-car-list/app-production-car-list-material/nz-row/nz-col/nz-space/div/button"
    EDIT_LINK = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-production-car-list/app-production-car-list-domestic/nz-card[1]/div[1]/div/div[2]/div"
    BUTTON_ADD_CAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-production-car-list/app-production-car-list-domestic/nz-card[2]/div[1]/div/div[2]/button"
    TXT_SEARCH_VALUE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-production-car-list/app-production-car-list-domestic/nz-card[2]/div[2]/app-production-car-list-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[2]/input"
    DROPDOWN_REQ_NUM = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-production-car-list/app-production-car-list-domestic/nz-card[2]/div[2]/app-production-car-list-filter/nz-row[1]/nz-col[1]/nz-input-group/span/span[1]/nz-select"
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
                if item.text == option_value:
                    item.click()
                    break
        time.sleep(2)

    def create_outcome_production(self):
        btn_create_outcome = self.find_element(By.XPATH,self.CREATE_OUTCOME_PRODUCTION_BUTTON)
        btn_create_outcome.click()

        confirm_dialog = self.driver.find_element(By.XPATH,"//*[contains(@class, 'ant-popover-buttons')]")
        confirm_btn = confirm_dialog.find_elements(By.TAG_NAME,"button")[1]
        confirm_btn.click()
    def create_outcome_export(self):
        btn_create_outcome = self.find_element(By.XPATH,self.CREATE_OUTCOME_EXPORT_BUTTON)
        btn_create_outcome.click()

        confirm_dialog = self.driver.find_element(By.XPATH,"//*[contains(@class, 'ant-popover-buttons')]")
        confirm_btn = confirm_dialog.find_elements(By.TAG_NAME,"button")[1]
        confirm_btn.click()
    def create_outcome_material(self):
        btn_create_outcome = self.find_element(By.XPATH,self.CREATE_OUTCOME_MATERIAL_BUTTON)
        btn_create_outcome.click()

        confirm_dialog = self.driver.find_element(By.XPATH,"//*[contains(@class, 'ant-popover-buttons')]")
        confirm_btn = confirm_dialog.find_elements(By.TAG_NAME,"button")[1]
        confirm_btn.click()
    def add_cars_to_production(self,chasis_number = ""):
        btn_add_car = self.find_element(By.XPATH,self.BUTTON_ADD_CAR)
        btn_add_car.click()
        modal_dialog = self.driver.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-content')]")
        body = modal_dialog.find_element(By.TAG_NAME,"tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME,"td")
            if len(tds) < 5:
                continue
            if tds[4].text == chasis_number and tds[4].text != "":
                input = tds[0].find_element(By.TAG_NAME,"input")
                input.click()
        footer = modal_dialog.find_element(By.XPATH,"//*[contains(@class, 'ant-modal-footer')]")
        buttons = footer.find_elements(By.TAG_NAME,"button")
        buttons[1].click()
    def search_car_in_production_list(self,request_number=-1,text_search="",priority=-1,production_flow=-1,production_status=-1):

        if request_number != -1:
            dropdown_request_num = self.find_element(By.XPATH,self.DROPDOWN_REQ_NUM)
            self.enter_web_item_drop_down(dropdown_request_num,request_number)
        if text_search != "":
            txt_search = self.find_element(By.XPATH,self.TXT_SEARCH_VALUE)
            self.enter_web_item_text(txt_search,text_search)







    def produce_car_parts(self,car_chasis_number,card_body_index=1):
        card_bodies = self.find_elements(By.CLASS_NAME, "ant-card-body")
        body = card_bodies[card_body_index].find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME, "tr")
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME, "td")
            chasis = tds[4].text
            if chasis  == car_chasis_number:
                tds[1].click()
                time.sleep(3)
                production_parts = ProductionParts(self.driver)
                production_parts.produce_parts()
                break




    def get_chasis_numbers_by_product_status(self, product_status="",status_column=11,card_boby_idx=1):
        lst_chasis_number = []
        card_bodies = self.find_elements(By.CLASS_NAME, "ant-card-body")
        body = card_bodies[card_boby_idx].find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME, "tr")
        for tr in trs:
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[status_column].text == product_status:
                lst_chasis_number.append(td[4].text)
        return lst_chasis_number
    def process_next_step(self,chasis_numbers,card_body_index=1):
        if len(chasis_numbers) == 0:
            return
        card_bodies = self.find_elements(By.CLASS_NAME, "ant-card-body")
        body = card_bodies[card_body_index].find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME, "tr")
        for tr in trs:
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[4].text in chasis_numbers :
                input = td[0].find_element(By.TAG_NAME,"input")
                input.click()
        title_footer = self.find_element(By.TAG_NAME, "nz-table-title-footer")
        button = title_footer.find_element(By.TAG_NAME, "button")
        button.click()



    def edit_product_detail(self,date="",working_person=2,working_hours=-1,working_minute=-1):
        edit_link = self.find_element(By.XPATH,self.EDIT_LINK)
        edit_link.click()
        time.sleep(2)
class ProductOutComeDetail(BaseDriver):
    BACK_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-header/app-header/div/nz-row/nz-col[2]/button"
    def go_back(self):
        back_button = self.find_element(By.XPATH,self.BACK_BUTTON)
        back_button.click()