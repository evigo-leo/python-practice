"""Packaging into boxes"""
def pack_boxes(items: list[int], limit: int) -> list[list[int]]:
    """
    Упаковывает предметы в коробки, не превышая лимит веса.
    Предметы упаковываются в порядке следования.
    Предметы, превышающие лимит, исключаются из результата.
    
    Алгоритм:
    1. Фильтруем предметы, исключая те, что превышают лимит
    2. Инициализируем пустой список для коробок
    3. Для каждого предмета:
       - Если текущая коробка пуста или добавление предмета не превысит лимит,
         добавляем предмет в текущую коробку
       - Иначе, создаем новую коробку и добавляем туда предмет
    4. Возвращаем список коробок
    
    :param items: Список весов предметов
    :param limit: Максимальный вес коробки
    :return: Список коробок (список списков)
    """
    if not items or not limit:
        return []

    sorted_items, box = [], []
    for i in items:
        if i <= limit and sum(box) + i <= limit:
            box.append(i)
        elif i > limit:
            continue
        else:
            sorted_items.append(box)
            box = [i]

    if box:
        sorted_items.append(box)
    return sorted_items
