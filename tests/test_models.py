import pytest

from cash_register.exceptions import NotSupportedCommand
from cash_register.models.base import CashRegister
from cash_register.commands.base import Command


def test_base_model_defaults():
    """
    Test a new CashRegister instance
    """
    register = CashRegister('Sarema X2')
    assert register.name == 'Sarema X2'
    assert register._supported_commands == []
    assert register._commands == []
    assert register._connection == None


def test_base_model_connection(mocker):
    """
    Ensure that a connection handler can be added after
    the instance initialization
    """
    register = CashRegister('Sarema X2')
    # create a fake connection object
    connection = object()
    # add the connection handler
    register.connect(connection)
    assert register._connection == connection


def test_base_model_supported_commands():
    """
    Ensure that if a CashRegister has defined some supported commands,
    the get_supported_commands() returns a list of commands.
    """
    # create an instance ad override supported commands
    register = CashRegister('Sarema X2')
    register._supported_commands = [object()]
    commands = register.get_supported_commands()
    assert register._supported_commands == commands


def test_base_model_supported_commands():
    """
    Ensure that if a CashRegister has defined some supported commands,
    the get_supported_commands() returns a new list that doesn't
    change the original instance's list.
    """
    # create an instance ad override supported commands
    register = CashRegister('Sarema X2')
    register._supported_commands = [object()]
    commands = register.get_supported_commands()
    # update supported commands list
    commands.append(object())
    # the instance list is not updated
    assert register._supported_commands != commands


def test_base_model_str():
    """
    Test the informal representation of the CashRegister
    """
    register = CashRegister('Sarema X2')
    assert str(register) == 'Sarema X2'


def test_base_model_send_empty_commands(mocker):
    """
    Test that no connection is opened if the commands list
    is empty
    """
    # create a CashRegister with a mocked connection
    mocked_serial = mocker.Mock()
    register = CashRegister('Sarema X2', connection=mocked_serial)
    # send commands
    register.send()
    assert register._connection.open.call_count == 0
    assert register._connection.write.call_count == 0
    assert register._connection.flush.call_count == 0
    assert register._connection.close.call_count == 0


def test_base_model_send_commands(mocker):
    """
    Test that a connection is opened and that all commands
    are sent through the connection object
    """
    # create a CashRegister with a mocked connection
    mocked_serial = mocker.Mock()
    register = CashRegister('Sarema X2', connection=mocked_serial)
    # add some commands
    register._commands = ['K', '1H1R', '1T']
    # send commands
    register.send()
    assert register._connection.open.call_count == 1
    assert register._connection.write.call_count == 3
    assert register._connection.flush.call_count == 1
    assert register._connection.close.call_count == 1


def test_base_model_send_commands_flush_list(mocker):
    """
    Ensure that after a send() call, the commands list is empty
    """
    # create a CashRegister with a mocked connection
    mocked_serial = mocker.Mock()
    register = CashRegister('Sarema X2', connection=mocked_serial)
    # add some commands
    register._commands = ['K', '1H1R', '1T']
    # send commands
    register.send()
    assert len(register._commands) == 0


def test_base_model_sell_products():
    """
    The sell_products method must be implemented in the child
    class and not in the CashRegister class.
    """
    with pytest.raises(NotImplementedError):
        register = CashRegister('Sarema X2')
        products = [object()]
        register.sell_products(products)

def test_base_model_add_commands_not_supported():
    """
    Ensure that a command can be added only if it's supported
    by the given model. If the command is not supported, the
    call must raise a NotSupportedCommand exception
    """
    # creates a cash register and appends an example command
    register = CashRegister('Sarema X2')
    command = Command('SELL', 'Sell command', '5.90H1R1')
    # try to use the command
    with pytest.raises(NotSupportedCommand):
        register._add_command(command)

def test_base_model_add_commands():
    """
    Ensure that a command can be added only if it's supported
    by the given model. If the command is supported, the
    call must add the formatted command to the _commands
    attribute
    """
    # creates a cash register and appends an example command
    register = CashRegister('Sarema X2')
    command = Command('SELL', 'Sell command', '5.90H1R1')
    register._supported_commands.append(command)
    # try to use the command
    register._add_command(command)
    assert b'5.90H1R1' in register._commands

def test_base_model_add_commands_with_params():
    """
    Ensure that a command can be added only if it's supported
    by the given model. If the command is supported, the
    call must add the formatted command with the given params,
    to the _commands attribute
    """
    # creates a cash register and appends an example command
    register = CashRegister('Sarema X2')
    command = Command('SELL', 'Sell command', '"{description}"5.90H1R1')
    register._supported_commands.append(command)
    # try to use the command
    params = {
        'description': 'Potatoes'
    }
    register._add_command(command, params)
    assert b'"Potatoes"5.90H1R1' in register._commands
