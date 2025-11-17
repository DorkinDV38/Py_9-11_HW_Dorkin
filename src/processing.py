from typing import List, Dict, Optional, Union
from datetime import datetime


def filter_by_state(operations_list: List[Dict[str, any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, any]]:
    """ Фильтрует словари операции из списка по заданному состоянию. """

    filtred_operations_list = []
    for operation in operations_list:
        if operation.get("state") == state:
            filtred_operations_list.append(operation)

    return filtred_operations_list


# # Пример использования функции:
# data = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
#
# print("Операции с состоянием EXECUTED:")
# print(filter_by_state(data, 'EXECUTED'))
#
# print("\nОперации с нулевым состоянием:")
# print(filter_by_state(data))
#
# print("\nОперации с состоянием CANCELED:")
# print(filter_by_state(data, 'CANCELED'))




def sort_by_date(operations_list: List[Dict[str, any]], reverse: Optional[bool] = True) -> List[Dict[str, any]]:
    """ Сортирует список словарей операций по дате. """

    sorted_list = sorted(operations_list, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)
    return sorted_list


# Пример использования:
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# sorted_descending = sort_by_date(data)
# print(sorted_descending)
#
# sorted_ascending = sort_by_date(data, reverse=False)
# print(sorted_ascending)


print(filter_by_state(data, 'EXECUTED'))