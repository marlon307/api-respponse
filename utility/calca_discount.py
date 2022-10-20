def calc_discount(precentage_discount: int, value: int) -> float:
    calc = (float(precentage_discount) / 100) * value
    return value + calc
