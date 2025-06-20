from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains
class CarValuationDetail(BaseDriver):
    CAR_VALUATION_ASSETMENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-detail/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/tbody/tr[2]/td[2]/div"
    PART_VALUATION_ASSETMENT = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-detail/nz-row[2]/nz-col[2]/nz-card[1]/div/nz-collapse/nz-collapse-panel/div[2]/div/nz-row/nz-col/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/tbody/tr[3]/td[2]/div"
    MODAL_CONTENT_AREA_CLASSNAME = "ant-modal-content"
    BUTTON_COME_BACK = "/html/body/app-root/app-home/nz-layout/nz-header/app-header/div/nz-row/nz-col[2]/button"
    BUTTON_CLOSE = "/html/body/app-root/app-home/nz-layout/nz-layout/nz-layout/nz-content/app-valuation-detail/nz-row[1]/nz-col[2]/nz-space/div[2]/button"
    def __init__(self,driver):
        super().__init__(driver=driver)
    def get_car_valuation_assetment(self):
        web_element = self.find_element(By.XPATH,self.CAR_VALUATION_ASSETMENT)
        print(web_element)
        return web_element.text
    def get_part_valuation_assetment(self):
        web_element = self.find_element(By.XPATH,self.PART_VALUATION_ASSETMENT)
        print(web_element)
        return web_element.text
    def go_back_to_valuation_list(self):
        button = self.find_element(By.XPATH,self.BUTTON_COME_BACK)
        button.click()
        time.sleep(2)
    def do_close_valuation_detail(self):
        button = self.find_element(By.XPATH,self.BUTTON_CLOSE)
        button.click()
        time.sleep(2)

    def enter_car_valuation_in_detail(self):
        web_element = self.find_element(By.XPATH, self.CAR_VALUATION_ASSETMENT)
        web_element.click()
        time.sleep(3)
        modal_area = self.find_element(By.CLASS_NAME,self.MODAL_CONTENT_AREA_CLASSNAME)
        rect = self.driver.execute_script("""
                var rect = arguments[0].getBoundingClientRect();
                return {
                    x: rect.x,
                    y: rect.y,
                    width: rect.width,
                    height: rect.height,
                    top: rect.top,
                    left: rect.left,
                    right: rect.right,
                    bottom: rect.bottom
                };
            """, modal_area)
        actions = ActionChains(self.driver)
        actions.move_by_offset(0, 0)
        actions.move_by_offset(rect['left']-2,rect['top']-2)
        actions.click()
        actions.perform()
        time.sleep(2)
    def enter_part_valuation_in_detail(self):
        web_element = self.find_element(By.XPATH, self.PART_VALUATION_ASSETMENT)
        web_element.click()
        time.sleep(3)
        modal_area = self.find_element(By.CLASS_NAME,self.MODAL_CONTENT_AREA_CLASSNAME)
        rect = self.driver.execute_script("""
                var rect = arguments[0].getBoundingClientRect();
                return {
                    x: rect.x,
                    y: rect.y,
                    width: rect.width,
                    height: rect.height,
                    top: rect.top,
                    left: rect.left,
                    right: rect.right,
                    bottom: rect.bottom
                };
            """, modal_area)
        actions = ActionChains(self.driver)
        actions.move_by_offset(0, 0)
        actions.move_by_offset(rect['left'] - 2, rect['top'] - 2)
        actions.click()
        actions.perform()
        time.sleep(2)







