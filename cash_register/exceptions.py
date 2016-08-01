class NotSupportedCommand(Exception):
    """
    Exception raised when a command is not supported by the given
    cash register model.
    """
    default_message = 'Command not supported in this cash register model'

    def __init__(self, message=None):
        if message is not None:
            self.message = message
        else:
            self.message = self.default_message

    def __str__(self):
        return self.message
