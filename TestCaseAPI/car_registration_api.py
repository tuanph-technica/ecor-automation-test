import pytest
import softest
import time
from TestCaseAPI.base_api import APICall
class CarRegistrationAPI(APICall):
    def __init__(self,base_url,token):
        super().__init__(base_url,token)
    def get_car_names_from_maker(self,maker_code):
        api = "v1/catalog/car-name/" + maker_code
        response = self.get_request(api)
        return response

