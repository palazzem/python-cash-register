import pytest

from cash_register.exceptions import NotSupportedCommand


def test_not_supported_command_default():
    """
    Test that NotSupportedCommand raises with a default message
    if not provided
    """
    with pytest.raises(NotSupportedCommand) as excinfo:
        raise NotSupportedCommand
    assert str(excinfo.value) == 'Command not supported in this cash register model'


def test_not_supported_command_with_message():
    """
    Test that NotSupportedCommand raises with given message
    if provided
    """
    with pytest.raises(NotSupportedCommand) as excinfo:
        raise NotSupportedCommand('You should not use this command')
    assert str(excinfo.value) == 'You should not use this command'
