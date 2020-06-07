class Error(Exception):
    pass

class ZlaWartoscNominalu(Error):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)