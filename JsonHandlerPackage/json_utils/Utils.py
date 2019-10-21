""" Utilitaries recourses module """
import time


class Utils(object):
    """ Utilitaries recourses """

    def success_info(self):
        """ Show SUCCESS ACTION 
            information to user """
        
        info = """
        -------------------------------
        ------  SUCCESS ACTION --------
        -------------------------------

         Action performed successfully.
        """
        print('{}'.format(info))

    def not_exists_info(self):
        """ Show NOT EXISTS FILE
            information to user """
        
        info = """
        -------------------------------
        ------ FILE NOT EXISTS --------
        -------------------------------

              File do not exists.
        """
        print('{}'.format(info))

    def already_exists_info(self):
        """ Show ALREADY EXISTS FILE 
            information to user """
        
        info = """
        -------------------------------
        ------- ALREADY EXISTS --------
        -------------------------------
        
            The file aleady exists.
        """
        print('{}'.format(info))

    def danger_info(self):
        """ Show DANGER ACTION 
            information to user """
        
        info = """
        -------------------------------
        ------- DANGER ACTION --------
        -------------------------------
        
            This is a danger a action.
        """
        print('{}'.format(info))
        time.sleep(7)

        print("\n\n Enter yes to continue or quit to abord")
        try:
            option = input('\n\n Enter your choice:  ')
        except Exception as er:
            print('\n PYTHON SAID: {} - {} \n {} - {}'.format(er, er.__cause__, er.__class__, er.__context__))
            self.danger_info()
        else:
            if option  in ['yes', 'quit']:
                return option
            else:
                print('\n\n INVALID OPTION ')
                self.danger_info() 
        finally:
            pass

    
