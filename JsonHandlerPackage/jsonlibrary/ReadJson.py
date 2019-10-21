""" Read Json module """

from os.path import dirname, realpath, isfile
import json
from JsonHandlerPackage.json_utils import Utils as util_m


class ReadJson(object):
    """ Read Json files """

    def __init__(self):
        self.j_utils = util_m.Utils()
    
    def retrieve_many(self, filepath):
        """ Retrieve(read) all content inside a json file 
            
            :param filepath: the absolute path to the json file will be read
            :type filepath: str
            :rtype: Dict data or Boolean 
        """

        if isfile(filepath):
            with open(filepath) as f:
                return json.load(f)   
            self.j_utils.success_information()
        else:
            self.j_utils.not_exists_information()
            return False

    def retrieve_one(self, filepath, attribute):
        """ Retrieve(read) a value from a attribute 

            :param filepath: the absolute path to the json file will be read
            :type filepath: str
            :param attribute: the name of attribute that goinna be read
            :type attribute: str
            :rtype: attribute value or Boolean 
        """

        if isfile(filepath):
            with open(filepath) as f:
                data = json.load(f)   
                return data[attribute]  
            self.j_utils.success_information()        
        else:
            self.j_utils.not_exists_information()
            return False

   
