list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
index_seredina = int(len(list_players)/2)
index_zamena = index_seredina
step_slice1 = list_players[:index_zamena]
step_slice2 = list_players[index_zamena:]
print(step_slice1)
print(step_slice2)
