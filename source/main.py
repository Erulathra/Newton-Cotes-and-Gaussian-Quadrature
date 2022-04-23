import numpy as np
import newton_cotes as nc


def test_function(x):
    return 2 * np.sin(x)


def main():
    print(nc.newton_cotes_quadrature(test_function, -3.5, 3, 0.00001))


if __name__ == "__main__":
    main()
