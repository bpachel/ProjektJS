class Error(Exception):
    pass

class ZlaWartoscNominalu(Error):
    '''Wyjatek, ktory jest wyrzucany w przypadku 
    wlozenia monety lub banknotu o złym nominale.
    '''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)