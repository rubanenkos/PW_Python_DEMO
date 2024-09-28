from enum import Enum

class Users(Enum):
    STANDARD_USER = {
        "title": "standard_user",
        "username": "standard_user",
        "password": "secret_sauce",
    }
    ERROR_USER = {
        "title": "error_user",
        "username": "error_user",
        "password": "secret_sauce",
    }
    UNREGISTERED_USER = {
        "title": "unregistered_user",
        "username": "unregistered_user",
        "password": "unregistered_user",
    }
    LOCKED_OUT_USER = {
        "title": "locked_out_user",
        "username": "locked_out_user",
        "password": "secret_sauce",
    }


    @property
    def TITLE(self):
        return self.value["title"]

    @property
    def USERNAME(self):
        return self.value["username"]

    @property
    def PASSWORD(self):
        return self.value["password"]

