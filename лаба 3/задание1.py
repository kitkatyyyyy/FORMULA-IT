# TODO Напишите функцию для поиска индекса товара

def get_find_item(items_list, bon_list):
    for find_item in bon_list:
        if find_item in items_list:
            index_item = items_list.index(find_item)
            print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
        else:
            print(f"Товар '{find_item}' не найден в списке.")

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
bon_list = ['банан', 'груша', 'персик']



get_find_item(items_list, bon_list)
