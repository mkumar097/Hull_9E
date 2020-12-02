import math


class Forwards:

    def __init__(self, delivery_price: float = None, spot_price: float = None,
                 short: bool = False, risk_free_rate: float = None,
                 current_price: float = None, time_to_maturity: float = None,
                 known_income: float = 0.0, known_yield: float = None):

        self._delivery_price = delivery_price
        self._spot_price = spot_price
        self._short = short
        self._risk_free_rate = risk_free_rate
        self._current_price = current_price
        self._time_to_maturity = time_to_maturity
        self._known_income = known_income
        self._known_yield = known_yield

    @property
    def delivery_price(self):
        return self._delivery_price

    @property
    def spot_price(self):
        return self._spot_price

    @property
    def short(self):
        return self._short

    @property
    def risk_free_rate(self):
        return self._risk_free_rate

    @property
    def current_price(self):
        return self._current_price

    @property
    def time_to_maturity(self):
        return self._time_to_maturity

    @property
    def known_income(self):
        return self._known_income

    @property
    def known_yield(self):
        return self._known_yield

    @property
    def forward_contract_payoff(self) -> float:
        if self._short:
            return self._delivery_price - self._spot_price
        else:
            return self._spot_price - self._delivery_price

    @property
    def forward_price(self) -> float:

        return (self._current_price - self._known_income) * \
               math.exp((self._risk_free_rate - self._known_yield) *
                        self._time_to_maturity)

    @property
    def forward_value(self) -> float:

        x = self._spot_price * math.exp(-self._known_yield *
                                        self._time_to_maturity)
        y = self._delivery_price * math.exp(-self._risk_free_rate *
                                            self._time_to_maturity)

        return x - self._known_income - y
