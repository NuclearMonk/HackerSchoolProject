from abc import ABC, abstractmethod
from os.path import exists


class AuthenticationSystem(ABC):

    # returns true if the user exists
    @abstractmethod
    def user_exists(self, username):
        pass

    # registers a new user
    # returns False if that username is in use
    @abstractmethod
    def register_user(self, username, password):
        pass

    #updates an already existing user credentials
    @abstractmethod
    def update_user_credentials(self, username, new_password):
        pass

    # returns True if the provided credentials match any of the existing ones
    # returns false otherwise
    @abstractmethod
    def login_user(self, user, password):
        pass


# stores username and password combos in plain text in a file named in the constructor
# DO NOT USE FOR ANYTHING EVER!!!!
class InsecureAuthenticationSystem(AuthenticationSystem):

    # takes the name of the file, creates said file if it doesn't exist
    def __init__(self, credentials_file):
        self.__credentials_file = credentials_file
        self.__user_credentials_dict = {}
        if not exists(f"./{self.__credentials_file}"):
            open(self.__credentials_file, "w").close()
        self.__credentials_load()

    # loads credentials from the file to the dictionary
    def __credentials_load(self):
        credentials = open(self.__credentials_file)
        for line in credentials:
            user, password = line.split(" : ")
            self.__user_credentials_dict[user] = password
        credentials.close()
    #writes the full dictionary overwriting the file
    def __credentials_store(self):
        credentials = open(self.__credentials_file, 'w')
        for user in self.__user_credentials_dict.keys():
            credentials.write(f"{user} : {self.__user_credentials_dict[user]}\n")
        credentials.close()

    def __user_password(self, user):
        return self.__user_credentials_dict[user]

    def user_exists(self, username):
        return username in self.__user_credentials_dict

    def register_user(self, username, password):
        if self.user_exists(username):
            return False
        self.__user_credentials_dict[username] = password
        self.__credentials_store()
        return True

    def update_user_credentials(self, username, new_password):
        self.__user_credentials_dict[username] = new_password

    def login_user(self, user, password):
        if self.user_exists(user):
            if password == self.__user_password(user):
                return True
        return False


authSystem = InsecureAuthenticationSystem("user_credentials.txt")
