from typing import Iterable


def avg(values: Iterable[float]) -> float:
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1

    if count == 0:
        raise ValueError("空のシーケンスの平均を計算することはできません")

    return total / count


def median(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise ValueError("空のシーケンスの中央値を計算することはできません")

    sorted_values = sorted(values)
    n = len(sorted_values)

    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        mid1 = sorted_values[n // 2 - 1]
        mid2 = sorted_values[n // 2]
        return (mid1 + mid2) / 2
