"""Sort segments"""
def sort_segments(segments: list[tuple[int]]) -> list[tuple[int]]:
    """
    Сортирует отрезки по убыванию длины с использованием словаря,
    где ключи - длины, значения - списки отрезков
    
    Args:
        segments: список кортежей (start, end), представляющих отрезки
        
    Returns:
        список отрезков, отсортированных по убыванию длины
    """
    segments_dict = {}
    for s in segments:
        length = s[1] - s[0]
        segments_dict.setdefault(length, []).append(s)

    keys = list(segments_dict.keys())
    n = len(keys)

    # Сортировка пузырьком
    for i in range(n):
        for j in range(n - i - 1):
            if keys[j] < keys[j + 1]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    segments_sorted = []
    for key in keys:
        segments_sorted += segments_dict[key]

    return segments_sorted


# альтернативный простой вариант
def sort_segments_simple(segments: list[tuple[int]]) -> list[tuple[int]]:
    """Простая сортировка с использованием sorted()"""
    segments_dict = {}
    for s in segments:
        length = s[1] - s[0]
        segments_dict.setdefault(length, []).append(s)

    segments_keys_sorted = sorted(segments_dict, reverse=True)
    segments_sorted = []
    for key in segments_keys_sorted:
        segments_sorted += segments_dict[key]
    return segments_sorted
