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
class TestHomePage(softest.TestCase):

    logger = LogGen.loggen()
    # debug
    #generate_data = GenerateData(".//testdata/car_infomation_testing_jpn.xlsx")
    # batch file
    #generate_data = GenerateData(".//testdata/car_infomation_testing_jpn.xlsx")
    #generate_data.suffle()
    @pytest.fixture(autouse=True)

    def class_setup(self):
       self.login = LogIn(self.driver)
       self.ut = Utils()
    def test_request_assesment(self):
        self.logger.info("************Test_Homepage*********")
        self.logger.info("************Starting UC 1*********")
        user_name, pass_word = self.ut.get_account_info(self.role)
        hp = self.login.do_login(user_name, pass_word)

        time.sleep(2)
        car_assetment_obj = hp.assessment_car()
        car_assetment_obj.enter_unassetment_tab()
        car_assetment_obj.request_assetment()
        time.sleep(5)

