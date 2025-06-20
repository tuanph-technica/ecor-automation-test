import random

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
@pytest.mark.test_part_management
class TestPartManagement(softest.TestCase):
    logger = LogGen.loggen()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = LogIn(self.driver)
        self.ut = Utils()

    def test_search_remove(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        #user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "export1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        part_management = hp.get_part_management()
        part_management.get_removed_tab()
        lst_chasis_number = part_management.get_all_chasis_number_in_list()
        for chasis_number in lst_chasis_number:
            numpart = part_management.search_part(request_num=2,search_text=chasis_number)
            self.ut.asset_ge(numpart,1)
            part_management.reset_search()
            numpart = part_management.search_parts_using_filter_button_tab_remove_produced(chasis_num=chasis_number)
            self.ut.asset_ge(numpart, 1)
            time.sleep(2)
            part_management.reset_search()
            time.sleep(2)
        hp.logout()
    def test_search_produced(self):
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        part_management = hp.get_part_management()
        part_management.get_produced_tab()
        lst_chasis_number = part_management.get_all_chasis_number_in_list()
        for chasis_number in lst_chasis_number:
            numpart = part_management.search_part(request_num=2, search_text=chasis_number)
            self.ut.asset_ge(numpart, 1)
            part_management.reset_search()
            numpart = part_management.search_parts_using_filter_button_tab_remove_produced(chasis_num=chasis_number)
            self.ut.asset_ge(numpart, 1)
            time.sleep(2)
            part_management.reset_search()
            time.sleep(2)
        hp.logout()

    def test_search_inproduction(self):
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        part_management = hp.get_part_management()
        part_management.get_inproduction_part_tab()
        lst_chasis_number = part_management.get_all_chasis_number_in_list()
        part_numbers = len(lst_chasis_number)
        num_test = random.randint(1,part_numbers-1)
        radom_indexes = random.sample(range(1,part_numbers-1),num_test)
        for index in radom_indexes:
            numpart = part_management.search_part(request_num=3, search_text=lst_chasis_number[index])
            self.ut.asset_ge(numpart, 1)
            part_management.reset_search()
            numpart = part_management.search_parts_using_filter_button_tab_stanby_and_in_production(chasis_num=lst_chasis_number[index])
            self.ut.asset_ge(numpart, 1)
            time.sleep(2)
            part_management.reset_search()
            time.sleep(2)
        hp.logout()
    def test_add_new_part(self):
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        part_management = hp.get_part_management()
        part_register = part_management.add_new_part()
        part_register.fill_info_specification(part_type=2,part_category=2,part_code=1,color="yellow",
                                              manufact_part_num="02",genuine_part_num="03",subsitute_num="04",part_maker="toyota")
        part_register.fill_info_condition(defect_score=2.5,defect_note="aaa",note_1="bbb",note_2="ccc")
        part_register.search_and_fill_basic_car_info(management_num="ccc")
        part_register.fill_inventory_and_processing(ware_house=1,production_pic=2,quantity="1",status=2,aquisition_route=1)
        part_register.fill_transaction_info(is_published=1,price="10000",retail_price=3000,brand_new_price=20000,transport_parttern=1,transport_classification=1,transport_fee="400")
        part_register.do_create_part()
        time.sleep(2)




