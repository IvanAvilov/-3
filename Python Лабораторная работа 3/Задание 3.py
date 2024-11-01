def count_letters(str_: str) -> dict and int:
    """Функция для выявления букв и их общего количества"""
    dict_letter_with_count = {}
    correct_str = str_.lower()
    list_letter = []
    for i in correct_str:
        if i.isalpha():
            list_letter.append(i)
    n = len(list_letter)
    for j in list_letter:
        count = list_letter.count(j)
        dict_letter_with_count[j] = count
    return dict_letter_with_count, n


def calculate_frequency(count_letter: dict, n: int) -> dict:
    """Функция для нахождения частоты использования каждой буквы"""
    dict_frequency = {}
    for name, count in count_letter.items():
        frequency = count / n
        dict_frequency[name] = frequency
    return dict_frequency


if __name__ == "__main__":
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
    Свои мне сказки говорил.
    """

    a, b = count_letters(main_str)
    c = calculate_frequency(a, b)
    for key, value in c.items():
        print(f"{key}: {value:.2f}")
