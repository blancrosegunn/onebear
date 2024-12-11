# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def find_first_index(items_list, find_item):
    try:
        return items_list.index(find_item)
    except ValueError:
        return None
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
