"""Module: Add records to Json"""

from os.path import dirname, realpath, isfile
import json
from JsonHandlerPackage.json_utils import Utils as util_m


class AddRecord(object):
    """ Add new records to Json """
 
    def __init__(self):
        self.j_utils = util_m.Utils()

    def add_record(self, filepath, new_record):
        """ Add one or many news records to file 
        
            :param filepath: the absolute path to the json file 
            :type filepath: str
            :param new_record: a coillection of attribute and each value
            :type knew_recordey: dict
            :rtype: Boolean 
        """

        if isfile(filepath):
            with open(filepath) as f:
                new_data = json.load(f)
            
            keys = list(new_record)
            values = list(new_record.values())
            for i in range(len(new_record)):
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



