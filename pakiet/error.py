class Error(Exception):
    """Klasa nadrzędna wyjątków
    """
    pass

class ZlaWartoscNominalu(Error):
    """Wyjatek, ktory jest wyrzucany w przypadku 
    wlozenia monety lub banknotu o złym nominale.
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class BrakMonetExeption(Error):
    """Wyjatek, ktory jest wyrzucany w przypadku 
    nie wrzucenia monet, a kliknięcia przycisk zatwierdź.
    """
    def __str__(self):
        return str("Pieniądze nie zostały wrzucone!")

class ZlyNumerRejestracyjnyException(Error):
    """Wyjatek, ktory jest wyrzucany w przypadku 
    nie podania numeru rejestracyjnego.
    """
    def __str__(self):
        return str("Brak podanego prawidłowego numeru rejestracyjnego!")