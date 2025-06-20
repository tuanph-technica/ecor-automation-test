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
@pytest.mark.test_car_production
class TestCarProduction(softest.TestCase):
    logger = LogGen.loggen()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = LogIn(self.driver)
        self.ut = Utils()
    def test_search_domestic(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        domestic_list = car_production_list.get_product_domestic()
        chassis_numbers = domestic_list.get_all_car_chasis_number()
        number_of_test = random.randint(0,len(chassis_numbers)-1)
        if number_of_test > len(chassis_numbers):
            number_of_test = len(chassis_numbers)
        for i in range(number_of_test):
            numcar = domestic_list.search_waiting_list(management=1,text_search=chassis_numbers[i])
            self.ut.asset_ge(numcar,1)
            domestic_list.do_reset_search()
            numcar = domestic_list.search_waiting_list_using_filter(chasis_number=chassis_numbers[i])
            self.ut.asset_ge(numcar, 1)
            domestic_list.do_reset_search()
        time.sleep(3)
        hp.logout()
    def test_search_export(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "export1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        export_list = car_production_list.get_product_export()
        chassis_numbers = export_list.get_all_car_chasis_number()
        number_of_test = random.randint(0, len(chassis_numbers))
        if number_of_test > len(chassis_numbers):
            number_of_test = len(chassis_numbers)
        for i in range(number_of_test):
            numcar = export_list.search_waiting_list(management=1, text_search=chassis_numbers[i])
            self.ut.asset_ge(numcar, 1)
            export_list.do_reset_search()
            numcar = export_list.search_waiting_list_using_filter(chasis_number=chassis_numbers[i])
            self.ut.asset_ge(numcar, 1)
            export_list.do_reset_search()
        time.sleep(3)
        hp.logout()

    def test_search_agp(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        agp_list = car_production_list.get_product_agp()
        chassis_numbers = agp_list.get_all_car_chasis_number()
        number_of_test = random.randint(0, len(chassis_numbers))
        if number_of_test > len(chassis_numbers):
            number_of_test = len(chassis_numbers)
        for i in range(number_of_test):
            numcar = agp_list.search_waiting_list(management=1, text_search=chassis_numbers[i])
            self.ut.asset_ge(numcar, 1)
            agp_list.do_reset_search()
            numcar = agp_list.search_waiting_list_using_filter(chasis_number=chassis_numbers[i])
            self.ut.asset_ge(numcar, 1)
            agp_list.do_reset_search()
        time.sleep(3)
        hp.logout()
    def test_search_material(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        material_list = car_production_list.get_product_material()
        chassis_numbers = material_list.get_all_car_chasis_number()
        number_of_test = random.randint(0, len(chassis_numbers))
        if number_of_test > len(chassis_numbers):
            number_of_test = len(chassis_numbers)
        for i in range(number_of_test):
            numcar = material_list.search_waiting_list(management=1, text_search=chassis_numbers[i])
            self.ut.asset_ge(numcar, 1)
            material_list.do_reset_search()
            numcar = material_list.search_waiting_list_using_filter(chasis_number=chassis_numbers[i])
            self.ut.asset_ge(numcar, 1)
            material_list.do_reset_search()
        time.sleep(3)
        hp.logout()
    def test_create_domestic_plam(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        domestic_list = car_production_list.get_product_domestic()
        create_plan = domestic_list.create_new_plan_domestic(working_date="",working_persons=2,working_hours=3,working_minutes=1)
        create_plan.add_car_by_filter(request_num=1,production_flow=0)
        create_plan.remove_batch_cars(num_car_remove=2)
        create_plan.remove_car_from_table()
        create_plan.confirm_product_plan()
        time.sleep(2)
        hp.logout()
    def test_create_export_plan(self):
        user_name = "export1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        export_list = car_production_list.get_product_export()
        export_plan = export_list.create_new_plan_export(AGP=True, DB=True)
        time.sleep(2)
        export_plan.confirm_product_plan()
        time.sleep(3)
        hp.logout()
    def test_create_agp_plan(self):
        user_name = "agp1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list_from_agp_user()
        agp_list = car_production_list.get_product_agp()
        agp_plan = agp_list.create_new_plan_agp()
        time.sleep(2)
        agp_plan.confirm_product_plan()
        time.sleep(3)
        hp.logout()

    def test_create_material_plan(self):
        user_name = "material1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        material_list = car_production_list.get_product_material()
        material_plan = material_list.create_new_plan_material(working_date="",working_persons=2,working_hours=3,working_minutes=1)
        time.sleep(2)
        material_plan.confirm_product_plan()
        time.sleep(2)
        hp.logout()
    def test_search_plan(self):
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        car_production_list.search_plan_list(department_index=0)
        car_production_list.enter_reset_search_button()
        time.sleep(2)
        car_production_list.search_plan_list(department_index=1)
        car_production_list.enter_reset_search_button()
        time.sleep(2)
        car_production_list.search_plan_list(department_index=2)
        car_production_list.enter_reset_search_button()
        time.sleep(2)
        car_production_list.search_plan_list(department_index=3)
        car_production_list.enter_reset_search_button()
        time.sleep(2)
        hp.logout()
    def test_create_domestic_production_list(self):
        user_name = "production1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        car_production_list.search_plan_list(department_index=0)
        domestic_plan = car_production_list.select_plan_in_list()
        domestic_plan.create_domestic_production_list()
        hp.logout()
    def test_create_export_production_list(self):
        user_name = "export1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        car_production_list.search_plan_list(department_index=2)
        export_plan = car_production_list.select_plan_in_list()
        export_plan.create_export_production_list()
        hp.logout()
    def test_create_material_production_list(self):
        user_name = "material1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        car_production_list = hp.get_car_production_list()
        car_production_list.search_plan_list(department_index=1)
        material_plan = car_production_list.select_plan_in_list()
        material_plan.create_material_production_list()
        hp.logout()











