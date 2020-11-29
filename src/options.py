def long_call(current: float = None,
              strike: float = None,
              option_price: float = None) -> float:

    if current > strike:
        return current - strike - option_price
    else:
        return -option_price


def long_put(current: float = None,
             strike: float = None,
             option_price: float = None) -> float:

    if strike > current:
        return strike - current - option_price
    else:
        return -option_price


def short_call(current: float = None,
               strike: float = None,
               option_price: float = None) -> float:

    if strike > current:
        return option_price
    else:
        return strike - current + option_price


def short_put(current: float = None,
              strike: float = None,
              option_price: float = None) -> float:

    if strike < current:
        return option_price
    else:
        return current - strike + option_price
