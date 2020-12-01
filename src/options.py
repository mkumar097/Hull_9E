class Options:
    """This is a class structure that computes the different option values
    for a long and short call/put.
    By defining 'current', 'strike' and 'option_price' the class will
    calculate the possible values for all the different options.
    ----------
    current: float
        Current stock price.
    strike: float
        Price at which to either buy or sell the stock.
    option_price: float
        Upfront cost of purchasing the option to either buy or sell a stock.

    >>> generic_stock = Options(1.0, 1.5, 0.5)
    >>> print(generic_stock.long_call)
    >>> print(generic_stock.long_put)
    """

    def __init__(self, current: float = None, strike: float = None,
                 option_price: float = None):

        self._current = current
        self._strike = strike
        self._option_price = option_price

    @property
    def current(self):
        return self._current

    @property
    def strike(self):
        return self._strike

    @property
    def option_price(self):
        return self._option_price

    @property
    def long_call(self) -> float:

        if self._current > self._strike:
            return self._current - self._strike - self._option_price
        else:
            return -self._option_price

    @property
    def long_put(self) -> float:

        if self._strike > self._current:
            return self._strike - self._current - self._option_price
        else:
            return -self._option_price

    @property
    def short_call(self) -> float:

        if self._strike > self._current:
            return self._option_price
        else:
            return self._strike - self._current + self._option_price

    @property
    def short_put(self) -> float:

        if self._strike < self._current:
            return self._option_price
        else:
            return self._current - self._strike + self._option_price
