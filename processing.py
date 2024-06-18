from typing import Optional, Union


def filter_by_state(inform: list, state='EXECUTED') -> list[str]:
    """Функция, возвращающая список словарей по введенному ключу"""

    new_list = []

    for k in inform:
        if k['state'] == state:
            new_list.append(k)

    return new_list


def sort_by_date(origin_list: list[dict[str, Optional[Union[int, str]]]], ascending=True) -> \
        list[dict[str, Optional[Union[int, str]]]]:
    """Функция принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию"""
    sorted_lists = sorted(origin_list, key=lambda d: d['date'], reverse=ascending)
    return sorted_lists
