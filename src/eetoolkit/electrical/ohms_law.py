from math import isfinite


def calculate(voltage=None, current=None, resistance=None):
    values = [voltage, current, resistance]

    if sum(v is not None for v in values) != 2:
        raise ValueError("Provide exactly two values.")

    for value in values:
        if value is not None:
            if not isinstance(value, (int, float)):
                raise TypeError("Values must be numeric.")
            if not isfinite(value):
                raise ValueError("Values must be finite.")

    if resistance is not None and resistance <= 0:
        raise ValueError("Resistance must be positive.")

    if voltage is not None and current is not None:
        if current == 0:
            raise ValueError("Current cannot be zero.")
        resistance = voltage / current

    elif voltage is not None and resistance is not None:
        current = voltage / resistance

    else:
        voltage = current * resistance

    if resistance <= 0:
        raise ValueError("Resistance must be positive.")

    power = voltage * current

    return {
        "voltage": voltage,
        "current": current,
        "resistance": resistance,
        "power": power,
  }
