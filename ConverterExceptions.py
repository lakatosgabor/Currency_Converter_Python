class Currencies:
    def __init__(self,currency,shortened,exchange,country):
        self.__curency = currency
        self.__shortened = shortened
        self.__exchange = exchange
        self.__country = country


class MissingDataException(Exception):
    def __init__(self,value):
        self.__value = value

    def __str__(self):
        return "The " + self.__value + " text box is empty. You should provide this mandatory data!"


class TypeError(Exception):
    pass

class TypeError2(Exception):
    def __init__(self,value):
        self.__value = value

    def __str__(self):
        return "The format of the " + self.__value + " text box is not correct!"


class SameDataException(Exception):
    pass