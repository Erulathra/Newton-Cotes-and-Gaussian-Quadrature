import numpy as np
import newton_cotes as nc
import gaussian_legendre as gl


def test_function(x):
    return np.log(x + 2) + x ** 2 - 6


def main():
    a = 0
    b = 10
    print(nc.newton_cotes_quadrature(test_function, a, b, 0.00001))
    print(gl.gaussian_legendre_quadrature(test_function, a, b, 2))
    print(gl.gaussian_legendre_quadrature(test_function, a, b, 3))
    print(gl.gaussian_legendre_quadrature(test_function, a, b, 4))
    print(gl.gaussian_legendre_quadrature(test_function, a, b, 5))


if __name__ == "__main__":
    main()
