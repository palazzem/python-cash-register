from cash_register.commands.base import Command


def test_base_command_init():
    """
    The base Command should create a proper instance. The
    test creates a new fake command and checks the instance
    attributes and __str__ informal representation.
    """
    command = Command('sell', 'sell command', '5.90H1R1')
    # instance attributes
    assert command.name == 'sell'
    assert command.description == 'sell command'
    assert command._command_string == '5.90H1R1'
    # string informal representation
    assert str(command) == 'sell - sell command'


def test_base_command_build():
    """
    The base Command should provide a public API that
    can be used to generate a valid cash register command.
    """
    # example sell command
    command = Command(
        'SELL',
        'Add a record to the current recipe',
        '"{description}"{price}{quantity}H1R',
    )
    # params used in the public API
    params = {
        'description': 'Potatoes',
        'price': '2.0',
        'quantity': '*1.0',
    }
    # expected result
    expected = b'"Potatoes"2.0*1.0H1R'
    generated = command.build(params)
    assert generated == expected
