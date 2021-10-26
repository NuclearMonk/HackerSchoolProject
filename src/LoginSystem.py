from abc import ABC, abstractmethod
from os.path import exists


class AuthenticatioSystem(ABC):

    @abstractmethod
    def user_exists(self, username):
        pass

    @abstractmethod
    def register_user(self, username, password):
        pass

    @abstractmethod
    def login_user(self, user, password):
        pass


# stores username and password combos in plain text in a file named in the constructor
class InsecureAuthenticationSystem(AuthenticatioSystem):

    def __init__(self, credentials_file):
        self.filename = credentials_file
        if not exists(f"./{credentials_file}"):
            open(credentials_file, "w").close()

     def read_users(self):
         creds_file = open(self.filename)
         for line in creds_file.readlines():
             user, pass = line.split("")

    def user_exists(self, username):
        pass

    def register_user(self, username, password):
        pass

    def login_user(self, user, password):
        pass


authSystem = InsecureAuthenticationSystem("user_credentials.txt")
