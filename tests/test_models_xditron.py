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
                'price': '2.0',
                'quantity': '3.0',
            },
            {
                'description': 'Water',
                'price': '0.50',
            },
        ]
        # create a list of commands
        register.sell_products(products)
        assert len(register._commands) == 4
        assert register._commands[0] == b'K'
        assert register._commands[1] == b'"Potatoes"2.0*3.0H1R'
        assert register._commands[2] == b'"Water"0.50H1R'
        assert register._commands[3] == b'1T'

    def test_sell_products_empty(self):
        """
        Ensure that the commands list is not modified if the
        products list is empty
        """
        # create the register
        register = SaremaX1('Sarema X1')
        # define a products list
        products = []
        # create a list of commands
        register.sell_products(products)
        assert len(register._commands) == 0

    def test_sell_products_multiple(self):
        """
        Ensure that two executions of sell_products generates two
        different recipes
        """
        # create the register
        register = SaremaX1('Sarema X1')
        # define a products list
        products_1 = [
            {
                'description': 'Potatoes',
                'price': '2.0',
                'quantity': '3.0',
            },
        ]
        products_2 = [
            {
                'description': 'Water',
                'price': '0.50',
            },
        ]
        # create a list of commands
        register.sell_products(products_1)
        register.sell_products(products_2)
        assert len(register._commands) == 6
        assert register._commands[0] == b'K'
        assert register._commands[1] == b'"Potatoes"2.0*3.0H1R'
        assert register._commands[2] == b'1T'
        assert register._commands[3] == b'K'
        assert register._commands[4] == b'"Water"0.50H1R'
        assert register._commands[5] == b'1T'
