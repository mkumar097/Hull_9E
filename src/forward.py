import math


def forward_contract_payoff(delivery_price: float = None,
                            spot_price: float = None,
                            short: bool = False) -> float:

    if short:
        return delivery_price - spot_price
    else:
        return spot_price - delivery_price


def forward_price(risk_free_rate: float = None,
                  current_price: float = None,
                  time_to_maturity: float = None,
                  known_income: float = 0.0,
                  known_yield: float = 0.0) -> float:

    return (current_price - known_income) * math.exp((risk_free_rate -
                                                      known_yield) *
                                                     time_to_maturity)


def forward_value(delivery_price: float = None,
                  spot_price: float = None,
                  risk_free_rate: float = None,
                  time_to_maturity: float = None,
                  known_income: float = 0.0,
                  known_yield: float = 0.0) -> float:

    x = spot_price * math.exp(-known_yield * time_to_maturity)
    y = delivery_price * math.exp(-risk_free_rate * time_to_maturity)

    return x - known_income - y
