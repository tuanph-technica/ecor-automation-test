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
@pytest.mark.test_car_production_manager
class TestCarProductionManager(softest.TestCase):
    NUM_COLUMN_PRODUCTION_LIST = 9
    logger = LogGen.loggen()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = LogIn(self.driver)
        self.ut = Utils()
    def test_production_list(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        # user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_manager = hp.get_car_production_manager()
        num_columns = car_production_manager.get_production_manager_column_counts()
        self.ut.assertItem(num_columns,self.NUM_COLUMN_PRODUCTION_LIST)
        hp.logout()
        time.sleep(2)
    def test_create_outcome(self):
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_manager = hp.get_car_production_manager()
        num_records = car_production_manager.get_number_product_from_list()
        if num_records > 0:
            index = random.randint(0,num_records-1)
            car_production_detail = car_production_manager.get_product_from_list(index)
            time.sleep(2)
            car_production_detail.create_outcome()
            time.sleep(2)
        hp.logout()
    def test_search_out_come(self):
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_manager = hp.get_car_production_manager()
        # outcome domestic
        num_outcome = car_production_manager.search_outcome(department_index=0)
        self.ut.asset_ge(num_outcome,1)
        car_production_manager.reset_outcome_list_search()
        # outcome material
        num_outcome = car_production_manager.search_outcome(department_index=1)
        self.ut.assertItem(num_outcome, 0)
        hp.logout()
    def test_outcome_detail(self):
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_manager = hp.get_car_production_manager()
        num_outcome = car_production_manager.search_outcome(department_index=0)
        if num_outcome > 0:
            outcome_index = random.randint(0,num_outcome-1)
            outcome_detail = car_production_manager.get_product_outcome_from_list(outcome_index=outcome_index)
            # test outcome detail here

            #comeback to production screen
            outcome_detail.go_back()
        hp.logout()
    def test_production_list_with_export_account(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        # user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "export1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_manager = hp.get_car_production_manager()
        num_columns = car_production_manager.get_production_manager_column_counts()
        self.ut.assertItem(num_columns, self.NUM_COLUMN_PRODUCTION_LIST)
        hp.logout()
        time.sleep(2)
    def test_production_list_with_material_account(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        # user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "material1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_manager = hp.get_car_production_manager()
        num_columns = car_production_manager.get_production_manager_column_counts()
        self.ut.assertItem(num_columns, self.NUM_COLUMN_PRODUCTION_LIST)
        hp.logout()
        time.sleep(2)
    def test_production_list_with_apg_account(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        # user_name, pass_word = self.ut.get_account_info(self.role)
        user_name = "agp1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_manager = hp.get_car_production_manager_from_apg_user()
        num_columns = car_production_manager.get_production_manager_column_counts()
        self.ut.assertItem(num_columns, self.NUM_COLUMN_PRODUCTION_LIST)
        hp.logout()
        time.sleep(2)

    def test_create_outcome_with_export(self):
        user_name = "export1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_manager = hp.get_car_production_manager()
        num_records = car_production_manager.get_number_product_from_list()
        if num_records > 0:
            index = random.randint(0, num_records - 1)
            car_production_detail = car_production_manager.get_product_from_list(index)
            time.sleep(2)
            car_production_detail.create_outcome()
            time.sleep(2)
        hp.logout()




















        #car_production_detail = car_production_manager.get_product_from_list(0)
        #car_production_detail.create_outcome()
        #time.sleep(2)
        #outcome_detail = car_production_manager.get_product_outcome_from_list(0)
        #time.sleep(3)
        #outcome_detail.go_back()
        time.sleep(3)



