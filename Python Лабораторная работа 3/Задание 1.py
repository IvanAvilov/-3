def find_index_item(item_list: list, must_item: str) -> int or None:
    """Функция для нахождения индекса первого вхождения товара в списке"""
    if must_item not in item_list:
        return None
    else:
        number_ = item_list.index(must_item)
        return number_


if __name__ == "__main__":
    items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
    for find_item in ['банан', 'груша', 'персик']:
        index_item = find_index_item(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
        if index_item is not None:
            print(f"Первое вхождение товара '{find_item:}' имеет индекс {index_item}.")
        else:
            print(f"Товар '{find_item}' не найден в списке.")
