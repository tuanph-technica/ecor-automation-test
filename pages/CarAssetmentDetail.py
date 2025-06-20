import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains

from pages.UsedCarAssetment import UsedCarAssetment


class CarAssetmentDetail(BaseDriver):
    CAR_ASSTMENT_VALUE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-detail/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/tbody/tr[2]/td[2]/div"
    CAR_PART_ASSETMENT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-detail/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/tbody/tr[3]/td[2]/div"
    CAR_MATERIAL_ASSETMENT_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-detail/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/tbody/tr[4]/td[2]/div"
    CAR_PURCHASE_FIELD = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-detail/nz-row[2]/nz-col[2]/nz-card[2]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-descriptions/div/table/tbody/tr/td[2]/input"
    BUTTON_BACK = "/html/body/app-root/app-home/nz-layout/nz-header/app-header/div/nz-row/nz-col[2]/button"
    BUTTON_UNPURCHASE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-detail/nz-row[1]/nz-col[2]/nz-space/div[1]/button"
    DROPDOWN_CONTENT_TAG = "cdk-virtual-scroll-viewport"
    BUTTON_REQUEST_ASSETMENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-detail/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/thead/tr/th[4]/button[2]"
    BUTTON_COST_CALCULATE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-detail/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/thead/tr/th[4]/button[1]"
    BUTTON_PURCHASE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-detail/nz-row[1]/nz-col[2]/nz-space/div[2]/button"
    BUTTON_ACCESSTMENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-car-assessment-detail/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/thead/tr/th[4]/button"
    def enter_dropdown_popup_element(self,element,option_text):
        element.click()
        time.sleep(2)
        dropdown_content = self.find_element(By.TAG_NAME,self.DROPDOWN_CONTENT_TAG)
        items = dropdown_content.find_elements(By.TAG_NAME,"nz-option-item")
        if isinstance(option_text,int):
            items[option_text].click()
        else:
            for item in items:
                if item.text == option_text:
                    item.click()
                    break



    def enter_text_popup_element(self,element,txt_value):
        txt_element = element.find_element(By.TAG_NAME,"input")
        txt_element.send_keys(Keys.CONTROL + "a")
        txt_element.send_keys(Keys.DELETE)
        txt_element.send_keys(txt_value)
        txt_element.send_keys(Keys.ENTER)
    def enter_value_to_text(self,element,text_value):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text_value)
        element.send_keys(Keys.ENTER)

    def set_ticked_check_box(self,contain_element):
        check_box = contain_element.find_element(By.TAG_NAME, "input")
        if not check_box.is_selected():
            check_box.click()
    def set_unticked_check_box(self,contain_element):
        check_box = contain_element.find_element(By.TAG_NAME, "input")
        if check_box.is_selected():
            check_box.click()



    def __init__(self,driver):
        super().__init__(driver=driver)
    def get_car_assetment_value(self):
        element = self.wait_until_element_is_clickable(By.XPATH,self.CAR_ASSTMENT_VALUE_FIELD)
        return element.text
    def car_assetment_click(self):
        self.wait_until_element_is_clickable(By.XPATH, self.CAR_ASSTMENT_VALUE_FIELD).click()
    def get_car_part_assetment(self):
        element = self.wait_until_element_is_clickable(By.XPATH, self.CAR_PART_ASSETMENT_FIELD)
        return element.text
    def get_material_assetment_value(self):
        element = self.wait_until_element_is_clickable(By.XPATH, self.CAR_MATERIAL_ASSETMENT_FIELD)
        return element.text
    def get_purchase_price(self):
        element = self.wait_until_element_is_clickable(By.XPATH, self.CAR_PURCHASE_FIELD)
        return element.get_attribute('value')
    def get_ai_car_price_available(self):
        car_price = self.get_car_assetment_value().replace(",","")
        try:
            car_price = float(car_price)
            if car_price > 0:
                return 1
            else:
                return 0
        except:
            return 0
    def get_ai_part_price_avaiable(self):
        part_price = self.get_car_part_assetment().replace(",","")
        try:
            part_price = float(part_price)
            if part_price > 0:
                return 1
            else:
                return 0
        except:
            return 0
    def get_ai_material_price_avaiable(self):
        material_price = self.get_material_assetment_value().replace(",","")
        try:
            material_price = float(material_price)
            if material_price > 0 :
                return 1
            else:
                return 0
        except:
            return 0




    def get_access_purchase_price(self):
        car_price = float(self.get_car_assetment_value().replace(",",""))
        try:
            part_price = float(self.get_car_part_assetment().replace(",",""))
        except:
            part_price = 0
        material_price = self.get_material_assetment_value()
        if material_price != '-':
            material_price = float(material_price.replace(",",""))
        else:
            material_price = 0
        purchase_price = float(self.get_purchase_price().replace(",",""))
        if purchase_price == max(car_price,part_price,material_price):
            return True
        else:
            return False
    def asset_car_price_detail(self):
        element = self.wait_until_element_is_clickable(By.XPATH, self.CAR_ASSTMENT_VALUE_FIELD)
        element.click()
        time.sleep(3)
        parent_element = self.driver.find_element(By.TAG_NAME,'app-view-detail-assess-used-car')
        div_elements = parent_element.find_elements(By.CLASS_NAME,"div-bordered")

        all_txt = div_elements[0].text.split("\n")
        car_auto_assement_val = float(all_txt[1].replace(",", ""))
        all_txt = div_elements[1].text.split("\n")
        car_other_value = float(all_txt[1].replace(",", ""))
        car_price = float(self.get_car_assetment_value().replace(",",""))
        actions = ActionChains(self.driver)

        actions.move_by_offset(0,0)
        actions.click()
        actions.perform()
        time.sleep(5)

        if car_price == car_other_value + car_auto_assement_val:
            return True
        else:
            return False
    def asset_part_price_detail(self):
        element = self.wait_until_element_is_clickable(By.XPATH, self.CAR_PART_ASSETMENT_FIELD)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        parent_element = self.driver.find_elements(By.TAG_NAME, 'app-view-detail-assess-part')
        if len(parent_element) > 0:
            div_elements = parent_element[0].find_elements(By.CLASS_NAME,"div-bordered")
            all_txt = div_elements[0].text.split("\n")
            part_assement_val = float(all_txt[1].replace(",",""))
            all_txt = div_elements[1].text.split("\n")
            part_material_val = float(all_txt[1].replace(",",""))
            all_txt = div_elements[2].text.split("\n")
            part_other_value = float(all_txt[1].replace(",",""))
            part_price = float(self.get_car_part_assetment().replace(",",""))
            actions = ActionChains(self.driver)
            actions.move_by_offset(0, 0)
            actions.click()
            actions.perform()
            time.sleep(5)
            if part_price == part_assement_val + part_material_val + part_other_value:
                return True
            else:
                return False
        else:
            return True
    def asset_material_price_detail(self):
        element = self.wait_until_element_is_clickable(By.XPATH, self.CAR_MATERIAL_ASSETMENT_FIELD)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        parent_element = self.driver.find_elements(By.TAG_NAME, 'app-view-detail-assess-material')
        div_elements = parent_element[0].find_elements(By.CLASS_NAME, "div-bordered")
        all_txt = div_elements[0].text.split("\n")
        material_assement_val = float(all_txt[1].replace(",", ""))
        all_txt = div_elements[1].text.split("\n")
        material_others_val = float(all_txt[1].replace(",", ""))
        if self.get_material_assetment_value() != "-":
            material_price = float(self.get_material_assetment_value().replace(",",""))
        else:
            material_price = 0

        actions = ActionChains(self.driver)
        actions.move_by_offset(0, 0)
        actions.click()
        actions.perform()
        time.sleep(5)
        if material_price == material_assement_val + material_others_val:
            return True
        else:
            return False
    def click_back_to_assetment_list(self):
        button = self.wait_until_element_is_clickable(By.XPATH,self.BUTTON_BACK)
        self.driver.execute_script("arguments[0].click();", button)
    def do_unpurchase(self,price_lost,sale_pic="",reason=""):
        button = self.find_element(By.XPATH,self.BUTTON_UNPURCHASE)
        button.click()
        pop_up_content = self.driver.find_element(By.TAG_NAME,"app-popup-refuse-car-assessment")
        childs = pop_up_content.find_elements(By.XPATH,"./nz-row")
        if sale_pic != "":
            ddl_sale_pic = childs[1].find_element(By.TAG_NAME,"app-select-sale-pic")
            self.enter_dropdown_popup_element(ddl_sale_pic,sale_pic)
        if reason != "":
            ddl_reason = childs[2].find_element(By.TAG_NAME,"app-select-option-value")
            self.enter_dropdown_popup_element(ddl_reason,reason)
        if reason == 0 or reason == 1:
            self.enter_text_popup_element(childs[3],str(price_lost))
        time.sleep(2)
        footer_dialog = self.find_element(By.XPATH,"//*[contains(@class, 'ant-modal-footer')]")
        buttons = footer_dialog.find_elements(By.TAG_NAME,"button")
        buttons[1].click()
    def do_purchase(self,
                    txt_register_val="",
                    sale_pic = "",
                    purpose = "",
                    production_flow="",
                    supplier_type=0,
                    supplier_name="",
                    supplier_address="",
                    picup_addr = "",
                    picup_place="",
                    picup_deadline="",
                    document_type = "",
                    confirmed= False,
                    original_unavailable=False,
                    transfer_permission= False,
                    include_vat = False,
                    car_price = "",
                    weight_tax ="",
                    recycle_fee = "",
                    compulsory_insurance = "",
                    automobile_tax="",
                    domestic = "",
                    ds = "",
                    material = "",
                    export = "",
                    alumi_wheel = False,
                    duplicate_reason = "",
                    dismantling_cer_required = False,
                    urgent_dismantling = False,
                    urgent_dis_items = "",
                    others = "",
                    removal_images = False,
                    dismarting_images = False

                    ):
        button = self.find_element(By.XPATH,self.BUTTON_PURCHASE)
        button.click()
        time.sleep(1)
        body_content = self.find_element(By.TAG_NAME,"app-popup-purchase-car-assessment")
        rows = body_content.find_elements(By.XPATH,"./nz-row")
        if txt_register_val != "":
            ant_rows = rows[0].find_elements(By.CLASS_NAME,"ant-row")
            inputs = ant_rows[-1].find_elements(By.TAG_NAME,"input")
            self.enter_value_to_text(inputs[1],txt_register_val)
            time.sleep(2)
        if sale_pic != "" :
            ddl_sale_pic = rows[1].find_element(By.TAG_NAME,"app-select-sale-pic")
            self.enter_dropdown_popup_element(ddl_sale_pic,sale_pic)
        if purpose != "":
            ddl_purpose = rows[1].find_elements(By.TAG_NAME,"app-select-option-value")[0]
            self.enter_dropdown_popup_element(ddl_purpose,purpose)
        if production_flow != "":
            ddl_production_flow = rows[1].find_elements(By.TAG_NAME, "app-select-option-value")[1]
            self.enter_dropdown_popup_element(ddl_production_flow,production_flow)
        body_contents = rows[2].find_element(By.TAG_NAME,"tbody")
        if supplier_type == 1:
            radio_group = rows[2].find_element(By.TAG_NAME,"nz-radio-group")
            radios = radio_group.find_elements(By.TAG_NAME,"input")
            if not radios[0].is_selected():
                radios[0].click()
            trs = body_contents.find_elements(By.TAG_NAME,"tr")
            tds = trs[0].find_elements(By.TAG_NAME,"td")
            self.enter_text_popup_element(tds[3],supplier_name)
            tds = trs[1].find_elements(By.TAG_NAME,"td")
            self.enter_text_popup_element(tds[1],supplier_address)
            self.enter_text_popup_element(tds[3],picup_addr)
            tds = trs[2].find_elements(By.TAG_NAME, "td")
            self.enter_text_popup_element(tds[1],picup_place)
            self.enter_text_popup_element(tds[3],picup_deadline)
        elif supplier_type == 2 :
            radio_group = rows[2].find_element(By.TAG_NAME, "nz-radio-group")
            radios = radio_group.find_elements(By.TAG_NAME, "input")
            if not radios[1].is_selected():
                radios[1].click()
            trs = body_contents.find_elements(By.TAG_NAME, "tr")
            tds = trs[0].find_elements(By.TAG_NAME, "td")
            self.enter_dropdown_popup_element(tds[3],supplier_name)
            tds = trs[1].find_elements(By.TAG_NAME, "td")
            self.enter_text_popup_element(tds[1],picup_addr)
            tds = trs[2].find_elements(By.TAG_NAME, "td")
            self.enter_text_popup_element(tds[1],picup_deadline)
        # confirmation document
        body_contents = rows[3].find_element(By.TAG_NAME, "tbody")
        trs = body_contents.find_elements(By.TAG_NAME,"tr")
        if document_type:
            tds = trs[0].find_elements(By.TAG_NAME,"td")
            self.enter_dropdown_popup_element(tds[1],document_type)
        if original_unavailable:
            tds = trs[0].find_elements(By.TAG_NAME, "td")
            self.set_ticked_check_box(tds[3])
        if confirmed:
            tds = trs[1].find_elements(By.TAG_NAME, "td")
            self.set_ticked_check_box(tds[1])
        if transfer_permission:
            tds = trs[1].find_elements(By.TAG_NAME, "td")
            self.set_ticked_check_box(tds[3])
        #purchase infomation
        body_content = rows[4].find_element(By.TAG_NAME, "tbody")
        trs = body_content.find_elements(By.TAG_NAME,"tr")
        if include_vat:
            tds = trs[0].find_elements(By.TAG_NAME,"td")
            self.set_ticked_check_box(tds[1])
            self.enter_text_popup_element(tds[3],car_price)
        else:
            tds = trs[0].find_elements(By.TAG_NAME, "td")
            self.set_unticked_check_box(tds[1])
            tds = trs[1].find_elements(By.TAG_NAME, "td")
            self.enter_text_popup_element(tds[3], car_price)
        tds = trs[2].find_elements(By.TAG_NAME, "td")
        if automobile_tax != "":
            self.enter_text_popup_element(tds[1], automobile_tax)
        if weight_tax != "":
            self.enter_text_popup_element(tds[3],weight_tax)
        if recycle_fee != "":
            tds = trs[3].find_elements(By.TAG_NAME, "td")
            self.enter_text_popup_element(tds[3], recycle_fee)
        if compulsory_insurance != "":
            tds = trs[4].find_elements(By.TAG_NAME, "td")
            self.enter_text_popup_element(tds[3], compulsory_insurance)
        # department cost
        body_content = rows[5].find_element(By.TAG_NAME, "tbody")
        trs = body_content.find_elements(By.TAG_NAME,"tr")
        tds = trs[0].find_elements(By.TAG_NAME, "td")
        if domestic != "":
            self.enter_text_popup_element(tds[1],domestic)
        if ds != "":
            self.enter_text_popup_element(tds[3], ds)
        tds = trs[1].find_elements(By.TAG_NAME, "td")
        if material != "":
            self.enter_text_popup_element(tds[1], material)
        if export != "":
            self.enter_text_popup_element(tds[3], export)
        # notice
        body_content = rows[7].find_element(By.TAG_NAME, "tbody")
        trs = body_content.find_elements(By.TAG_NAME,"tr")
        tds = trs[0].find_elements(By.TAG_NAME,"td")
        if alumi_wheel:
            self.set_ticked_check_box(tds[1])
        else:
            self.set_unticked_check_box(tds[1])
        if duplicate_reason != "":
            self.enter_text_popup_element(tds[3],duplicate_reason)
        tds = trs[1].find_elements(By.TAG_NAME, "td")
        if dismantling_cer_required:
            self.set_ticked_check_box(tds[1])
        else:
            self.set_unticked_check_box(tds[1])
        if urgent_dismantling:
            self.set_ticked_check_box(tds[3])
        else:
            self.set_unticked_check_box(tds[3])
        tds = trs[2].find_elements(By.TAG_NAME, "td")
        if urgent_dis_items != "":
            self.enter_text_popup_element(tds[1],urgent_dis_items)
        if others != "":
            self.enter_text_popup_element(tds[3], others)
        #image capture
        body_content = rows[8].find_element(By.TAG_NAME, "tbody")
        trs = body_content.find_elements(By.TAG_NAME,"tr")
        tds = trs[0].find_elements(By.TAG_NAME,"td")
        if removal_images:
            self.set_ticked_check_box(tds[1])
        else:
            self.set_unticked_check_box(tds[1])
        if dismarting_images:
            self.set_ticked_check_box(tds[3])
        else:
            self.set_unticked_check_box(tds[3])


        footer_dialog = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = footer_dialog.find_elements(By.TAG_NAME, "button")
        buttons[1].click()








    def calculate_cost(self,
                       weigh_tax=0,
                       automobile_tax=0,
                       compulsory_insurance=0,
                       freon_fee=0,
                       air_bag_fee=0,
                       all_recircle_fee=0,
                       deliver_fee=0,
                       other_fee=0):
        button = self.find_element(By.XPATH,self.BUTTON_COST_CALCULATE)
        button.click()
        time.sleep(2)
        refund_content = self.find_element(By.TAG_NAME,"app-popup-refund-assessment")
        items = refund_content.find_elements(By.XPATH, "./nz-row")

        if weigh_tax != 0:
            nz_cols = items[0].find_elements(By.TAG_NAME,"nz-col")
            self.set_ticked_check_box(nz_cols[0])
            time.sleep(1)
            self.enter_text_popup_element(nz_cols[1],str(weigh_tax))
        if automobile_tax != 0:
            nz_cols = items[1].find_elements(By.TAG_NAME, "nz-col")
            self.set_ticked_check_box(nz_cols[0])
            time.sleep(1)
            self.enter_text_popup_element(nz_cols[1], str(automobile_tax))
        if compulsory_insurance != 0:
            nz_cols = items[2].find_elements(By.TAG_NAME, "nz-col")
            self.set_ticked_check_box(nz_cols[0])
            time.sleep(1)
            self.enter_text_popup_element(nz_cols[1], str(compulsory_insurance))
        if freon_fee != 0:
            nz_cols = items[3].find_elements(By.TAG_NAME, "nz-col")
            self.set_ticked_check_box(nz_cols[0])
            time.sleep(1)
            self.enter_text_popup_element(nz_cols[1], str(freon_fee))
        if air_bag_fee != 0:
            nz_cols = items[4].find_elements(By.TAG_NAME, "nz-col")
            self.set_ticked_check_box(nz_cols[0])
            time.sleep(1)
            self.enter_text_popup_element(nz_cols[1], str(air_bag_fee))
        if all_recircle_fee != 0:
            nz_cols = items[5].find_elements(By.TAG_NAME, "nz-col")
            self.set_ticked_check_box(nz_cols[0])
            time.sleep(1)
            self.enter_text_popup_element(nz_cols[1], str(all_recircle_fee))
        if deliver_fee != 0:
            nz_cols = items[6].find_elements(By.TAG_NAME, "nz-col")
            self.set_ticked_check_box(nz_cols[0])
            time.sleep(1)
            self.enter_text_popup_element(nz_cols[1], str(deliver_fee))
        if other_fee != 0:
            nz_cols = items[7].find_elements(By.TAG_NAME, "nz-col")
            self.set_ticked_check_box(nz_cols[0])
            time.sleep(1)
            self.enter_text_popup_element(nz_cols[1], str(other_fee))
        time.sleep(2)
        footer_dialog = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = footer_dialog.find_elements(By.TAG_NAME, "button")
        buttons[1].click()
    def do_request_assessment(self,notes):
        button = self.find_element(By.XPATH,self.BUTTON_REQUEST_ASSETMENT)
        button.click()
        time.sleep(2)
        dialog = self.find_element(By.TAG_NAME, "app-popup-request-department-assess")
        child_divs = dialog.find_elements(By.XPATH, "./div")

        checkboxes_department = child_divs[0].find_elements(By.TAG_NAME, "nz-checkbox-wrapper")
        checkboxes_department[4].click()
        p2_checkboxes = child_divs[1].find_elements(By.TAG_NAME, "input")
        p2_checkboxes[0].click()
        time.sleep(1)
        p2_checkboxes[1].click()
        txt_area = child_divs[2].find_element(By.TAG_NAME, "textarea")
        txt_area.send_keys(Keys.CONTROL + "a")
        txt_area.send_keys(Keys.DELETE)
        txt_area.send_keys(notes)
        txt_area.send_keys(Keys.ENTER)
        footer = self.find_element(By.XPATH, "//*[contains(@class, 'ant-modal-footer')]")
        buttons = footer.find_elements(By.TAG_NAME, "button")
        buttons[1].click()
    def do_reject_assetment(self,note=""):
        button = self.find_element(By.XPATH,self.BUTTON_ACCESSTMENT)
        button.click()
        time.sleep(3)
        usecarassetment_obj = UsedCarAssetment(self.driver)
        usecarassetment_obj.do_reject_assetment(note = note)
    def do_confirm_assessment(self,car_price="",cost_rate="",note="",role="ds"):
        if role == "ds":
            button = self.find_element(By.XPATH, self.BUTTON_ACCESSTMENT)
            button.click()
            time.sleep(3)
            usecarassetment_obj = UsedCarAssetment(self.driver)
            usecarassetment_obj.do_confirm_assetment_ds(car_price=car_price,cost_rate=cost_rate,note=note)
        elif role == "production":
            button = self.find_element(By.XPATH, self.BUTTON_ACCESSTMENT)
            button.click()
            time.sleep(3)
            usecarassetment_obj = UsedCarAssetment(self.driver)
            if usecarassetment_obj.get_number_of_parts() == 0:
                usecarassetment_obj.do_add_parts_production_role(number_of_parts=3)
            usecarassetment_obj.do_confirm_assetment_production(note=note)
        elif role == "export":
            button = self.find_element(By.XPATH, self.BUTTON_ACCESSTMENT)
            button.click()
            time.sleep(2)
            usecarassetment_obj = UsedCarAssetment(self.driver)
            usecarassetment_obj.do_confirm_assetment_export(car_price=car_price,cost_rate=cost_rate,note=note)




































