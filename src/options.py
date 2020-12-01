
class Options:

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
