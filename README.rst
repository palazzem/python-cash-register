====================
python-cash-register
====================

.. image:: https://badge.fury.io/py/python-cash-register.svg
    :target: https://badge.fury.io/py/python-cash-register

.. image:: https://travis-ci.org/palazzem/python-cash-register.svg?branch=master
    :target: https://travis-ci.org/palazzem/python-cash-register

.. image:: https://codecov.io/gh/palazzem/python-cash-register/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/palazzem/python-cash-register


Python bindings for generic cash registers, using the `XON/XOFF protocol`_ for serial communication.

.. _XON/XOFF protocol: https://en.wikipedia.org/wiki/Software_flow_control

Support
-------

If you need support, please use the `GitHub issue tracker`_.

.. _GitHub issue tracker: https://github.com/palazzem/wagtail-nesting-box/issues

Contributing
------------

We love contributions, so please feel free to fix bugs, improve things, provide documentation.
Just follow the guidelines and submit a PR.

Requirements
------------

* Python 2.7, 3.3, 3.4 and 3.5

Overview
--------

Coming soon.

Getting started
---------------

This example could be outdated and you should not use it until a stable version
of the library is out:

.. code-block:: python

    from serial import Serial
    from cash_register.models.xditron import SaremaX1


    # defines the serial communication
    conn = Serial()
    conn.port = '/dev/ttyUSB0'
    conn.baudrate = 9600
    conn.xonxoff = True
    conn.timeout = 1

    # create a cash register with a serial connection handler
    register = SaremaX1('Shop center', connection=conn)

    # write a list of products
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

    # prepare and send cash register commands
    register.sell_products(products)
    register.send()

Documentation
-------------

Coming soon.

License
-------

``python-cash-register`` is released under the terms of the **BSD license**. Full details in ``LICENSE`` file.
