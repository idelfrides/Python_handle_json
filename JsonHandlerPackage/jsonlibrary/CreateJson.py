""" Create Json module """

from os.path import dirname, realpath, isfile
import json
from JsonHandlerPackage.json_utils import Utils as util_m


class CreateJson(object):
    """ Create Json files class """

    def __init__(self):
        """ init method """

        self.j_utils = util_m.Utils()
        x = 'Simeao'
        self.default_data = {
            "dev_name": x, 
            "company": 'Padtec', 
            "role": 'Full stack dev', 
            "country": 'Brazil'
        }

    def create_json(self, filepath, newdata=None):
        """ create a new json file"""

        if newdata is None:
            newdata = self.default_data
        else:
            pass        

        if not isfile(filepath):             
            with open(filepath, 'w') as f:
                json.dump(newdata, f, indent=4, sort_keys=True, separators=(',', ': '))
            self.j_utils.success_information()
            return True

        if isfile(filepath):
            self.j_utils.already_exists_information()
            return False

    
