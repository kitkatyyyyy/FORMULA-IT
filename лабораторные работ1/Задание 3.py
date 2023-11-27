# TODO Найдите количество книг, которое можно разместить на дискете
value_simbol_in_strok = 25*4
value_strok_in_page = value_simbol_in_strok*50
value_page_in_book = value_strok_in_page*100
mb1 = 1024*1024
all_value = (1.44*mb1)/value_page_in_book
book = round(all_value)

print("Количество книг, помещающихся на дискету:",book)
