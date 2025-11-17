from typing import List, Dict, Optional

def filter_by_state(operations_list: List[Dict[str, any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, any]]:
    """  Фильтрует словари операции по заданному состоянию.  """

    filtred_operations_list = []
    for operation in operations_list:
        if operation.get("state") == state:
            filtred_operations_list.append(operation)

    return filtred_operations_list


# Пример использования функции:
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

print("Операции с состоянием EXECUTED:")
print(filter_by_state(data, 'EXECUTED'))

print("\nОперации с нулевым состоянием:")
print(filter_by_state(data))

print("\nОперации с состоянием CANCELED:")
print(filter_by_state(data, 'CANCELED'))