""" Delete Json module """

from os.path import dirname, realpath, isfile
from JsonHandlerPackage.json_utils import Utils as util_m
import json, time


class DeleteJson(object):
    """ Delete Json files """

    def __init__(self):
        self.j_utils = util_m.Utils()


    def delete_many(self, filepath, keys2delete):
        """ Delete many records from json file
        
            :param filepath: the absolute path to the json file will be read
            :type filepath: str
            :param keys2delete: a list of keys name to be deleted
            :type keys2delete: list
            :rtype: Boolean 
        """

        option = self.j_utils.danger_information()
        print('\n option: ', option)
        if option == "quit":
            print('\n chosen quit')
            return False
        if option == 'yes':
            pass 
 
        if isfile(filepath):
            with open(filepath) as f:
                new_data = json.load(f)
                for i in range(len(keys2delete)):
                    new_data.pop(keys2delete[i])
                
            with open(filepath, 'w') as f:
                json.dump(
                    new_data, 
                    f, 
                    indent=4, 
                    sort_keys=True, 
                    separators=(',', ': ')
                )
            self.j_utils.success_information()
            return True
        else:
            self.j_utils.not_exists_information()
            return False


    def delete_one(self, filepath, key):
        """ Delete one record from file
        
            :param filepath: the absolute path to the json file 
            :type filepath: str
            :param key: the name of key to be deleted
            :type key: str
            :rtype: Boolean 
        """
          
        option = self.j_utils.danger_information()
        if option == 'quit':
            return False
        if option == 'yes':
            pass

        if isfile(filepath):
            with open(filepath) as f:
                new_data = json.load(f)
                new_data.pop(key)

            with open(filepath, 'w') as f:
                json.dump(
                    new_data, 
                    f, 
                    indent=4, 
                    sort_keys=True, 
                    separators=(',', ': ')
                )
            self.j_utils.success_information()
            return True
        else:
            self.j_utils.not_exists_information()
            return False
