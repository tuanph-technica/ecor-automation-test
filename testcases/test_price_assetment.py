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
REGISTER_COLUMN_TEST_RESULT_IDX = 35
CAR_AI_PRICE_TEST_RESULT_IDX = 36
PART_AI_PRICE_TEST_RESULT_IDX = 37
PART_CO_AI_PRICE_TEST_RESULT_IDX = 38
MATERIAL_AI_PRICE_TEST_RESULT_IDX = 39



@pytest.mark.usefixtures("setup")
@pytest.mark.test_price_assetment
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

    def test_car_unaccessed(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        time.sleep(2)
        car_assetment_list = hp.assessment_car()
        time.sleep(2)
        car_assetment_list.select_assetment_list_tab(1)


    def test_car_assesment(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")

        user_name = "sale1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        time.sleep(2)
        car_assetment_list = hp.assessment_car()
        time.sleep(2)
        
        car_assetment_list.select_assetment_list_tab(1)
        num_car = car_assetment_list.unassessed_search(management_number=1, dropdown_source="国内生産部", dropdown_person="古山",
                                      input_date="2025/04/28")
        self.ut.asset_ge(num_car,1)
        data_len = self.generate_data.get_data_len()
        for i in range(data_len):
            data_obj = self.generate_data.get_data_by_index(i)
            num_car = car_assetment_list.unassessed_search_using_filter(chassis_number=data_obj['chassis_no'])
            self.ut.asset_ge(num_car, 1)

        car_assetment_list.select_assetment_list_tab(7)
        num_car = car_assetment_list.all_search(management_number=1,dropdown_source=0,input_date="2025/04/28",dropdown_person=1)
        self.ut.asset_ge(num_car, 1)
        
        car_assetment_list.select_assetment_list_tab(1)
        car_assetment_list.do_batch_accessetment(number_of_cars=3,notes="test")
        car_assetment_list.do_unpurchase_batch(number_of_cars=3)
        car_assetment_list.do_purchase(number_of_cars=4)
        car_assetment = car_assetment_list.get_car_assetment_detail()
        car_assetment.calculate_cost(freon_fee=10,air_bag_fee=20)
        car_assetment.do_request_assessment("test text")

        car_assetment.do_purchase(txt_register_val="12345678", sale_pic=True, purpose=True, production_flow=True,
                                  supplier_type=2,
                                  supplier_name="aaa", picup_addr="bbb", picup_place="ccc", picup_deadline="2025/04/01",
                                  document_type=True,original_unavailable=True,transfer_permission=True,
                                  include_vat=True,car_price="135000",weight_tax="10",recycle_fee="20",compulsory_insurance="30",
                                  automobile_tax="6",domestic="20",ds="10",material="5",export="9",alumi_wheel=True,duplicate_reason="aaa",
                                  dismantling_cer_required=False,urgent_dismantling=True,urgent_dis_items="bbb",others="ccc",removal_images=True,
                                  dismarting_images=True)
        time.sleep(2)
        car_assetment.click_back_to_assetment_list()
        hp.logout()
        time.sleep(5)

    def test_other(self):
        i = 1
        """
        data_len = self.generate_data.get_data_len()
        for i in range(data_len):
            print(i)
            data_obj = self.generate_data.get_data_by_index(i)
            chasis_number = data_obj['chassis_number']
            car_ai_price_expected = data_obj['car_ai_price']
            part_ai_price_expected = data_obj['part_ai_price']
            co_part_ai_price_expected = data_obj['co_part_ai_price']
            material_price_expected = data_obj['material_price']

        car_assetment_obj = hp.assessment_car()
        time.sleep(1)
        car_assetment_obj.select_assetment_list_tab(7)
        time.sleep(2)

        car_assetment_obj.unassessed_search(management_number=2,
                                            text_search="aaa",
                                            dropdown_source=3,
                                            input_date="2025/02/13",
                                            dropdown_person=2)
        time.sleep(3)

        car_assetment_obj.assessing_search(management_number=2,
                                           text_search="aaa",
                                           dropdown_source=3,
                                           input_date="2025/02/13",
                                           dropdown_person=2)

        car_assetment_obj.assessed_search(management_number=2,
                                          text_search="aaa",
                                          dropdown_source=3,
                                          input_date="2025/02/13",
                                          dropdown_person=2)

        car_assetment_obj.all_search(management_number=2,
                                     text_search="aaa",
                                     dropdown_source=3,
                                     input_date="2025/02/13",
                                     dropdown_person=2)

        car_assetment_obj.unassessed_search_using_filter(management_number="aaaa",
                                                         car_maker=1,
                                                         car_name=1,
                                                         model=1,
                                                         chassis_number="bbbb",
                                                         mile_age="34000-100000",
                                                         displacement="600-1500",
                                                         sale_pic=3,
                                                         supplier=4,
                                                         input_date="2025/02/03-2025-03-02",
                                                         source=3)

        car_assetment_obj.assessing_search_using_filter(management_number="aaaa",
                                                        car_maker=1,
                                                        car_name=1,
                                                        model=1,
                                                        chassis_number="bbbb",
                                                        mile_age="34000-100000",
                                                        displacement="600-1500",
                                                        sale_pic=3,
                                                        supplier=4,
                                                        input_date="2025/02/03-2025-03-02",
                                                        source=3)

        car_assetment_obj.all_search_using_filter(management_number="aaaa",
                                                  car_maker=1,
                                                  car_name=1,
                                                  model=1,
                                                  chassis_number="bbbb",
                                                  mile_age="34000-100000",
                                                  displacement="600-1500",
                                                  sale_pic=3,
                                                  supplier=4,
                                                  input_date="2025/02/03-2025-03-02",
                                                  assetment_status=1,
                                                  source=3)

        car_assetment_obj.click_select_search()
        time.sleep(2)
        car_assetment_obj.select_search_option(1)
        time.sleep(3)
        ret = car_assetment_obj.do_search(chasis_number)
        time.sleep(2)
        self.ut.assertItem(ret, True)
        if ret == True:
            car_assetment_detail = car_assetment_obj.get_car_assetment_detail(1)
            time.sleep(3)
            row_index = i + 2
            if self.ut.assertItem(car_assetment_detail.get_ai_car_price_available(), car_ai_price_expected) == True:
                self.generate_data.write_data_at_index(row_index, CAR_AI_PRICE_TEST_RESULT_IDX, 'o')
            else:
                self.generate_data.write_data_at_index(row_index, CAR_AI_PRICE_TEST_RESULT_IDX, 'x')
            if self.ut.assertItem(car_assetment_detail.get_ai_part_price_avaiable(), part_ai_price_expected) == True:
                self.generate_data.write_data_at_index(row_index, PART_AI_PRICE_TEST_RESULT_IDX, 'o')
                self.generate_data.write_data_at_index(row_index, PART_CO_AI_PRICE_TEST_RESULT_IDX, 'o')
            else:
                self.generate_data.write_data_at_index(row_index, PART_AI_PRICE_TEST_RESULT_IDX, 'x')
                self.generate_data.write_data_at_index(row_index, PART_CO_AI_PRICE_TEST_RESULT_IDX, 'x')
            if self.ut.assertItem(car_assetment_detail.get_ai_material_price_avaiable(),
                                  material_price_expected) == True:
                self.generate_data.write_data_at_index(row_index, MATERIAL_AI_PRICE_TEST_RESULT_IDX, 'o')
            else:
                self.generate_data.write_data_at_index(row_index, MATERIAL_AI_PRICE_TEST_RESULT_IDX, 'x')

            if car_assetment_detail.get_ai_car_price_available() == 1:
                self.ut.assertItem(car_assetment_detail.get_access_purchase_price(), True)
                self.ut.assertItem(car_assetment_detail.asset_car_price_detail(), True)
                self.ut.assertItem(car_assetment_detail.asset_part_price_detail(), True)
                self.ut.assertItem(car_assetment_detail.asset_material_price_detail(), True)
            car_assetment_detail.click_back_to_assetment_list()
    """
    def test_car_assetment_with_ds(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "ds1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        time.sleep(2)
        car_assetment_list = hp.assessment_car()
        time.sleep(2)
        car_assetment_list.select_assetment_list_tab(1)
        # get all chasis number
        chasis_numbers = car_assetment_list.get_all_chasis_number_in_list()
        # search
        num_charsis_number = len(chasis_numbers)
        chasis_number_index = random.randint(0,num_charsis_number-1)
        # do search in list
        num_car = car_assetment_list.requested_search(management_number=1,text_search=chasis_numbers[chasis_number_index])
        self.ut.asset_ge(num_car,1)
        # do search in filter
        num_car = car_assetment_list.requested_search_using_filter(chassis_number=chasis_numbers[chasis_number_index])
        self.ut.asset_ge(num_car, 1)
        # get request access car and then access price for this car
        car_request_assetment = car_assetment_list.get_car_assetment_detail()
        car_request_assetment.do_reject_assetment(note="note1")
        car_request_assetment.click_back_to_assetment_list()
        car_request_assetment = car_assetment_list.get_car_assetment_detail()
        car_request_assetment.do_confirm_assessment(car_price="200000",cost_rate=33,note="OK")
        car_request_assetment.click_back_to_assetment_list()















