import random

import softest

from utilities import ExcelUtil


class Utils(softest.TestCase):
    def assertListItemText(self,list,value):
        for item in list:
            print("The text is:  " + item.text)
            self.soft_assert(self.assertEquals,item.text,value)
            if item.text == value:
                print('test_past')
            else:
                print('test_failed')
    def assertItem(self,item,value):
        self.soft_assert(self.assertEquals,item,value)
        if item == value:
            return True
        else:
            return False
    def asset_ge(self,value_1,value_2):
        self.soft_assert(self.assertGreaterEqual,value_1,value_2)

        if value_1 >= value_2:
            return True
        else:
            return False


    def get_account_info(self,role):
        if role == "Sale":
            user_name = 'sale1'
            pass_word = '123456'
        elif role == "Ds":
            user_name = 'ds1'
            pass_word = '123456'
        elif role == "Domestic":
            user_name = 'production1'
            pass_word = '123456'
        elif role == "Export":
            user_name = 'export1'
            pass_word = '123456'
        elif role == "Material":
            user_name = 'material1'
            pass_word = '123456'
        else:
            user_name = 'sale1'
            pass_word = '123456'
        return user_name,pass_word
    @staticmethod
    def generate_chasis_number(test_data_file):
        row_counts = ExcelUtil.getRowCount(test_data_file, sheetName='Sheet1')
        for row_num in range(2, row_counts + 1):
            chassis_number = ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 15)
            if len(chassis_number) < 6:
                random_surffix = random.randint(10000,9999999)
                chassis_number = chassis_number + "-" + str(random_surffix)
                ExcelUtil.writeData(test_data_file,sheetName='Sheet1',row_num=row_num,columnno=15,data=chassis_number)









