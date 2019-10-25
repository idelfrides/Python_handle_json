""" Main module hold main method """

from JsonHandlerPackage import CreateJson
from JsonHandlerPackage import ReadJson
from JsonHandlerPackage import UpdateJson
from JsonHandlerPackage import DeleteJson
from JsonHandlerPackage import AddRecord
from os.path import dirname, realpath, join
import time


class MainJson(ReadJson, UpdateJson):
    """ Main Json class """

    def __init__(self):
        self.root = dirname(realpath(__file__))
        self.path_data = join(self.root, 'files_json/dev.json')
        self.ctj = CreateJson()
        self.dtj = DeleteJson()
        self.add = AddRecord()


    def main(self):
        """ main method """  

        t_sleep = 2

        initial_content = {
            "dev_name": 'Idelfrides', 
            "company": 'Izio', 
            "role": 'Back-end dev', 
            "country": 'Brasil'
        }

        status = self.ctj.create_json(self.path_data, initial_content)
        
        """
        new_content = {
            "dev_name": 'obama', 
            "company": 'ibm', 
            "role": 'dasigner', 
            "country": 'USA'
        }"""

        # status = UpdateJson().update_many(self.path_data, new_content)
        # status = UpdateJson().update_one(self.path_data, 'dev_name','WAR MACHINE')
        
        # status = self.dtj.delete_one(self.path_data, 'level')
        # status = self.dtj.delete_many(self.path_data, ['salary','age'])
        
        # status = self.add.add_record(self.path_data, {"age": 29, "salary": 500, "level": 'JR'})
        
        if status is False:
            print('\n\n RESULT:  ', status)
            time.sleep(t_sleep)
            print('\n\n')
            exit()
        else:
            print('\n\n RESULT:  ', status)
            time.sleep(t_sleep)
        
        data = ReadJson().retrieve_many(self.path_data)   
        # data = ReadJson().retrieve_one(self.path_data, 'dev_name')   
        
        if data is not False:
            print('\n\n')
            print(data)

        if data is False:
            print('\n\n\n')
            exit()

        print('\n\n\n')


if __name__ == '__main__':
    mj = MainJson()
    mj.main()
