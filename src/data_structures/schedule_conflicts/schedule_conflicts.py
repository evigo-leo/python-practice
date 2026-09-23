"""Interval conflicts"""
from datetime import datetime

def find_schedule_conflicts(intervals):
    """
    Находит все конфликтующие пары интервалов времени, включая интервалы через полночь.
    
    Аргументы:
        intervals: список кортежей вида [("HH:MM", "HH:MM"), ...]
        
    Возвращает:
        Список кортежей конфликтующих пар интервалов [(interval1, interval2), ...]
    """
    def to_datetime(time: str, mask="%H:%M"):
        """Convert time string to datetime"""
        return datetime.strptime(time, mask)

    if not intervals:
        return []
    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    interval_conflicts = []
    for n, int_1 in enumerate(intervals_sorted, 1):
        for int_2 in intervals_sorted[n:]:
            if to_datetime(int_1[1]) > to_datetime(int_2[0]):
                interval_conflicts.append((int_1, int_2))
    return interval_conflicts
