import sys

guest_history = open(sys.argv[1])
"""Imagine there is a jazz club with robot waiters.
   1) Guests should order music by typing composer names or id numbers (print int/string)
   2) Guests may save their favorite composer names or ids using arbitrary names
   3) The bill is calculated based on predefined prices of orders by composer names (sum up by var names)
   Example:
   _______________________________________________________________________________
   favorite1=Hamasyan   # store a composer name
   favorite2=23         # store a composer id
   Hamasyan=1000        # define price for one piece of music of a composer
   Peterson=555         # define price for one piece of music of a composer
   favorite2            # print/order stored composer name/id
   Chick Corea, please! # print/order any composer name  
   Hamasyan+Peterson    # calculate your bill by ordered composer stored names (sum up)
"""
orders_stored = {}


def store_order(text):
    """ variable assignment: varname=value
    two types are supported: integer and string
    """
    if text.count("=") == 1:
        i = text.index("=")
        try:
            orders_stored[text[:i]] = int(text[i + 1:])
        except:
            orders_stored[text[:i]] = text[i + 1:-1]


def place_order(text):
    """To order music of your favorite composer (print)
    just enter the name or id number of the composer (string, integer)
    """
    if text.find("=") == -1 and text.find("+") == -1:
        if text[:-1] in orders_stored.keys():
            print("Order:", orders_stored[text[:-1]])
        elif text.isdigit():
            print("Order:", int(text))
        elif text != "\n":
            print("Order:", text)


def calc_bill(text):
    """calculate your bill, i.e. sum up the price of each order,
    you should use the price previously stored in our system for each composer"""
    if text.count("+") == 1:
        i = text.index("+")
        num1 = text[:i]
        num2 = text[i + 1:-1]
        if num1 in orders_stored.keys() and num2 in orders_stored.keys():
            try:
                bill = orders_stored[num1] + orders_stored[num2]
                print("Your Bill:", bill)
            except:
                raise ValueError("price is not defined")


# Execute the program
for guest in guest_history:
    store_order(guest)
    place_order(guest)
    calc_bill(guest)
