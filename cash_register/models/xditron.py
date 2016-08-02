from .base import CashRegister

from ..commands import sell as C


class SaremaX1(CashRegister):
    """
    CashRegister implementation for the SaremaX1 model
    """
    def __init__(self, name, connection=None):
        # initializes the CashRegister instance
        super(SaremaX1, self).__init__(name, connection)
        # defines the supported commands
        self._supported_commands = [
            C.clear,
            C.close,
            C.sell,
        ]

    def sell_products(self, products):
        """
        Expects a list of products and creates the proper commands
        into the instance _commands list. Each run of this method
        creates a different recipe and it's not possible to add
        the list of products later.

        Note that the products order matters, and the recipe is
        printed according to this order.

        Accepted products must have the following schema:
            {
                'description': '',  # mandatory, (string)
                'price': '',        # mandatory, (string)
                'quantity': '',     # optional, (string)
            }
        """
        if len(products) > 0:
            # start the transaction
            self._add_command(C.clear)
            # iterate over products
            for product in products:
                params = {
                    'description': product['description'],
                    'price': product['price'],
                }

                quantity = product.get('quantity', '')

                # FIXME: workaround that prepends a *
                # this should be handled in a better way otherwise
                # we risk to make commands too specific and not reausable
                # between different model (maybe we want that?)
                if quantity:
                    quantity = '*{}'.format(quantity)

                params.update({'quantity': quantity})
                self._add_command(C.sell, params)
            # end the transaction
            self._add_command(C.close)
