import random
from sys import displayhook
from time import sleep

import pytest
import softest
import time
from pages.login import LogIn
from pages.ecor_home_page import EcorHomePage
from utilities.readProperties import ReadConfig
from utilities.utils import Utils
from utilities.customLogger import LogGen
from utilities.GenerateData import GenerateData
@pytest.mark.usefixtures("setup")
@pytest.mark.test_car_list_on_register
class TestCarListOnRegister(softest.TestCase):
    logger = LogGen.loggen()
    # debug


    # batch file
    # generate_data = GenerateData(".//testdata/car_infomation_testing_jpn.xlsx")
    # generate_data.suffle()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = LogIn(self.driver)
        self.ut = Utils()

    def test_search_all(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(1)
        data_len = self.generate_data.get_data_len()
        for i in range(data_len):
            data_obj = self.generate_data.get_data_by_index(i)
            ret = car_list.all_search(request_number=2, search_text=data_obj['chassis_no'], expected_record_num_result=1)
            self.ut.assertItem(ret, True)

        hp.logout()
        time.sleep(5)
    def test_search_negotiating(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(3)
        generate_data = GenerateData("..//testdata/car_infomation_testing_jpn.xlsx",status='registred')
        time.sleep(2)
        data_len = generate_data.get_data_len()
        for i in range(data_len):
            data_obj = generate_data.get_data_by_index(i)
            num_car = car_list.negotiating_search(request_number=2,text_search=data_obj['chassis_no'])
            self.ut.assertItem(num_car,1)
        car_list.enter_nego_reset()
        numcar = car_list.negotiating_search(source="営業部")
        self.ut.asset_ge(numcar, 1)
        car_list.enter_nego_reset()
        numcar = car_list.negotiating_search(sale_person=1)
        self.ut.asset_ge(numcar, 1)
        car_list.enter_nego_reset()
        num_car = car_list.negotiating_search(input_date="2025/04/25")
        self.ut.asset_ge(num_car, 1)
        hp.logout()
        time.sleep(5)
    
    def test_delele_multi_items_from_all_tab(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(1)
        time.sleep(2)
        car_list.delete_multi_car_selection(num_car_delete=3)
        hp.logout()
        time.sleep(5)

    def test_search_negotiating_with_filter(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(3)
        time.sleep(2)
        data_len = self.generate_data.get_data_len()
        for i in range(data_len):
            data_obj = self.generate_data.get_data_by_index(i)
            num_car = car_list.negotiating_search_with_popup_filter(chasis_number=data_obj['chassis_no'])
            self.ut.assertItem(num_car,1)

        for i in range(data_len):
            data_obj = self.generate_data.get_data_by_index(i)
            year_range = str(data_obj['year']-1) + "-" + str(data_obj['year']+1)

            num_car = car_list.negotiating_search_with_popup_filter(car_maker=data_obj['maker'],
                                                                    car_name=data_obj['car_name'],
                                                                    model=data_obj['model_name'],
                                                                    year= year_range,
                                                                    )
            self.ut.asset_ge(num_car, 1)
        hp.logout()
        time.sleep(3)
    
    def test_get_register_car_detail_all_tab(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(1)
        data_len = self.generate_data.get_data_len()
        for i in range(data_len):
            data_obj = self.generate_data.get_data_by_index(i)
            car_detail = car_list.get_car_detail(chasis_number=data_obj['chassis_no'])
            basic_car_info = car_detail.get_car_basic_infomation()
            car_detail.enter_back_button()
            time.sleep(2)
        hp.logout()
        time.sleep(2)
    
    def test_edit_register_car_detail_all_tab(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(1)
        data_len = self.generate_data.get_data_len()
        for i in range(data_len):
            data_obj = self.generate_data.get_data_by_index(i)
            car_detail = car_list.get_car_detail(chasis_number=data_obj['chassis_no'])
            car_detail.edit_car_condition()
            car_detail.enter_back_button()
            time.sleep(2)


    def test_storage_car_in_unstock_tab(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.storage_batch(number_of_car=3)
    def test_car_detail_genera_info(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(1)
        data_len = self.generate_data.get_data_len()
        random_index = random.randint(1,data_len-1)
        data_obj = self.generate_data.get_data_by_index(random_index)
        car_detail = car_list.get_car_detail(chasis_number=data_obj['chassis_no'])
        general_info = car_detail.get_confirmmation_document()

        car_detail.edit_car_condition(evaluation_point=4, repare_history=0, external_cond=2, interior_cond=3,
                                      immovable_suspense=1)




































