from ..exceptions import NotSupportedCommand


class CashRegister(object):
    """
    The CashRegister class provides a minimal class which should
    be extended to write custom cash register implementations.

    When defining a new model, the following methods **must** be
    overridden to handle validity checks required by high-level
    APIs:
        * ``__init__``: just call the super() and set the
          _supported_commands attribute
        * ``sell_products``: define the sequence of commands
          required to print a recipe with the given products
    """
    def __init__(self, name, connection=None):
        self.name = name
        # supported commands should not be changed
        # for any reason, otherwise a wrong command may
        # damage the cash register
        self._supported_commands = []
        # list of current commands that are not been executed
        self._commands = []
        # store the connection object that sends commands
        # to the cash register
        self._connection = connection

    def connect(self, connection):
        """
        Provides the connection handler used to send commands
        to the cash register
        """
        self._connection = connection

    def get_supported_commands(self):
        """
        Returns a new list of supported commands. The list
        is copied to prevent any changes to the list of
        supported commands. Remember that using wrong
        commands may cause unexpected behaviors.
        """
        return list(self._supported_commands)

    def _add_command(self, command, params=None):
        """
        Adds the given command to the command list. This
        method also ensures that the command is a supported
        command, otherwise an exception is raised.
        """
        if command in self._supported_commands:
            command_string = command.build(params)
            self._commands.append(command_string)
        else:
            raise NotSupportedCommand

    def sell_products(self, products):
        """
        This method **must** be implemented to define the
        right sequence of commands required to print a
        recipe with the given products
        """
        raise NotImplementedError

    def send(self):
        """
        Sends data to the cash register. It iterates over the
        self._commands list, opening and closing the
        connection automatically.
        """
        if len(self._commands) > 0:
            # open the connection and iterates over the
            # _commands buffer
            self._connection.open()
            for command in self._commands:
                self._connection.write(command)
            # force to get the data out *now* and
            # close the connection
            self._connection.flush()
            self._connection.close()
            # remove sent commands from the internal list
            self._commands = []

    def __str__(self):
        """
        Representation of the CashRegister object
        """
        return self.name
