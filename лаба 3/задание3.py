# TODO  Напишите функцию count_letters
def get_count_letters(main_str):
    letter_counts = {}  # Используйте letter_counts вместо letter_count
    main_str = main_str.lower()
    for i in main_str:
        if i.isalpha():
            if i in letter_counts:
                letter_counts[i] += 1
            else:
                letter_counts[i] = 1

    return letter_counts


def calculate_frequency(letter_counts):
    total_letters = sum(letter_counts.values())
    letter_frequencies = {}

    for letter, count in letter_counts.items():
        frequency = count / total_letters
        letter_frequencies[letter] = frequency

    return letter_frequencies

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говори
"""

letter_counts = get_count_letters(main_str)  # Используйте get_count_letters вместо count_letters
frequencies = calculate_frequency(letter_counts)

for letter, frequency in frequencies.items():
    print(f"{letter}: {frequency:.2f}")






