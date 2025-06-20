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
STATUS_COLUMN_IDX_JPN = 31



@pytest.mark.usefixtures("setup")
@pytest.mark.test_car_registration
class TestHomePage(softest.TestCase):

    logger = LogGen.loggen()
    # debug
    generate_data = GenerateData("..//testdata/car_infomation_testing_jpn.xlsx")
    # batch file
    #generate_data = GenerateData(".//testdata/car_infomation_testing_jpn.xlsx")
    #generate_data.suffle()
    @pytest.fixture(autouse=True)

    def class_setup(self):
       self.login = LogIn(self.driver)
       self.ut = Utils()
    def test_registration_car(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name,pass_word = self.ut.get_account_info(self.role)
        hp = self.login.do_login(user_name,pass_word)
        time.sleep(2)
        data_len = self.generate_data.get_data_len()
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 2*********")
        registered_index = random.randint(0,data_len-1)
        registration = hp.registration_car()
        time.sleep(2)
        language = registration.get_page_language()
        data_obj = self.generate_data.get_data_by_index(registered_index)
        if language == 'JP':
            regist_result =registration.do_registration(
                data_obj['maker'],
                data_obj['car_name'],
                data_obj['model_name'],
                data_obj['year'],
                chasis_no=data_obj['chassis_no'],
                car_grade=data_obj['grade'],
                vehicle_type=data_obj['vehicle_type'],
                displacement= data_obj['displacement'],
                car_weight = data_obj['weight'],
                mileage= data_obj['mileage'],
                color = data_obj['color'],
                minor_change = data_obj['color'],
                purpose = data_obj['purpose'],
                supplier_type = data_obj['supplier_type'],
                supplier_name = data_obj['supplier_name'],
                supplier_address = data_obj['supplier_addr'],
                evaluation_point = str(data_obj['evaluation_points']),
                ex_valuation= data_obj['exterior_condition'],
                int_valuation= data_obj['interior_condition'],
                immove_suspension = data_obj['immovable_suspension'],
                immove_engine = data_obj['immovable_engine'],
                immove_accident = data_obj['immovable_accident_disability'],
                immove_battery = data_obj['immovable_battery_dead'],
                immove_others = data_obj['immovable_other']
            )
        else :
            regist_result = registration.do_registration(
                data_obj['eng_maker'],
                data_obj['eng_car_name'],
                data_obj['model_name'],
                data_obj['year'],
                chasis_no=data_obj['chassis_no'],
                car_grade=data_obj['eng_grade'],
                vehicle_type=data_obj['eng_vehicle_type'],
                displacement=data_obj['displacement'],
                car_weight=data_obj['weight'],
                mileage=data_obj['mileage'],
                color_index = data_obj['color'],
                minor_change = data_obj['color'],
                purpose = data_obj['purpose'],
                supplier_type = data_obj['supplier_type'],
                supplier_name = data_obj['supplier_name'],
                supplier_address = data_obj['supplier_addr'],
                evaluation_point = data_obj['evaluation_points'],
                ex_valuation = data_obj['exterior_condition'],
                int_valuation = data_obj['interior_condition'],
                immove_suspension = data_obj['immovable_suspension'],
                immove_engine = data_obj['immovable_engine'],
                immove_accident = data_obj['immovable_accident_disability'],
                immove_battery = data_obj['immovable_battery_dead'],
                immove_others = data_obj['immovable_other'])
        time.sleep(2)
        row_index = registered_index + 2
        if regist_result == 1:
            self.generate_data.write_data_at_index(row_index,STATUS_COLUMN_IDX_JPN,'registred')
        else:
            self.generate_data.write_data_at_index(row_index, STATUS_COLUMN_IDX_JPN, 'registred failed')
        time.sleep(2)









