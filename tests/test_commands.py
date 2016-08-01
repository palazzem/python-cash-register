from cash_register.commands.base import Command
from cash_register.commands.sell import clear, close, sell


def test_base_command():
    """
    The base Command should create a proper instance. The
    test creates a new fake command and checks the instance
    attributes and __str__ informal representation.
    """
    command = Command('sell', 'sell command', '5.90H1R1')
    # instance attributes
    assert command.name == 'sell'
    assert command.description == 'sell command'
    assert command.command_string == '5.90H1R1'
    # string informal representation
    assert str(command) == 'sell - sell command'


def test_clear_command():
    """
    Ensures that the clear command is generated with
    the proper command_string.
    """
    assert clear.command_string == 'K'


def test_close_command():
    """
    Ensures that the close command is generated with
    the proper command_string.
    """
    assert close.command_string == '1T'


def test_sell_command():
    """
    Ensures that the sell command is generated with
    the proper command_string.
    """
    description = 'Potatoes'
    amount = '2.0'
    quantity = '*1.0'
    expected = '"Potatoes"2.0*1.0H1R'
    generated = sell.command_string.format(
        description=description,
        amount=amount,
        quantity=quantity,
    )
    assert generated == expected
