"""
The function for finding twin pairs
"""
import math


def find_twin_pairs(X, threshold):
    """
    Находит все пары объектов, у которых евклидово расстояние меньше threshold.
    
    Аргументы:
    X -- двумерный список чисел (n x m)
    threshold -- пороговое значение расстояния
    
    Возвращает:
    Список кортежей (i, j, distance), где i < j и distance < threshold
    """
    result = []
    for i, vi  in enumerate(X):
        for j, vj in enumerate(X):
            if i != j and i < j:
                distance = math.dist(vi, vj)
                if distance <= threshold:
                    result.append((i, j, distance))
    return result

# X = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [1, 2, 3],
#     [7, 8, 9]
# ]

# print(find_twin_pairs(X, 1.))
