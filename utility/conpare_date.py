from datetime import datetime


def conpare_date(date_1: str, date_2: str) -> bool:
    datetime.fromisoformat
    if datetime.fromisoformat(
        date_1
    ) >= datetime.now() and datetime.now() <= datetime.fromisoformat(date_2):
        return True
    return False
