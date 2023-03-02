import pandas as pd
from utils.Classes import Post, Account

class KnowledgeBase:

    def __init__(self):
        """
        This is the KB \n
        this class is the Data Safe which is meant to gather important information,
        such that not always an API request has to be send \n
        \n
        --------
        """

        # create the DataFrames to store the Data about Posts and Accounts
        posts_df = pd.DataFrame()
        """
        ID      | TYPE    | NUM LIKES | PUBLISHER ACC ID | ####### | ####### | ####### | ####### | ####### |
        ___________________________________________________________________________________________________|
        1294fgkj| Image   | 307       | dfjh435nfdfofge4 | ...     | ...     | ...     | ...     | ...     |
        
        """
        accounts_df = pd.DataFrame()
        """
        ID      | BIO     | NUM POSTS | NUM FOLLOWERS    | PROFILENAME | ####### | ####### | ####### | ####### |
        _______________________________________________________________________________________________________|
        1294fgkj| Image   | 307       | dfjh435nfdfofge4 | ...         | ...     | ...     | ...     | ...     |
        
        """
    
    # ACCESS DATA

    def get_post (self, id: str):
        """
        This method returns the Post as POST object if a result was found otherwise it returns None
        """
        pass

    def get_account(self, id: str):
        """
        This method returns the Account as ACCOUNT object if a result was found otherwise it returns None
        """
        pass

    # search ????

    # CHANGE DATA

    def add_parameter_value(self, type, id, parameter, value):
        """
        This method adds a value to a cell, given that the cell is empty beforehand. Otherwise an Error is raised
        """
        pass

    def overwrite_parameter_value(self, type, id, parameter, value):
        """
        This method overwrites the value of a cell
        """
        pass

    def overwrite_column(self, type, id, dict):
        """
        This overwrites all given values in a column
        """
        pass

    # ADD DATA

    def add_post(self, post: Post):
        """
        This method adds a new Post to the Knowledgebase
        An Error is raised if the Post already exists
        """
        pass

    def add_account(self, account: Account):
        """
        This method adds a new Account to the Knowledgebase
        An Error is raised if the Account already exists
        """