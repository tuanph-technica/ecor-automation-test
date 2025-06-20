import random
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
@pytest.mark.test_car_valuation
class TestCarValuation(softest.TestCase):
    logger = LogGen.loggen()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = LogIn(self.driver)
        self.ut = Utils()

    def test_requested_tab(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        #user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "ds1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_evaluation_list = hp.get_car_valuation_list()
        time.sleep(2)
        tab_index = 1
        car_evaluation_list.select_valuation_list_tab(tab_index)
        time.sleep(1)
        # perform search random
        chasis_numbers = car_evaluation_list.get_all_chasis_number_in_list(tab_index=1)
        if len(chasis_numbers) > 0:
            rand_index = random.randint(0,len(chasis_numbers)-1)
            chasis_num = chasis_numbers[rand_index]
            numcar = car_evaluation_list.search_requested(management_number=2,search_text=chasis_num)
            self.ut.asset_ge(numcar,1)
            numvar = car_evaluation_list.search_using_filter(tab_index=1,chassis_number=chasis_num)
            self.ut.asset_ge(numcar, 1)

        car_on_validation = car_evaluation_list.do_valuate_item_in_list()
        car_on_validation.do_confirm_valuated_ds_role(valuation_price="120000",car_cost_rate="75",note="OK")
        car_on_validation.come_back()
        hp.logout()
    def test_search_valuating_tab(self, number_of_test=1):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        # user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "ds1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_evaluation_list = hp.get_car_valuation_list()
        time.sleep(2)
        tab_index = 5
        car_evaluation_list.select_valuation_list_tab(tab_index)
        chasis_numbers = car_evaluation_list.get_all_chasis_number_in_list(tab_index=tab_index)
        random_indexes = random.sample(range(0,len(chasis_numbers)), number_of_test)
        for index in random_indexes:
            numcar = car_evaluation_list.search_valuating(management_number=2,search_text=chasis_numbers[index])
            self.ut.asset_ge(numcar,1)
            time.sleep(1)
            car_evaluation_list.enter_reset_valuating()
            numcar = car_evaluation_list.search_using_filter(tab_index=tab_index,chassis_number=chasis_numbers[index])
            self.ut.asset_ge(numcar,1)
            time.sleep(1)
            car_evaluation_list.enter_reset_valuating()
        hp.logout()
        
    def test_search_valuated_tab(self,number_of_test=1):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        # user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "ds1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_evaluation_list = hp.get_car_valuation_list()
        time.sleep(2)
        tab_index = 7
        car_evaluation_list.select_valuation_list_tab(tab_index)
        chasis_numbers = car_evaluation_list.get_all_chasis_number_in_list(tab_index=tab_index)
        random_indexes = random.sample(range(0, len(chasis_numbers)), number_of_test)
        for index in random_indexes:
            numcar = car_evaluation_list.search_valuated(management_number=2,search_text=chasis_numbers[index])
            self.ut.asset_ge(numcar,1)
            time.sleep(1)
            car_evaluation_list.enter_reset_valuated()
            numcar = car_evaluation_list.search_using_filter(tab_index=tab_index,chassis_number=chasis_numbers[index])
            self.ut.asset_ge(numcar,1)
            time.sleep(1)
            car_evaluation_list.enter_reset_valuated()


    def test_get_valuated_car_in_list(self):
        user_name = "ds1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_evaluation_list = hp.get_car_valuation_list()
        time.sleep(2)
        tab_index = 7
        car_evaluation_list.select_valuation_list_tab(tab_index)
        car_evaluation = car_evaluation_list.select_car_valuation()
        car_evaluation.go_back_to_valuation_list()

    def test_assort_part_in_list(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        # user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_evaluation_list = hp.get_car_valuation_list()
        time.sleep(2)
        tab_index = 7
        car_evaluation_list.select_valuation_list_tab(tab_index)
        car_evaluation_list.do_assort_part()
        time.sleep(2)
        hp.logout()
    def test_auto_part_in_list(self):
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_evaluation_list = hp.get_car_valuation_list()
        time.sleep(2)
        tab_index = 7
        car_evaluation_list.select_valuation_list_tab(tab_index)
        car_evaluation_list.do_auto_assort()
        time.sleep(2)





    def test_search_assorted_tab(self,number_of_test=1):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        # user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "ds1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_evaluation_list = hp.get_car_valuation_list()
        time.sleep(2)
        tab_index = 9
        car_evaluation_list.select_valuation_list_tab(tab_index)
        chasis_numbers = car_evaluation_list.get_all_chasis_number_in_list(tab_index=tab_index)
        random_indexes = random.sample(range(0, len(chasis_numbers)), number_of_test)
        for index in random_indexes:
            numcar = car_evaluation_list.search_assorted(management_number=2, search_text=chasis_numbers[index])
            self.ut.asset_ge(numcar, 1)
            time.sleep(1)
            car_evaluation_list.enter_reset_assorted()
            numcar = car_evaluation_list.search_using_filter(tab_index=tab_index, chassis_number=chasis_numbers[index])
            self.ut.asset_ge(numcar, 1)
            time.sleep(1)
            car_evaluation_list.enter_reset_assorted()
        time.sleep(1)
        hp.logout()
        time.sleep(1)




















