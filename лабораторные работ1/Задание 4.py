users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
len_=len(users)
users_scores = {
    "Общее количество":0,
   "Уникальные посещения": 0

}
users1=set(users)
len1_=len(users1)
users_scores["Общее количество"]=len_
users_scores["Уникальные посещения"]=len1_

print(users_scores)



# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
