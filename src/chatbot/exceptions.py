
class _SpWebBaseError(Exception):
    """
    Internal Base exception
    """
    def __init__(self, message):
        """
        Constructor

        :param message: information about the exception
        :returns: an instance of PsQaError
        """
        self.message = message

    def __str__(self):
        """
        Overloading the __str__ method so that the exception will be printed
        correctly when it's casted with str().

        :returns: exception in string
        """
        message = [self.message]
        return ''.join(message)


class UserNotFoundError(_SpWebBaseError):
    pass
