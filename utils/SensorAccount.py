from instaloader import Instaloader, Profile
import numpy as np





class SensorAccount:

    def __init__ (self, username: str = None, password: str = None, load: bool = False):
        """
        This is a SensorAccount it is used to gather important information from Instagram without risking the actual account
        
        ---------------------

        """
        self.Instagram = Instaloader()

        if load == False: # then try to login in and create an Instagram instance
            self.Instagram.login(username, password)
        
        elif load == True: #then try to load from an instaloader file
            self.Instagram.load_session_from_file(username)

        else:
            raise ValueError ("load is neither True or False")


    #GET DATA

    
    #WORKFLOW

    def perform_workflow (self):
        pass