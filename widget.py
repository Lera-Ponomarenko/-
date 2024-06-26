from datetime import datetime

import masks


def mask_account_card(string: str) -> str:
    """Функция общей маскировки карты и счета"""
    if "Счет" in string:
        account = string[-20:]
        return string[-20:] + masks.mask_account(account)
    else:
        cardnumber = "".join(string[-16:].split())
        return string[:-16] + masks.mask_card_number(cardnumber)


def get_data(date: str) -> str:
    """Функция преобразования даты"""
    date_it = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    formated_date = date_it.strptime("%d.%m.%Y")
    return formated_date

