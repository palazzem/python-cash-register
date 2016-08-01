class Command(object):
    """
    The base Command class provides a minimal class which may be used
    for writing custom command implementations.

    Note that it's not intended as a way to create categories of
    commands, instead to provide a common way to create commands
    with the same behavior.
    """
    def __init__(self, name, description, command_string):
        """
        Each command should describe itself, with a string that defines
        what the command does. The command_string attribute, should be
        a string that could be changed through the string.format()
        method. In this way, the package's public APIs know how to
        transform user inputs in valid cash register serial commands.

        A proper example of this command could be:
            name -> 'sell'
            description -> 'this command add a record to the recipe'
            command_string -> '"{description}"{amount}*{quantity}'

        So that the public API could:
            command_string.format(description="Potatoes", amount=2.0, quantity=1.0)
        """
        self.name = name
        self.description = description
        self.command_string = command_string
