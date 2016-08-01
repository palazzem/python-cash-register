class CashRegister(object):
    """
    The CashRegister class provides a minimal class which should
    be extended to write custom cash register implementations.

    When writing a new model, the following methods must be
    overridden to handle validity checks required by high-level
    APIs:
    """
    def __init__(self, name, supported_commands=[], connection=None):
        # supported commands should not be changed
        # for any reasons, otherwise a wrong command may
        # damage the cash register.
        self.name = name
        self._supported_commands = supported_commands
        # list of current commands that has not been executed
        # at the moment
        self._commands = []
        self._connection = connection

    def get_supported_commands(self):
        """
        Returns a new list of supported commands. The list
        is copied to prevent any changes to the list of
        supported commands. Remember that using wrong
        commands may cause unexpected behaviors.
        """
        return list(self._supported_commands)

    def send(self):
        """
        Sends data to the cash register. It iterates over the
        self._commands list, opening and closing the
        connection automatically.
        """
        if len(self._commands) > 0:
            # open the connection
            self._connection.open()
            # iterate and send commands
            for command in self._commands:
                self._connection.write(command)
            # force to get the data out *now*
            self._connection.flush()
            # close the connection
            self._connection.close()
