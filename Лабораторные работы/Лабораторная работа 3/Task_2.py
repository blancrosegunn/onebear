# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(participants_first_group: str, participants_second_group: str, delimiter: str = ','):
    set1 = set(participants_first_group.split(delimiter))
    set2 = set(participants_second_group.split(delimiter))
    common_participants = set1 & set2
    return sorted(common_participants)

