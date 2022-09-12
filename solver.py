from math import sqrt, isnan, isinf


def solve(a: float, b: float, c: float, e: float = 1e-5) -> list[float]:
    for arg in (a, b, c, e):
        if isnan(arg) or isinf(arg):
            raise TypeError("Params cannot be NaN or ±Inf")

    D = b ** 2 - 4 * a * c

    if abs(a) < e:
        raise ValueError("'a' equals to zero")

    if abs(D) < e:
        return [
            -b / 2 * a,
            -b / 2 * a
        ]

    if D < 0:
        return []

    if D > 0:
        return [
            (-b + sqrt(D)) / 2 * a,
            (-b - sqrt(D)) / 2 * a,
        ]
