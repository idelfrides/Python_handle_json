""" Utilitaries recourses module """
import time
from textwrap import dedent

class Utils(object):
    """ Utilitaries recourses """

    def success_information(self):
        """ Show SUCCESS ACTION 
            information to user """
        
        info = dedent("""
        -------------------------------
        ------  SUCCESS ACTION --------
        
         Action performed successfully.
        -------------------------------
        """)
        print('{}'.format(info))

    def not_exists_information(self):
        """ Show NOT EXISTS FILE
            information to user """
        
        info = dedent("""
        -------------------------------
        ------ FILE NOT EXISTS --------
        
              File do not exists.
        -------------------------------
        """)
        print('{}'.format(info))

    def already_exists_information(self):
        """ Show ALREADY EXISTS FILE 
            information to user """
        
        info = dedent("""
        -------------------------------
        ------- ALREADY EXISTS --------
        
            The file aleady exists.
        -------------------------------
        """)
        print('{}'.format(info))

    def danger_information(self):
        """ Show DANGER ACTION 
            information to user """
        import pdb
        info = dedent("""
        -------------------------------
        ------- DANGER ACTION ---------
        
            This is a danger action.
        -------------------------------
        """)
        print('{}'.format(info))
        time.sleep(7)
        # pdb.set_trace()
        print("\n\n Enter yes to continue or quit to abord")

        try:
            option = input('\n\n Enter your choice >  ')
        except KeyboardInterrupt as ki:
            print('\n\n WARNING: Program Interrupted by user {}'.format(ki))
            print('\n CLASS:  {}'.format(ki.__class__))
            time.sleep(5)
            return 'quit'    
        else:
            print('option: ', option)
            if option in ['yes', 'quit']:
                return option
            else:
                print('\n\n INVALID OPTION ')
                time.sleep(5)
                self.danger_information() 
        finally:
            pass

    
    def own_quit(self):
        """ Show QUIT WARNING  
            information to user """
        
        info = dedent("""
        -------------------------------
        ------- QUIT WARNING ----------
        
            The app gonna be quited.
            See you later :)
        -------------------------------
        """)
        print('{}'.format(info))

