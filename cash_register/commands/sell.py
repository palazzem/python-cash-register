"""
Module that groups all commands related to sales.
"""
from .base import Command


clear = Command(
    'CLEAR',
    'Clear the current action handled by the cash register',
    'K',
)

sell = Command(
    'SELL',
    'Add a record to the current recipe',
    '"{description}"{price}{quantity}H1R',
)

close = Command(
    'CLOSE',
    'Close the current recipe',
    '1T',
)
