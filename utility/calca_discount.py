def calc_discount(precentage_discount: int, value: int) -> int:
    calc = (float(precentage_discount) / 100) * value
    value = value + calc
    return value
