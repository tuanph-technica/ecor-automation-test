from utilities import ExcelUtil
import random
import ast
class GenerateData:
    def __init__(self,test_data_file,status=""):
        row_counts = ExcelUtil.getRowCount(test_data_file,sheetName='Sheet1')
        self.test_data = []
        self.data_file_name = test_data_file
        for row_num in range(2,row_counts+1):

            obj = {
                'maker': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 1),
                'eng_maker': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 2),
                'car_name': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 3),
                'eng_car_name': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 4),
                'model_name': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 5),
                'year': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 6),
                'chassis_no': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 7),
                'grade': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 8),
                'eng_grade': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 9),
                'vehicle_type': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 10),
                'eng_vehicle_type': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 11),
                'displacement': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 12),
                'weight': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 13),
                'mileage': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 14),
                'chassis_number': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 15),
                'color': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 16),
                'minor_change': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 17),
                'purpose': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 18),
                'supplier_type': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 19),
                'supplier_name': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 20),
                'supplier_addr': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 21),
                'evaluation_points': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 22),
                'exterior_condition': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 23),
                'interior_condition': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 24),
                'immovable_suspension': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 25),
                'immovable_engine': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 26),
                'immovable_accident_disability': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 27),
                'immovable_battery_dead': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 28),
                'immovable_other': ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 29),
                'registration_date':ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 30),
                'status':     ExcelUtil.readData(test_data_file, 'Sheet1', row_num, 31),
            }
            if status == "":
                self.test_data.append(obj)
            elif obj['status']  == status:
                self.test_data.append(obj)

    def suffle(self):
        random.shuffle(self.test_data)
    def get_data_len(self):
        return len(self.test_data)
    def get_data_by_index(self,index):
        return self.test_data[index]
    def write_data_at_index(self,row_index,column_index,data_value):
        ExcelUtil.writeData(self.data_file_name,"Sheet1",row_index,column_index,data_value)
    def get_index_from_chasis_num(self,chasis_num):
        ret = -1
        for data in self.test_data:
            ret = ret + 1
            if str(data["chassis_number"]).find(str(chasis_num)) >= 0:
                break
        return ret
class PurchaseData:
    def __init__(self,purchase_data_file):
        row_counts = ExcelUtil.getRowCount(purchase_data_file, sheetName='Sheet1')
        self.test_data = []
        self.data_file_name = purchase_data_file
        for row_num in range(2, row_counts + 1):

            obj = {

                'register_number': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 1),
                'sale_pic': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 2),
                'purpose': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 3),
                'product_flow': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 4),
                'supplier_type': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 5),
                'supplier_name': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 6),
                'supplier_address': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 7),
                'picup_address': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 8),
                'picup_place': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 9),
                'picup_deadline': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 10),
                'confirm': ast.literal_eval(ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 11)),
                'original': ast.literal_eval(ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 12)),
                'transfer_permission': ast.literal_eval(ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 13)),
                'include_vat': ast.literal_eval(ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 14)),
                'vat': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 15),
                'car_price': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 16),
                'weight_tax': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 17),
                'recycle_fee': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 18),
                'compulsory_insurance': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 19),
                'automobile_tax': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 20),
                'domestic': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 21),
                'ds': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 22),
                'material': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 23),
                'export': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 24),
                'alumi_wheel': ast.literal_eval(ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 25)),
                'duplicate_reason': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 26),
                'dismantling_cer_required': ast.literal_eval(ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 27)),
                'urgent_dismantling': ast.literal_eval(ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 28)),
                'urgent_dis_items': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 29),
                'others': ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 30),
                'removal_images': ast.literal_eval(ExcelUtil.readData(purchase_data_file, 'Sheet1', row_num, 31)),
            }
            self.test_data.append(obj)
    def get_purchase_record(self):
        data_len = len(self.test_data)
        index = random.randint(0,data_len-1)
        return self.test_data[index]













