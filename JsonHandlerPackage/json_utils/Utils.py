""" Utilitaries recourses module """
import time


class Utils(object):
    """ Utilitaries recourses """

    def success_information(self):
        """ Show SUCCESS ACTION 
            information to user """
        
        info = """
        -------------------------------
        ------  SUCCESS ACTION --------
        -------------------------------

         Action performed successfully.
        """
        print('{}'.format(info))

    def not_exists_information(self):
        """ Show NOT EXISTS FILE
            information to user """
        
        info = """
        -------------------------------
        ------ FILE NOT EXISTS --------
        -------------------------------

              File do not exists.
        """
        print('{}'.format(info))

    def already_exists_information(self):
        """ Show ALREADY EXISTS FILE 
            information to user """
        
        info = """
        -------------------------------
        ------- ALREADY EXISTS --------
        -------------------------------
        
            The file aleady exists.
        """
        print('{}'.format(info))

    def danger_information(self):
        """ Show DANGER ACTION 
            information to user """
        
        info = """
        -------------------------------
        ------- DANGER ACTION ---------
        -------------------------------
        
            This is a danger action.
        """
        print('{}'.format(info))
        time.sleep(7)

        print("\n\n Enter yes to continue or quit to abord")

        try:
            option = input('\n\n Enter your choice >  ')
        except KeyboardInterrupt as ki:
            print('\n\n WARNING: Program Interrupted by user {}'.format(ki))
            print('\n CLASS:  {}'.format(ki.__class__))
            time.sleep(5)
            return 'quit'    
        else:
            if option in ['yes', 'quit']:
                return option
            else:
                print('\n\n INVALID OPTION ')
                time.sleep(5)
                self.danger_information() 
        finally:
            pass

    
