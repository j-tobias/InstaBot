from PIL import Image






### THE POST
# Keep in mind, that a Post can be:
# - Reel
# - Carousel
# - Image
# - Video

class Post:

    def __init__ (self, id: str = None, type: str = None, image: Image = None, num_likes: int = None, publisher_acc_id: str = None): #addditional parameters will be added
        """
        This is a POST \n
        this class represents a POST in the InstaBot 
        \n
        --------
        \n
        - id: is a string which allows the API to directly access the Post \n
        - type: 'Reel', 'Carousel', 'Image', 'Video' \n
        - image: if the type is an Image then the image parameter is the Image in the PIL format \n
        - num_likes: is the number of Likes the Post has \n
        - publisher_acc_id: is the ID of the Account which published the Post \n
        """
        self.id = id
        self.type = type
        self.image = image
        self.num_likes = num_likes
        self.publisher_acc_id = publisher_acc_id
        # ...

    # INITIALIZING

    def init_from_instaloader (self, profile: dict):
        """
        This method initializes Post by the Information given from the instaloader
        """
        pass

    # ACTIONS ON THE POST
    # those Methods need the Instagram Object

    def follow (self, instagram: object = None):
        """
        This method follows the Account which created the Post
        """
        pass

    def unfollow (self, instagram: object = None):
        """
        This method follows the Account which created the Post
        """
        pass

    def like (self, instagram: object = None):
        """
        This method likes the Post
        """
        pass

    def save (self, category: str = None, instagram: object = None):
        """
        This method saves the Post to a given category. If the cateory is None the Post will be saved to a rondom one 
        and if a none existing category is given - the respective category is created
        """
        pass

    def comment (self, comment: str, instagram: object = None):
        """
        This method comments the Post with the given comment string
        """
        pass

    # ACTIONS INSIDE THE BOT

    def add_to_KB (self):
        """
        Thid method adds the Post to the Knowledge Base
        """
        pass

    def is_already_known (self):
        """
        This method checks if the Image of the Post is identical to another Picture in the KB
        """
        pass


### Account

class Account:

    def __init__ (self, id: str = None, profilename:str = None, posts: list = [], num_followers: int = None, followers: list = [], bio: str = None, num_posts: int = None): #addditional parameters will be added
        """
        This is an ACCOUNT \n
        this class represents an ACCOUNT in the InstaBot 
        \n
        --------
        \n
        - id: is an Indentifier which allows direct access to the Account through the API \n
        - profilename: is the visible Profilename of the Account \n
        - posts: is a List of POST objects \n
        - num_followers: number of accounts which are following the Account \n
        - followers: a list of followers which are already in the KB (or which the Bot is also following) \n
        - bio: the short description under the profile Picture \n
        - num_posts: the number of Posts on the Account
        """

        self.id = id
        self.posts = posts
        self.num_followers = num_followers
        self.followers = followers
        self.bio = bio
        self.num_posts = num_posts
        # ...

    # INITIALIZING

    def init_from_instaloader (self, profile: dict):
        """
        This method initializes Acccount by the Information given from the instaloader
        """
        pass

    # ACTIONS ON THE POST
    # those Methods need the Instagram Object

    def follow (self, instagram: object = None):
        """
        This method follows the Account
        """
        pass

    def unfollow (self, instagram: object = None):
        """
        This method follows the Account
        """
        pass

    def message (message: str, instagram: object = None):
        """
        This method sends a direct message to the Account
        """
        pass

    # ACTIONS INSIDE THE BOT

    def add_to_KB (self):
        """
        Thid method adds the Account to the Knowledge Base
        """
        pass

    def is_already_known (self):
        """
        This method checks if the Account is already in the Knowledge Base
        """
        pass