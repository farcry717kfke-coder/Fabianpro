"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate) -> float:
    return budget / exchange_rate


def get_change(budget, exchanging_value):
   return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills



def get_number_of_bills(amount= float, denomination= int):
    return amount // denomination


def get_leftover_of_bills(amount= float, denomination= int):
    return amount % denomination
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    final_rate = exchange_rate + (exchange_rate * spread / 100)
    

    exchanged_amount = budget / final_rate

    number_of_bills = int(exchanged_amount // denomination)
    
   
    total_value = number_of_bills * denomination
    
    return total_value
