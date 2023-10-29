
def get_find_common_participants(first_group, second_group, sep):
    participants_list1 = first_group.split(sep)
    participants_list2 = second_group.split(sep)

    common_participants = []

    for i in participants_list1:
        for j in participants_list2:
            if i == j:
                common_participants.append(i)
                break

    return common_participants

# Пример использования функции:
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = get_find_common_participants(participants_first_group, participants_second_group, '|')
print(common_participants)
