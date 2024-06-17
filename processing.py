from typing import Optional, Union


def filter_by_state(list_of_data: list[dict[str, str | int]], condition: str = 'EXECUTED') -> (
        list)[dict[str, str | int]]:
    """Функция принимает список словарей и возвращает новый список словарей,
    у которых ключ содержит переданное в функцию значение"""
    filtered_list = []
    for data in list_of_data:
        if data.get("state") == condition:
            filtered_list.append(data)
    return filtered_list


print(
    filter_by_state(
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ])
)


def sort_by_date(origin_list: list[dict[str, Optional[Union[int, str]]]], reverse_list: bool = True) -> \
        list[dict[str, Optional[Union[int, str]]]]:
    """Функция принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию"""
    sorted_lists = sorted(origin_list, key=lambda d: d['date'], reverse=reverse_list)
    return sorted_lists
