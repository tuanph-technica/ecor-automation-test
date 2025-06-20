import datetime
import random
from sys import displayhook
from time import sleep
from datetime import datetime,timedelta
import pytest
import softest
import time
from pages.login import LogIn
from pages.ecor_home_page import EcorHomePage
from utilities.readProperties import ReadConfig
from utilities.utils import Utils
from utilities.customLogger import LogGen
from utilities.GenerateData import GenerateData, PurchaseData

REGISTERED_STATUS = 'registered'
DELETED_STATUS = "deleted"
REQUEST_SENT_STATUS = "request_sent"
UNPURCHASE_STATUS = "unpurchase"
PURCHASED_STATUS = "bought"
STORAGED_STATUS = "storaged"
VALUATED_STATUS = "valuated"
ASSORTED = "assorted"
PLANED = "planed"

STATUS_COLUMN_IDX_JPN = 31
REGISTERED_DATE_COLUMN_IDX = 30
DATA_TEST_JAPAN_PATH = "..//testdata/car_infomation_testing_jpn.xlsx" # for debuging
PURCHASE_DATA_FILE_NAME = "..//testdata/purchase.xlsx" # for debuging
#DATA_TEST_JAPAN_PATH = ".//testdata/car_infomation_testing_jpn.xlsx" batch file run
@pytest.mark.usefixtures("setup")
@pytest.mark.test_main_flow
class TestFlows(softest.TestCase):
    logger = LogGen.loggen()

    # batch file
    # generate_data = GenerateData(".//testdata/car_infomation_testing_jpn.xlsx")
    # generate_data.suffle()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = LogIn(self.driver)
        self.ut = Utils()
    def register_new_car(self):
        self.ut.generate_chasis_number(DATA_TEST_JAPAN_PATH)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH,status="new")
        self.logger.info("************Test_Flows*********")
        self.logger.info("************Test Scenario 1*********")
        user_name = "sale1"
        pass_word = "123456"
        hp = self.login.do_login(user_name, pass_word)
        time.sleep(2)
        data_len = generate_data.get_data_len()
        registered_index = random.randint(0, data_len - 1)
        registration = hp.registration_car()
        time.sleep(2)
        language = registration.get_page_language()
        data_obj = generate_data.get_data_by_index(registered_index)
        if language == 'JP':
            regist_result = registration.do_registration(
                data_obj['maker'],
                data_obj['car_name'],
                data_obj['model_name'],
                data_obj['year'],
                chasis_no=data_obj['chassis_number'],
                car_grade=data_obj['grade'],
                vehicle_type=data_obj['vehicle_type'],
                displacement=data_obj['displacement'],
                car_weight=data_obj['weight'],
                mileage=data_obj['mileage'],
                color=data_obj['color'],
                minor_change=data_obj['color'],
                purpose=data_obj['purpose'],
                supplier_type=data_obj['supplier_type'],
                supplier_name=data_obj['supplier_name'],
                supplier_address=data_obj['supplier_addr'],
                evaluation_point=str(data_obj['evaluation_points']),
                ex_valuation=data_obj['exterior_condition'],
                int_valuation=data_obj['interior_condition'],
                immove_suspension=data_obj['immovable_suspension'],
                immove_engine=data_obj['immovable_engine'],
                immove_accident=data_obj['immovable_accident_disability'],
                immove_battery=data_obj['immovable_battery_dead'],
                immove_others=data_obj['immovable_other'])
        else:
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
                color_index=data_obj['color'],
                minor_change=data_obj['color'],
                purpose=data_obj['purpose'],
                supplier_type=data_obj['supplier_type'],
                supplier_name=data_obj['supplier_name'],
                supplier_address=data_obj['supplier_addr'],
                evaluation_point=data_obj['evaluation_points'],
                ex_valuation=data_obj['exterior_condition'],
                int_valuation=data_obj['interior_condition'],
                immove_suspension=data_obj['immovable_suspension'],
                immove_engine=data_obj['immovable_engine'],
                immove_accident=data_obj['immovable_accident_disability'],
                immove_battery=data_obj['immovable_battery_dead'],
                immove_others=data_obj['immovable_other'])
        time.sleep(10)
        row_index = registered_index + 2
        if regist_result == 1:
            generate_data.write_data_at_index(row_index, STATUS_COLUMN_IDX_JPN,REGISTERED_STATUS)
            generate_data.write_data_at_index(row_index, REGISTERED_DATE_COLUMN_IDX,
                                              datetime.now().strftime("%Y/%m/%d"))

        else:
            generate_data.write_data_at_index(row_index, STATUS_COLUMN_IDX_JPN, 'registred failed')
        hp.logout()
    def do_search_negotiating(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(3)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH,REGISTERED_STATUS)
        data_len = generate_data.get_data_len()
        index = random.randint(0, data_len - 1)
        data_obj = generate_data.get_data_by_index(index)
        # search in grid
        num_car = car_list.negotiating_search(request_number=2, text_search=data_obj['chassis_number'])
        self.ut.assertItem(num_car, 1)
        car_list.enter_nego_reset()
        num_car = car_list.negotiating_search(source="営業部")
        self.ut.assertItem(num_car, 1)
        car_list.enter_nego_reset()
        num_car = car_list.negotiating_search(sale_person=1)
        self.ut.assertItem(num_car, 1)
        car_list.enter_nego_reset()
        num_car = car_list.negotiating_search(input_date=data_obj['registration_date'])
        self.ut.assertItem(num_car, 1)
        car_list.enter_nego_reset()
        #search using filter
        time.sleep(3)
        num_car = car_list.negotiating_search_with_popup_filter(chasis_number=data_obj['chassis_number'])
        self.ut.assertItem(num_car, 1)
        car_list.enter_nego_reset()
        time.sleep(3)
        num_car = car_list.negotiating_search_with_popup_filter(car_maker=data_obj['maker'],
                                                                car_name=data_obj['car_name'],
                                                                model=data_obj['model_name'])
        self.ut.assertItem(num_car, 1)
        car_list.enter_nego_reset()
    def do_delete_car(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(3)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, REGISTERED_STATUS)
        data_len = generate_data.get_data_len()
        index = random.randint(0, data_len - 1)
        data_obj = generate_data.get_data_by_index(index)
        num_car = car_list.negotiating_search(request_number=2, text_search=data_obj['chassis_number'])
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH)
        if num_car > 0:
            car_detail = car_list.get_car_detail(chasis_number=data_obj['chassis_number'],chasis_column_num=5)
            car_detail.delete_car()
            car_delete_index = generate_data.get_index_from_chasis_num(chasis_num=data_obj['chassis_number'])
            generate_data.write_data_at_index(car_delete_index+2,STATUS_COLUMN_IDX_JPN,"deleted")
        hp.logout()




    def do_check_deleted_car(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        car_list = hp.get_car_list()
        car_list.click_at_tab(17)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH,status=DELETED_STATUS)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            num_car = car_list.deleted_search(request_number=3,text_search=data_obj['chassis_number'])
            self.ut.asset_ge(num_car,1)
        hp.logout()
    def send_request_assetment(self):
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=REGISTERED_STATUS)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            time.sleep(2)
            car_assetment_list = hp.assessment_car()
            car_assetment_list.select_assetment_list_tab(1)
            car_detail = car_assetment_list.get_car_from_chasis_number(chassis_no=data_obj['chassis_number'])
            car_detail.do_request_assessment("please asset this car")
            generate_data = GenerateData(DATA_TEST_JAPAN_PATH)
            car_delete_index = generate_data.get_index_from_chasis_num(chasis_num=data_obj['chassis_number'])
            generate_data.write_data_at_index(car_delete_index + 2, STATUS_COLUMN_IDX_JPN, REQUEST_SENT_STATUS)
            car_detail.click_back_to_assetment_list()
        hp.logout()
    def confirm_assetment(self):
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=REQUEST_SENT_STATUS)
        if generate_data.get_data_len() > 0:
            # ds confirmation

            user_name = "ds1"
            password = "123456"
            hp = self.login.do_login(user_name, password)
            data_obj = generate_data.get_data_by_index(0)
            car_assetment_list = hp.assessment_car()
            car_assetment_list.select_assetment_list_tab(1)
            car_assetment_detail = car_assetment_list.get_car_assetment_detail(chassis_number=data_obj['chassis_number'])
            car_assetment_detail.do_confirm_assessment(car_price="100000",cost_rate=75,note="ds confirmed")
            car_assetment_detail.click_back_to_assetment_list()
            hp.logout()
            
            # production confirmation
            user_name = "production1"
            password = "123456"
            hp = self.login.do_login(user_name, password)
            data_obj = generate_data.get_data_by_index(0)
            car_assetment_list = hp.assessment_car()
            car_assetment_list.select_assetment_list_tab(1)
            car_assetment_detail = car_assetment_list.get_car_assetment_detail(
                chassis_number=data_obj['chassis_number'])

            car_assetment_detail.do_confirm_assessment(note="production confirmed",role="production")
            car_assetment_detail.click_back_to_assetment_list()


            user_name = "export1"
            password = "123456"
            hp = self.login.do_login(user_name, password)
            data_obj = generate_data.get_data_by_index(0)
            car_assetment_list = hp.assessment_car()
            car_assetment_list.select_assetment_list_tab(1)


            car_assetment_detail = car_assetment_list.get_car_assetment_detail(
                chassis_number=data_obj['chassis_number'])
            if car_assetment_detail != None:
                car_assetment_detail.do_confirm_assessment(car_price="50000",cost_rate="80", note= "production confirmed", role="export")
                car_assetment_detail.click_back_to_assetment_list()






    def do_unpurchase(self):
        user_name = "sale1"
        password = "123456"
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=REGISTERED_STATUS)
        tab_index=1
        if generate_data.get_data_len() == 0:
            generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=REQUEST_SENT_STATUS)
            tab_index = 3
        hp = self.login.do_login(user_name, password)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            time.sleep(2)
            car_assetment_list = hp.assessment_car()
            car_assetment_list.select_assetment_list_tab(tab_index)
            car_detail = car_assetment_list.get_car_from_chasis_number(chassis_no=data_obj['chassis_number'])
            car_detail.do_unpurchase("2000",sale_pic=2,reason=2)
            car_detail.click_back_to_assetment_list()
            time.sleep(2)
            generate_data = GenerateData(DATA_TEST_JAPAN_PATH)
            car_delete_index = generate_data.get_index_from_chasis_num(chasis_num=data_obj['chassis_number'])
            generate_data.write_data_at_index(car_delete_index + 2, STATUS_COLUMN_IDX_JPN, UNPURCHASE_STATUS)
        hp.logout()

    def check_search_unpurchase_tab(self):
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=UNPURCHASE_STATUS)

        car_list = hp.get_car_list()
        car_list.click_at_tab(15)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            num_car = car_list.not_purchased_search(request_number=2,text_search=data_obj['chassis_number'])
            self.ut.asset_ge(num_car,1)


        hp.logout()








    def purchase_car(self):
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=REGISTERED_STATUS)
        purchase_data = PurchaseData(PURCHASE_DATA_FILE_NAME)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            time.sleep(2)
            car_assetment_list = hp.assessment_car()
            car_assetment_list.select_assetment_list_tab(1)
            num_car = car_assetment_list.unassessed_search(management_number=1,text_search=str(data_obj['chassis_number']))
            self.ut.asset_ge(num_car,1)
            car_assetment_list.reset_unassessed_search()
            time.sleep(3)
            num_car = car_assetment_list.unassessed_search_using_filter(car_maker=data_obj['maker'],
                                                                car_name=data_obj['car_name'],
                                                                )
            self.ut.asset_ge(num_car,1)
            car_assetment_list.reset_unassessed_search()
            car_detail = car_assetment_list.get_car_from_chasis_number(chassis_no=data_obj['chassis_number'])

            purchase_record = purchase_data.get_purchase_record()
            car_detail.do_purchase(txt_register_val=purchase_record["register_number"],
                                   sale_pic=purchase_record["sale_pic"],
                                   purpose=purchase_record["purpose"],
                                   production_flow=purchase_record["product_flow"],
                                   supplier_type=purchase_record["supplier_type"],
                                   supplier_name=purchase_record["supplier_name"],
                                   supplier_address=purchase_record["supplier_address"],
                                   picup_addr=purchase_record["picup_address"],
                                   picup_place=purchase_record["picup_place"],
                                   picup_deadline=purchase_record["picup_deadline"],
                                   confirmed=purchase_record["confirm"],
                                   original_unavailable=purchase_record["original"],
                                   transfer_permission=purchase_record["transfer_permission"],
                                   include_vat=purchase_record["include_vat"],
                                   car_price=purchase_record["car_price"],
                                   weight_tax=purchase_record["weight_tax"],
                                   recycle_fee=purchase_record["recycle_fee"],
                                   compulsory_insurance=purchase_record["compulsory_insurance"],
                                   automobile_tax=purchase_record["automobile_tax"],
                                   domestic=purchase_record["domestic"],
                                   ds=purchase_record["ds"],
                                   material=purchase_record["material"],
                                   export=purchase_record["export"],
                                   alumi_wheel=purchase_record["alumi_wheel"],
                                   duplicate_reason=purchase_record["duplicate_reason"],
                                   dismantling_cer_required=purchase_record["dismantling_cer_required"],
                                   urgent_dismantling=purchase_record["urgent_dismantling"],
                                   urgent_dis_items=purchase_record["urgent_dis_items"],
                                   others=purchase_record["others"],






            )
            time.sleep(2)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH)
        car_delete_index = generate_data.get_index_from_chasis_num(chasis_num=data_obj['chassis_number'])
        generate_data.write_data_at_index(car_delete_index + 2, STATUS_COLUMN_IDX_JPN, PURCHASED_STATUS)
        hp.logout()
        # now check in unstock tab
    def check_bought_data(self):
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=PURCHASED_STATUS)
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            car_list  = hp.get_car_list()
            car_list.click_at_tab(5)
            num_car = car_list.unstock_search(request_number=2,text_search=data_obj["chassis_number"])
            self.ut.asset_ge(num_car,1)
            car_list.enter_reset_unstock()
            num_car = car_list.unstocked_search_with_popup_filter(car_maker=data_obj["maker"],
                                                                  car_name=data_obj["car_name"],chasis_number=data_obj["chassis_number"])
            self.ut.asset_ge(num_car, 1)
        hp.logout()
    def do_storage_car(self):
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=PURCHASED_STATUS)
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            car_list = hp.get_car_list()
            car_list.storage_car(chasis_number=data_obj["chassis_number"])
            generate_data = GenerateData(DATA_TEST_JAPAN_PATH)
            car_storage_index = generate_data.get_index_from_chasis_num(chasis_num=data_obj['chassis_number'])
            generate_data.write_data_at_index(car_storage_index + 2, STATUS_COLUMN_IDX_JPN, STORAGED_STATUS)
        hp.logout()
    def check_storage_tab(self):
        user_name = "sale1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=STORAGED_STATUS)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            car_list = hp.get_car_list()
            car_list.click_at_tab(7)
            numcar = car_list.storage_search(request_number=2,text_search=data_obj["chassis_number"])
            self.ut.asset_ge(numcar,1)
            car_list.enter_storage_reset()
            numcar = car_list.storage_search_with_popup_filter(car_maker=data_obj["maker"],
                                                                  car_name=data_obj["car_name"],chasis_number=data_obj["chassis_number"])
            self.ut.asset_ge(numcar, 1)
            car_list.enter_storage_reset()
        hp.logout()



    def do_search_valuation(self,user_name,password):

        hp = self.login.do_login(user_name, password)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=STORAGED_STATUS)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            valuation_list = hp.get_car_valuation_list()
            valuation_list.select_valuation_list_tab(1)
            numcar = valuation_list.search_requested(management_number=2,search_text=data_obj["chassis_number"])
            self.ut.asset_ge(numcar,1)
            valuation_list.enter_reset_requested_button()
            valuation_list.search_using_filter(tab_index=1,car_maker=data_obj["maker"],car_name=data_obj["car_name"],
                                                           chassis_number=data_obj["chassis_number"])
        hp.logout()
    def do_valuation(self,user_name,password,data_obj=None):
        hp = self.login.do_login(user_name, password)
        valuation_list = hp.get_car_valuation_list()
        valuation_list.select_valuation_list_tab(1)
        car_valuation = valuation_list.do_valuate_item_in_list(chasis_number=data_obj["chassis_number"])
        if user_name == "ds1":
            car_valuation.do_confirm_valuated_ds_role(valuation_price="100000",car_cost_rate="70",note="ds valuated")
        elif user_name == "production1":
            car_valuation.do_confirm_valuated_production_role(note="production confirmed")
        elif user_name == "export1":
            car_valuation.do_confirm_export_valuate_used_car(valuation_price="110000",car_cost_rate="80",note="export used car valuated")
            car_valuation.do_valuate_export_part_by_select_list(select_num_cat=2,select_num_part=2,note="export parts valuated")

        time.sleep(3)
        hp.logout()
    def do_all_valuations(self):
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=STORAGED_STATUS)
        if generate_data.get_data_len() == 0:
            return
        data_obj = generate_data.get_data_by_index(0)
        #self.do_valuation(user_name="ds1",password="123456",data_obj=data_obj)
        #self.do_valuation(user_name="production1",password="123456",data_obj=data_obj)
        self.do_valuation(user_name="export1",password="123456",data_obj=data_obj)

        generate_data = GenerateData(DATA_TEST_JAPAN_PATH)
        car_valuated_index = generate_data.get_index_from_chasis_num(chasis_num=data_obj['chassis_number'])
        generate_data.write_data_at_index(car_valuated_index + 2, STATUS_COLUMN_IDX_JPN, VALUATED_STATUS)
    def do_all_assort_cars(self):
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=VALUATED_STATUS)
        if generate_data.get_data_len() == 0:
            return
        data_obj = generate_data.get_data_by_index(0)
        self.do_assort_cars(user_name="production1", pass_word="123456", data_obj=data_obj)
        time.sleep(2)
        self.do_assort_cars(user_name="export1",pass_word="123456",data_obj=data_obj)
        time.sleep(2)
        self.do_assort_cars(user_name="material1", pass_word="123456", data_obj=data_obj)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH)
        car_assorted_index = generate_data.get_index_from_chasis_num(chasis_num=data_obj['chassis_number'])
        generate_data.write_data_at_index(car_assorted_index + 2, STATUS_COLUMN_IDX_JPN, ASSORTED)
    def do_assort_cars(self,user_name="",pass_word="",data_obj=None):
        hp = self.login.do_login(user_name, pass_word)
        valuation_list = hp.get_car_valuation_list()
        valuation_list.select_valuation_list_tab(7)
        # do search valuated
        num_car = valuation_list.search_valuated(management_number=2,search_text=data_obj["chassis_number"])
        self.ut.asset_ge(num_car,1)
        valuation_list.do_auto_assort(chasis_number=data_obj["chassis_number"])
        """
        valuation_list.enter_reset_valuated()
        num_car = valuation_list.search_using_filter(tab_index=7,car_maker=data_obj["maker"],car_name=data_obj["car_name"],
                                                           chassis_number=data_obj["chassis_number"])
        self.ut.asset_ge(num_car, 1)
        valuation_list.enter_reset_valuated()
        valuation_list.search_valuated(management_number=2, search_text=data_obj["chassis_number"])
        valuation_list.do_auto_assort(chasis_number=data_obj["chassis_number"])
        """







    def do_product_plan_tasks(self,user_name,pass_word,data_obj,working_date=""):

        hp = self.login.do_login(user_name, pass_word)
        product_list = hp.get_car_production_list()
        if user_name == "export1":
            _list = product_list.get_product_export()
        elif user_name == "material1":
            _list = product_list.get_product_material()
        elif user_name == "production1":
            _list = product_list.get_product_domestic()

        # search in waiting list

        num_car = _list.search_waiting_list(management=1, text_search=data_obj['chassis_number'])
        self.ut.asset_ge(num_car, 1)
        _list.do_reset_search()
        # search using filter
        num_car = _list.search_waiting_list_using_filter(car_maker=data_obj['maker'],
                                                               car_name=data_obj['car_name'])
        self.ut.asset_ge(num_car, 1)

        # create plan:
        if user_name == "export1":
            plan = _list.create_new_plan_export(plan_date=working_date,AGP=True,DB=True,JOR=True,PG1=True,DOM=True)


        elif user_name == "production1":
            plan =_list.create_new_plan_domestic(working_date=working_date,working_persons="2",working_hours="3")
        elif user_name == "material1":
            plan = _list.create_new_plan_material(working_date=working_date,working_persons="4",working_hours=2)
        #plan.cancel_product_plan()
        plan.confirm_product_plan()
        hp.logout()
        
















    def do_document_car(self):
        user_name = "office1"
        password = "123456"
        hp = self.login.do_login(user_name, password)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=STORAGED_STATUS)
        if generate_data.get_data_len() > 0:
            data_obj = generate_data.get_data_by_index(0)
            car_list = hp.get_car_list()
            car_list.click_at_tab(7)
            car_list.do_document_car(data_obj["chassis_number"],reason_for_process="フロン")
        time.sleep(2)
        hp.logout()

    def make_production_plan_for_all_roles(self,working_date):
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH, status=ASSORTED)
        if generate_data.get_data_len() == 0:
            return
        data_obj = generate_data.get_data_by_index(0)
        self.do_product_plan_tasks(user_name="production1", pass_word="123456", data_obj=data_obj,
                                   working_date=working_date)
        time.sleep(3)
        self.do_product_plan_tasks(user_name="export1", pass_word="123456",data_obj=data_obj,working_date=working_date)
        time.sleep(3)
        self.do_product_plan_tasks(user_name="material1", pass_word="123456",data_obj=data_obj,working_date=working_date)
        generate_data = GenerateData(DATA_TEST_JAPAN_PATH)
        car_assorted_index = generate_data.get_index_from_chasis_num(chasis_num=data_obj['chassis_number'])
        generate_data.write_data_at_index(car_assorted_index + 2, STATUS_COLUMN_IDX_JPN, PLANED)

    def check_plans(self,user_name,pass_word,plan_date):
        hp = self.login.do_login(user_name, pass_word)
        product_list = hp.get_car_production_list()
        num_plan = product_list.search_plan_list(production_date=plan_date,department_index=0)
        self.ut.asset_ge(num_plan,1)
        product_list.enter_reset_search_button()
        num_plan = product_list.search_plan_list(production_date=plan_date, department_index=1)
        self.ut.asset_ge(num_plan, 1)
        product_list.enter_reset_search_button()
        num_plan = product_list.search_plan_list(production_date=plan_date, department_index=2)
        self.ut.asset_ge(num_plan, 1)
        product_list.enter_reset_search_button()
        hp.logout()
    def create_production_list(self,user_name="",pass_word="",plan_date = ""):
        hp = self.login.do_login(user_name, pass_word)
        product_list = hp.get_car_production_list()
        dep_name = ""
        if user_name == "production1":
            dep_name = "国内"
        elif user_name == "export1":
            dep_name = "海外"
        elif user_name == "material1":
            dep_name = "マテリアル"

        product_plan = product_list.get_plan_for_make_production_list(production_date=plan_date,dep_name=dep_name)
        if user_name == "production1":
            product_plan.create_domestic_production_list()
        elif user_name == "export1":
            product_plan.create_export_production_list()
        elif user_name == "material1":
            product_plan.create_material_production_list()
        hp.logout()


    def create_production_list_all_roles(self,plan_date=""):
        self.create_production_list(user_name="production1",pass_word="123456",plan_date=plan_date)
        self.create_production_list(user_name="export1", pass_word="123456", plan_date=plan_date)
        self.create_production_list(user_name="material1", pass_word="123456", plan_date=plan_date)

    def do_product_managers_tasks(self,user_name="",password="",date_=""):
        # login
        status_column = 11
        card_body_index = 1
        if user_name == "export1":
            status_column = 12
        elif user_name == "material1":
            status_column = 12
            card_body_index = 2
        hp = self.login.do_login(user_name, password)
        product_manager = hp.get_car_production_manager()
        production_detail = product_manager.get_production_plan_from_date(date_)
        chasis_numbers = production_detail.get_chasis_numbers_by_product_status("待機",status_column=status_column,card_boby_idx=card_body_index)
        production_detail.process_next_step(chasis_numbers=chasis_numbers,card_body_index=card_body_index)
        chasis_numbers = production_detail.get_chasis_numbers_by_product_status("生産待ち",status_column=status_column,card_boby_idx=card_body_index)
        production_detail.process_next_step(chasis_numbers=chasis_numbers,card_body_index=card_body_index)
        chasis_numbers = production_detail.get_chasis_numbers_by_product_status("生産中",status_column=status_column,card_boby_idx=card_body_index)
        if user_name == "export1" or user_name == "production1":
            for chasis_number in chasis_numbers:
                production_detail.produce_car_parts(chasis_number)
        production_detail.process_next_step(chasis_numbers=chasis_numbers,card_body_index=card_body_index)
        if user_name == "production1":
            production_detail.create_outcome_production()
        elif user_name == "export1":
            production_detail.create_outcome_export()
        elif user_name == "material1":
            production_detail.create_outcome_material()
        hp.logout()
    def do_product_managers_task_for_all_roles(self,date=""):
        #self.do_product_managers_tasks(user_name="production1",password="123456",date_=date)
        #self.do_product_managers_tasks(user_name="export1",password="123456",date_=date)
        self.do_product_managers_tasks(user_name="material1",password="123456",date_=date)
    def check_outcome_results(self,user_name="",pass_word="",production_date=""):
        department = ""
        if user_name == "production1":
            dep_name = "国内"
        elif user_name == "export1":
            dep_name = "海外"
        elif user_name == "material1":
            dep_name = "マテリアル"

        hp = self.login.do_login(user_name, pass_word)
        product_manager = hp.get_car_production_manager()
        out_come_num = product_manager.search_outcome(production_date=production_date,department=dep_name)
        self.ut.asset_ge(out_come_num,1)
        hp.logout()























    def test_do_purchase_car(self):
        #self.register_new_car()
        #self.purchase_car()
        #self.check_bought_data()
        #self.do_storage_car()
        #self.check_storage_tab()
        #self.do_search_valuation(user_name="ds1",password="123456")
        #self.do_search_valuation(user_name="export1", password="123456")
        #self.do_search_valuation(user_name="production1", password="123456")
        #self.do_search_valuation(user_name="material1", password="123456")
        #self.do_document_car()
        #self.do_all_valuations()
        #self.do_all_assort_cars()
        #plan_date = datetime.now().strftime('%Y/%m/%d')
        #self.make_production_plan_for_all_roles(plan_date)
        #self.check_plans(user_name="production1",pass_word="123456",plan_date=plan_date)
        #self.create_production_list_all_roles(plan_date="2025/06/20")
        #self.do_product_managers_task_for_all_roles(date="2025/06/20")
        self.check_outcome_results(user_name="production1",pass_word="123456",production_date="2025/06/20")
        self.check_outcome_results(user_name="export1",pass_word="123456",production_date="2025/06/20")
        self.check_outcome_results(user_name="material1", pass_word="123456", production_date="2025/06/20")









    def test_unpurchase_car(self):
        self.register_new_car()
        self.do_unpurchase()
        self.check_search_unpurchase_tab()
        time.sleep(2)
    def test_delete_car(self):
        self.register_new_car()
        self.do_delete_car()
        self.do_check_deleted_car()
    def test_accessment(self):
        #self.register_new_car()
        #self.send_request_assetment()
        self.confirm_assetment()
































