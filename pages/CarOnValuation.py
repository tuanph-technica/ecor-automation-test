import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains
BUYERS = ["AGP","DB","JOR","PG1","KABIR","CEBU","DOM"]
class CarOnValuation(BaseDriver):
    EDIT_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[1]/nz-col[2]/nz-space/div[1]/button"
    CLOSE_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[1]/nz-col[2]/nz-space/div[2]/button"
    RETURN_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-header/app-header/div/nz-row/nz-col[2]/button"
    PART_VALUATION_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/nz-tabs-nav/div/div/div[1]/div"
    USER_CAR_VALUATION_CONTENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/nz-tabs-nav/div/div/div[2]/div"
    REJECT_BUTTON_PART =    "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[1]/app-valuation-part/nz-row[2]/nz-col/nz-space/div[1]/button"
    CONFIRM_BUTTON_PART = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[1]/app-valuation-part/nz-row[2]/nz-col/nz-space/div[2]/button"
    REJECT_BUTTON_USEDCAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[2]/app-valuation-used-car/nz-row[6]/nz-col/nz-space/div[1]/button"
    CONFIRM_BUTTON_USEDCAR = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[2]/app-valuation-used-car/nz-row[6]/nz-col/nz-space/div[2]/button"
    ADD_PART_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[1]/app-valuation-part/div/nz-row/nz-col[2]/div/button"
    DIALOG_ADDPART_CONFIRM_BUTTON = "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]"
    MODAL_FOOTER_DIALOG_CLASSNAME = "ant-modal-footer"
    TXT_VALUATION_PRICE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[2]/app-valuation-used-car/nz-row[1]/nz-col[2]/app-input-currency/nz-input-number/div[2]/input"
    TXT_CAR_CODE_RATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[2]/app-valuation-used-car/nz-row[2]/nz-col[2]/app-input-percent/nz-input-number/div[2]/input"
    DDL_BUYER = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[2]/app-valuation-used-car/nz-row[4]/nz-col[2]/app-select-buyer"
    TEXT_AREA_NOTE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[2]/app-valuation-used-car/nz-row[5]/nz-col[2]/nz-textarea-count/textarea"
    BTN_REJECT_VALUATION = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[2]/app-valuation-used-car/nz-row[6]/nz-col/nz-space/div[1]/button"
    BTN_CONFIRM_BUTTON =  "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[2]/app-valuation-used-car/nz-row[6]/nz-col/nz-space/div[2]/button"
    DROPDOWN_CONTENT_TAG_NAME = "cdk-virtual-scroll-viewport"
    TXT_PART_CODE_SEARCH = "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/app-add-parts/app-popup-add-parts-export/nz-row[3]/nz-col[2]/app-input-search/nz-input-group/input"
    LST_PART_CATEGORY_TAGNAME = "nz-list"
    LST_PART = "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[2]/app-add-parts/app-popup-add-parts-export/nz-row[4]/nz-col[2]/div"
    BTN_CONFIRM_PART = "/html/body/div[2]/div[2]/div/nz-modal-container/div/div/div[3]/button[2]"
    # DS Role
    TXT_VALUAION_PRICE_DS = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-valuation-used-car/nz-row[1]/nz-col[2]/app-input-currency/nz-input-number/div[2]/input"
    TXT_CAR_COST_RATE_DS = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-valuation-used-car/nz-row[2]/nz-col[2]/app-input-percent/nz-input-number/div[2]/input"
    TXT_NOTE_DS = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-valuation-used-car/nz-row[4]/nz-col[2]/nz-textarea-count/textarea"
    BTN_CONFIRM_DS = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-valuation-used-car/nz-row[5]/nz-col/nz-space/div[2]/button"
    BTN_REJECT_DS = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-valuation-used-car/nz-row[5]/nz-col/nz-space/div[1]/button"
    # PRODUCTION Role
    TXT_NOTE_PRODUCTION = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-valuation-part/nz-row[1]/nz-col[2]/nz-textarea-count/textarea"
    BTN_CONFIRM_PRODUCTION = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div/app-valuation-part/nz-row[2]/nz-col/nz-space/div[2]/button"
    # Export role
    TXT_NOTE_EXPORT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[1]/app-valuation-part/nz-row[1]/nz-col[2]/nz-textarea-count/textarea"
    BTN_CONFIRM_EXPORT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-car/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-tabset/div/div/div[1]/app-valuation-part/nz-row[2]/nz-col/nz-space/div[2]/button"


    def enter_text_value(self,element,value):

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(value)
        element.send_keys(Keys.ENTER)
    def enter_dropdown_value(self,element,option_text):
        element.click()
        time.sleep(1)
        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_TAG_NAME)
        items = self.find_elements_from_node(dropdown_content,By.TAG_NAME,"nz-option-item")
        if isinstance(option_text,int):
            items[option_text].click()
        else:
            input = element.find_element(By.TAG_NAME,"input")
            input.send_keys(option_text)
            input.send_keys(Keys.ENTER)
        time.sleep(1)

    def come_back(self):
        return_button = self.find_element(By.XPATH,self.RETURN_BUTTON)
        return_button.click()
    def add_parts_normal(self,select_num_cat, select_num_part):
        part_content = self.find_element(By.XPATH, self.PART_VALUATION_CONTENT)
        part_content.click()
        time.sleep(1)
        button_add_part = self.find_element(By.XPATH, self.ADD_PART_BUTTON)
        button_add_part.click()
        time.sleep(2)
        lst_part_category = self.find_element(By.TAG_NAME, self.LST_PART_CATEGORY_TAGNAME)
        categories = self.find_elements_from_node(lst_part_category, By.TAG_NAME, "nz-list-item")
        num_category = len(categories)
        if select_num_cat > num_category:
            select_num_cat = num_category
        for i in range(select_num_cat):
            category_index = random.randint(0, num_category - 1)
            categories[category_index].click()
            app_popup = self.find_element(By.TAG_NAME, "app-popup-add-parts-normal")
            lst_content  = app_popup.find_elements(By.XPATH, "./*")[2]
            nzcols = lst_content.find_elements(By.TAG_NAME, "nz-col")
            parts = nzcols[1].find_elements(By.TAG_NAME, "input")
            num_parts = len(parts)
            if select_num_part > num_parts:
                select_num_part = num_parts
            for k in range(select_num_part):
                part_index = random.randint(0, num_parts - 1)
                parts[part_index].click()
        time.sleep(3)
        element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = element.find_elements(By.XPATH, "./*")
        buttons[1].click()
        time.sleep(2)
        content = self.find_element(By.TAG_NAME,"app-valuation-part")
        body = content.find_element(By.TAG_NAME,"tbody")
        trs = body.find_elements(By.TAG_NAME,"tr")
        for i in range(1,len(trs)-1):
            tds = trs[i].find_elements(By.TAG_NAME,"td")
            input = tds[0].find_element(By.TAG_NAME,"input")
            input.click()
            txt_val_price = tds[3].find_element(By.TAG_NAME,"input")
            txt_val_price.send_keys("15000")
            txt_val_price.send_keys(Keys.ENTER)


    def do_valuate_export_part_by_select_list(self,select_num_cat, select_num_part,note=""):
        # select num_category : number category_selecton
        # select num part : number of part for category
        part_content = self.find_element(By.XPATH,self.PART_VALUATION_CONTENT)
        part_content.click()
        time.sleep(1)
        button_add_part = self.find_element(By.XPATH,self.ADD_PART_BUTTON)
        button_add_part.click()
        time.sleep(2)
        lst_part_category = self.find_element(By.TAG_NAME,self.LST_PART_CATEGORY_TAGNAME)
        categories = self.find_elements_from_node(lst_part_category,By.TAG_NAME,"nz-list-item")
        num_category = len(categories)
        if select_num_cat > num_category:
            select_num_cat = num_category
        for i in range(select_num_cat):
            category_index = random.randint(0,num_category-1)
            categories[category_index].click()
            app_popup = self.find_element(By.TAG_NAME,"app-popup-add-parts-export")
            nzrows = app_popup.find_elements(By.TAG_NAME,"nz-row")
            nzcols = nzrows[3].find_elements(By.TAG_NAME,"nz-col")
            parts = nzcols[1].find_elements(By.TAG_NAME,"input")
            num_parts = len(parts)
            if select_num_part > num_parts:
                select_num_part = num_parts
            for k in range(select_num_part):
                part_index = random.randint(0,num_parts-1)
                parts[part_index].click()
        time.sleep(3)
        element = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = element.find_elements(By.XPATH,"./*")
        buttons[1].click()
        time.sleep(2)
        content = self.find_element(By.TAG_NAME, "app-valuation-part")
        body = content.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME, "tr")
        for i in range(1, len(trs) - 1):
            tds = trs[i].find_elements(By.TAG_NAME, "td")
            input = tds[0].find_element(By.TAG_NAME, "input")
            input.click()
            txt_val_price = tds[3].find_element(By.TAG_NAME, "input")
            txt_val_price.send_keys("15000")
            txt_val_price.send_keys(Keys.ENTER)
            ddl_buyer = tds[5].find_element(By.TAG_NAME,"app-select-buyer")
            random_index = random.randint(0,len(BUYERS)-1)
            self.enter_dropdown_value(ddl_buyer,BUYERS[random_index])


        if note != "":
            txt_note = self.find_element(By.XPATH, self.TXT_NOTE_EXPORT)
            self.enter_text_value(txt_note, note)
        btn_confirm = self.find_element(By.XPATH, self.BTN_CONFIRM_EXPORT)
        btn_confirm.click()



    def do_confirm_valuated_ds_role(self,valuation_price="",car_cost_rate="",note=""):
        if valuation_price != "":
            txt_price = self.find_element(By.XPATH,self.TXT_VALUAION_PRICE_DS)
            self.enter_text_value(txt_price,valuation_price)
        if car_cost_rate != "":
            txt_car_cost_rate = self.find_element(By.XPATH,self.TXT_CAR_COST_RATE_DS)
            self.enter_text_value(txt_car_cost_rate,car_cost_rate)
        if note != "":
            txt_note = self.find_element(By.XPATH,self.TXT_NOTE_DS)
            self.enter_text_value(txt_note,note)
        btn_confirm = self.find_element(By.XPATH, self.BTN_CONFIRM_DS)
        btn_confirm.click()
    def do_confirm_valuated_production_role(self,note):
        self.add_parts_normal(2,2)
        if note != "":
            txt_note = self.find_element(By.XPATH,self.TXT_NOTE_PRODUCTION)
            self.enter_text_value(txt_note,note)
        btn_confirm = self.find_element(By.XPATH, self.BTN_CONFIRM_PRODUCTION)
        btn_confirm.click()



    def do_confirm_export_valuate_used_car(self, valuation_price="",car_cost_rate="",buyer="",note=""):
        used_car_content = self.find_element(By.XPATH,self.USER_CAR_VALUATION_CONTENT)
        used_car_content.click()
        time.sleep(3)
        if valuation_price != "":
            txt_valuation_price = self.find_element(By.XPATH,self.TXT_VALUATION_PRICE)
            self.enter_text_value(txt_valuation_price,valuation_price)
        if car_cost_rate != "":
            txt_car_cost_rate = self.find_element(By.XPATH,self.TXT_CAR_CODE_RATE)
            self.enter_text_value(txt_car_cost_rate,car_cost_rate)
        if buyer != "":
            ddl_buyer = self.find_element(By.XPATH,self.DDL_BUYER)
            self.enter_dropdown_value(ddl_buyer,buyer)
        if note != "":
            txt_note = self.find_element(By.XPATH,self.TEXT_AREA_NOTE)
            self.enter_text_value(txt_note,note)
        btn_confirm = self.find_element(By.XPATH,self.BTN_CONFIRM_BUTTON)
        btn_confirm.click()
    def do_reject_valuate_export_used_car(self, valuation_price="",car_cost_rate="",buyer="",note=""):
        if valuation_price != "":
            txt_valuation_price = self.find_element(By.XPATH,self.TXT_VALUATION_PRICE)
            self.enter_text_value(txt_valuation_price,valuation_price)
        if car_cost_rate != "":
            txt_car_cost_rate = self.find_element(By.XPATH,self.TXT_CAR_CODE_RATE)
            self.enter_text_value(txt_car_cost_rate,car_cost_rate)
        if buyer != "":
            ddl_buyer = self.find_element(By.XPATH,self.DDL_BUYER)
            self.enter_dropdown_value(ddl_buyer,buyer)
        if note != "":
            txt_note = self.find_element(By.XPATH,self.TEXT_AREA_NOTE)
            self.enter_text_value(txt_note,note)
        btn_reject = self.find_element(By.XPATH,self.BTN_REJECT_VALUATION)
        btn_reject.click()















