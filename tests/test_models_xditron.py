from cash_register.models.xditron import SaremaX1
from cash_register.commands import sell as C


class TestSaremaX1:
    """
    Tests for the Sarema X1 model
    """
    def test_initialization(self):
        """
        Ensure that the supported commands are properly set
        """
        # create the register
        register = SaremaX1('Sarema X1')
        # check supported commands
        assert C.clear in register._supported_commands
        assert C.close in register._supported_commands
        assert C.sell in register._supported_commands

    def test_sell_products(self):
        """
        Ensure that given products are correctly added to
        the internal commands list
        """
        # create the register
        register = SaremaX1('Sarema X1')
        # define a products list
        products = [
            {
                'description': 'Potatoes',
                'amount': '2.0',
                'quantity': '3.0',
            },
            {
                'description': 'Water',
                'amount': '0.50',
            },
        ]
        # create a list of commands
        register.sell_products(products)
        assert len(register._commands) == 4
        assert register._commands[0] == 'K'
        assert register._commands[1] == '"Potatoes"2.0*3.0H1R'
        assert register._commands[2] == '"Water"0.50H1R'
        assert register._commands[3] == '1T'
