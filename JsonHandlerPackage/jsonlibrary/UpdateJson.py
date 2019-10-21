""" Update Json module """

from os.path import dirname, realpath, isfile
import json
from JsonHandlerPackage.json_utils import Utils as util_m


class UpdateJson(object):
    """ Update Json files """

    def __init__(self):
        self.j_utils = util_m.Utils()


    def update_many(self, filepath, new_dictionary):
        """ Update many records in the file
        
            :param filepath: the absolute path to the json file will be read
            :type filepath: str
            :param new_dictionary: the new dictionary data to set
            :type new_dictionary: dict
            :rtype: Boolean 
        """

        if isfile(filepath):
            with open(filepath) as f:
                new_data = json.load(f)

            keys = list(new_dictionary)
            values = list(new_dictionary.values())

            for i in range(len(new_dictionary)):
                new_data[keys[i]] = values[i]
            
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

    def update_one(self, filepath, *args):
        """ Update a record in the josn file

            WARNING: For *args values,
                     respect the order: key, value
            
            :param filepath: the absolute path to the json file will be read
            :type filepath: str
            :param *args: conventional python variable to get many arguments
            :type *args: various
            :rtype: Boolean 
        """
        if isfile(filepath):
            with open(filepath) as f:
                new_data = json.load(f)

            new_data[args[0]] = args[1]
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

