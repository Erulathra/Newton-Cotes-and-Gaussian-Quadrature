import numpy as np

# Legendre polynomials solution (P2, P3, P4, P5)
legendre_polynomials_solutions = [
    [-np.sqrt(1 / 3), np.sqrt(1 / 3)],
    [-np.sqrt(3 / 5), 0, np.sqrt(3 / 5)],
    [-np.sqrt(3 / 7 + (2 / 7) * np.sqrt(6 / 5)), -np.sqrt(3 / 7 - (2 / 7) * np.sqrt(6 / 5)),
     np.sqrt(3 / 7 - (2 / 7) * np.sqrt(6 / 5)), np.sqrt(3 / 7 + (2 / 7) * np.sqrt(6 / 5))],
    [-1 / 3 * np.sqrt(5 + 2 * np.sqrt(10 / 7)), -1 / 3 * np.sqrt(5 - 2 * np.sqrt(10 / 7)), 0,
     1 / 3 * np.sqrt(5 - 2 * np.sqrt(10 / 7)), 1 / 3 * np.sqrt(5 + 2 * np.sqrt(10 / 7))],
    [-0.932469514203152027812,
     -0.661209386466264513661,
     -0.238619186083196908631,
     0.238619186083196908631,
     0.661209386466264513661,
     0.932469514203152027812]
]

gaussian_legendre_weights = [
    [1, 1],
    [5 / 9, 8 / 9, 5 / 9],
    [(18 - np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 - np.sqrt(30)) / 36],
    [(322 - 13 * np.sqrt(70)) / 900, (322 + 13 * np.sqrt(70)) / 900, 128 / 225,
     (322 + 13 * np.sqrt(70)) / 900, (322 - 13 * np.sqrt(70)) / 900],
    [-0.932469514203152027812, -0.661209386466264513661, -0.238619186083196908631,
          0.238619186083196908631, 0.661209386466264513661, 0.932469514203152027812]
]


def gaussian_legendre_quadrature(function, a: float, b: float, node_count: int) -> float:
    if node_count > 6 or node_count < 2:
        raise WrongNodeCountException

    if a > b:
        b, a = a, b

    result = 0

    for i in range(node_count):
        t = ((a + b) / 2) + ((b - a) / 2) * legendre_polynomials_solutions[node_count - 2][i]
        result += ((b - a) / 2) * gaussian_legendre_weights[node_count - 2][i] * function(t)

    return result


class WrongNodeCountException(ValueError):
    pass
