

# base class for error class
class Error(Exception):
    def __init__(self, message):
        self.massage = message


class AlreadyInKeysOfDict(Error):
    def __init__(self, message="value already in keys of dictionary"):
        super().__init__(message)

