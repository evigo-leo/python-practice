"""Get weapons with max price"""
def find_most_expensive_weapons(
        inventory: dict[str, int], blueprints: dict[str, dict]
        ) -> list[str]:
    """
    Находит все оружия, которые можно изготовить из данного инвентаря,
    и которые имеют максимальную стоимость среди возможных.

    :param inventory: Словарь материалов и их количества (например, {"wood": 5, "metal": 3}).
    :param blueprints: Словарь чертежей оружия (например, 
                        {"sword": {"materials": {"wood": 2}, "price": 10}}).
    :return: Список названий оружий с максимальной ценой, которые можно создать.
    """
    max_price = 0
    weapons_prices = {}
    flag = False

    # Проходимся по всем видам оружия
    for weapon in blueprints:
        materials = blueprints.get(weapon)["materials"] # материалы для конкретного оружия
        price = blueprints.get(weapon)["price"]         # цена конкретного оружия
        # Проходимся по материалам для конкретного оружия и сравниваем с инвентарными запасами
        for mat in materials:
            # Если материалов не хватает или они отсутствуют, переходим к другому оружию
            if materials[mat] > inventory.get(mat, 0):
                flag = True
                break
        if not flag and max_price <= price:
            max_price = price
            weapons_prices.setdefault(max_price, []).append(weapon)

    return weapons_prices.get(max_price, [])
