import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains
LIST_PART_AVAIABLES = ["1040","1060","1350","1310","1510","2010","2012","2013","2014","2017",
                       "3010","3020","3021","3030","3040"]
class UsedCarAssetment(BaseDriver):

    CONFIRM_DS_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-assessment-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-assess-used-car/nz-row[6]/nz-col/nz-space/div[2]/button"
    CONFIRM_PRODUCTION_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-assessment-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-assess-part/nz-row[3]/nz-col/nz-space/div[2]/button"
    REJECT_BUTTON =  "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-assessment-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-assess-used-car/nz-row[6]/nz-col/nz-space/div[1]/button"
    REJECT_DROPDOWN = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-assessment-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-assess-used-car/nz-row[4]/nz-col[2]/app-select-option-value"
    NOTE_AREA = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-assessment-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-assess-used-car/nz-row[5]/nz-col[2]/nz-textarea-count/textarea"
    NOTE_AREA_PRODUCTION = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-assessment-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-assess-part/nz-row[2]/nz-col[2]/nz-textarea-count/textarea"
    TXT_CAR_PRICE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-assessment-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-assess-used-car/nz-row[1]/nz-col[2]/app-input-currency/nz-input-number/div[2]/input"
    TXT_CAR_COST_RATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-assessment-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-assess-used-car/nz-row[2]/nz-col[2]/app-input-percent/nz-input-number/div[2]/input"
    DROPDOWN_CONTENT_TAG = "cdk-virtual-scroll-viewport"
    BTN_ADD_PARTS_PRODUCTION_ROLE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-assessment-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-assess-part/div/nz-row/nz-col[2]/div/button"
    def enter_dropdown_element(self,element,option_value=-1):
        element.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_TAG)
        items = dropdown_content.find_elements(By.TAG_NAME,"nz-option-item")
        if option_value == -1:
            random_index = random.randint(0,len(items)-1)
            items[random_index].click()
        else:
            for item in items:
                if item.text.find(str(option_value)) >= 0:
                    item.click()
                    break
    def enter_text_element(self,element,txt_value):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(txt_value)
        element.send_keys(Keys.ENTER)
    def do_reject_assetment(self,note=""):
        dropdown_reason = self.find_element(By.XPATH,self.REJECT_DROPDOWN)
        self.enter_dropdown_element(dropdown_reason)
        if note != "":
            txt_node = self.find_element(By.XPATH,self.NOTE_AREA)
            self.enter_text_element(txt_node,txt_value=note)
        button = self.find_element(By.XPATH,self.REJECT_BUTTON)
        button.click()
        ok_cancel_dialog = self.find_element(By.ID,"cdk-overlay-10")
        buttons = ok_cancel_dialog.find_elements(By.TAG_NAME,"button")
        buttons[1].click()

    def do_confirm_assetment_ds(self,car_price="",cost_rate="",note=""):
        if car_price != "":
            txt_car_price = self.find_element(By.XPATH,self.TXT_CAR_PRICE)
            self.enter_text_element(txt_car_price,car_price)
        if cost_rate != "":
            txt_cost_rate = self.find_element(By.XPATH,self.TXT_CAR_COST_RATE)
            self.enter_text_element(txt_cost_rate,cost_rate)
        if note != "":
            txt_note = self.find_element(By.XPATH,self.NOTE_AREA)
            self.enter_text_element(txt_note,note)
        button = self.find_element(By.XPATH, self.CONFIRM_DS_BUTTON)
        button.click()
    def get_number_of_parts(self):
        bodies = self.find_elements(By.TAG_NAME,"tbody")
        trs = bodies[0].find_elements(By.TAG_NAME,"tr")
        return len(trs)
    def do_add_parts_production_role(self,number_of_parts):
        btn_add_part = self.find_element(By.XPATH,self.BTN_ADD_PARTS_PRODUCTION_ROLE)
        btn_add_part.click()
        time.sleep(1)
        part_available_num = len(LIST_PART_AVAIABLES)
        part_indexes = random.sample(range(0,part_available_num),number_of_parts)
        for part_index in part_indexes:
            part_code = part_indexes[part_index]
            app_input_search = self.find_element(By.TAG_NAME,"app-input-search")
            input = app_input_search.find_element(By.TAG_NAME,input)
            input.send_keys(Keys.CONTROL + "a")
            input.send_keys(Keys.DELETE)
            input.send_keys(part_code)
            input.send_keys(Keys.ENTER)
            checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
            checkboxes[0].click()
    def do_confirm_assetment_production(self,note=""):
        if note != "":
            txt_note = self.find_element(By.XPATH,self.NOTE_AREA_PRODUCTION)
            self.enter_text_element(txt_note,note)
        button = self.find_element(By.XPATH, self.CONFIRM_PRODUCTION_BUTTON)
        button.click()
    def do_confirm_assetment_export(self,car_price="",cost_rate="",note=""):
        if car_price != "":
            txt_car_price = self.find_element(By.XPATH,self.TXT_CAR_PRICE)
            self.enter_text_element(txt_car_price,car_price)
        if cost_rate != "":
            txt_cost_rate = self.find_element(By.XPATH,self.TXT_CAR_COST_RATE)
            self.enter_text_element(txt_cost_rate,cost_rate)
        if note != "":
            txt_note = self.find_element(By.XPATH,self.NOTE_AREA)
            self.enter_text_element(txt_note,note)
        button = self.find_element(By.XPATH, self.CONFIRM_DS_BUTTON)
        button.click()



