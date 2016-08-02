from cash_register.commands.sell import clear, close, sell


def test_clear_command():
    """
    Ensures that the clear command is generated with
    the proper command_string.
    """
    assert clear.build() == b'K'


def test_close_command():
    """
    Ensures that the close command is generated with
    the proper command_string.
    """
    assert close.build() == b'1T'


def test_sell_command():
    """
    Ensures that the sell command is generated with
    the proper command_string.
    """
    # params used in the public API
    params = {
        'description': 'Potatoes',
        'price': '2.0',
        'quantity': '*1.0',
    }
    # expected result
    expected = b'"Potatoes"2.0*1.0H1R'
    generated = sell.build(params)
    assert generated == expected
