import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base.base_driver import BaseDriver
class ProductionParts(BaseDriver):
    BACK_BUTTON = "/html/body/app-root/app-home/nz-layout/nz-header/app-header/div/nz-row/nz-col[2]/button"
    def get_part_indexes_from_status(self,status):
        lst_indexes = []
        ant_body = self.find_element(By.TAG_NAME, "nz-table")
        body = ant_body.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME, "tr")
        for i in range(1, len(trs) - 1):
            tds = trs[i].find_elements(By.TAG_NAME, "td")
            if tds[7].text == status:
                lst_indexes.append(i)
        return lst_indexes
    def process_parts(self,part_indexes):
        if len(part_indexes) == 0:
            return
        ant_body = self.find_element(By.TAG_NAME, "nz-table")
        body = ant_body.find_element(By.TAG_NAME, "tbody")
        trs = body.find_elements(By.TAG_NAME, "tr")
        for index in part_indexes:
            tds = trs[index].find_elements(By.TAG_NAME,"td")
            input = tds[0].find_element(By.TAG_NAME, "input")
            input.click()
        title_footer = self.find_element(By.TAG_NAME, "nz-table-title-footer")
        button_process = title_footer.find_element(By.TAG_NAME, "button")
        button_process.click()


    def produce_parts(self):
        part_indexes = self.get_part_indexes_from_status(status="生産中")
        self.process_parts(part_indexes)
        part_indexes = self.get_part_indexes_from_status(status="Removed")
        self.process_parts(part_indexes)
        back_button = self.find_element(By.XPATH,self.BACK_BUTTON)
        back_button.click()
        time.sleep(5)






