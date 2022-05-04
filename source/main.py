import math
import os
from math import cos, log, sin
from time import process_time_ns

import gaussian_legendre as gl
import newton_cotes as nc


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    chosen_solver = nc.newton_cotes_quadrature
    chosen_function = Example_Functions.with_log
    logger_enabled = False
    logger_output = ""
    user_input = ""
    precision = 0.00001
    boundaries = [0, 10]
    while user_input != "q":
        try:
            cls()
            print()
            if logger_enabled:
                print("[ Logger Enabled ]\n")
            print("Wybrana funkcja:", function_name(chosen_function))
            print("Wybrana metoda:", solver_name(chosen_solver))
            print(f"Przedział: <{boundaries[0]}, {boundaries[1]})")
            print(f"Dokładność/liczba węzłów: {precision:.8f}")
            print()
            user_input = input('''Podaj, czy chcesz:
            (1) Wybrać funkcję
            (2) wybrać metodę całkowania
            (3) Podać przedział
            (4) Podać dokładność
            (5) Obliczyć całkę
            [l - włącz/wyłącz logger]
            [q - wyjście]\n> ''')
            match user_input:
                case '1':
                    chosen_function = choose_function() or chosen_function
                case '2':
                    chosen_solver = choose_solver() or chosen_solver
                case '3':
                    boundaries = input(
                        f"Podaj przedział, oddzielając liczby spacją [<{boundaries[0]}, {boundaries[1]})]: ").split() or boundaries
                    boundaries = [float(number) for number in boundaries]
                case '4':
                    precision = float(
                        input(f"Podaj dokładność/węzły [{precision:.8f}]: ").replace(",", ".")) or precision
                case '5':
                    if chosen_solver == gl.gaussian_legendre_quadrature:
                        if not (2 <= precision <= 5):
                            print("Dokładność dla tej metody musi się mieścić w przedziale <2, 5>")
                            input("Wciśnij dowolny klawisz by kontynuować...")
                            continue
                        precision = int(precision)
                    duration_start = process_time_ns()
                    outcome = chosen_solver(chosen_function, boundaries[0], boundaries[1], precision)
                    duration_end = process_time_ns()
                    print("Wynik:", outcome)
                    if logger_enabled:
                        time_difference = duration_end - duration_start
                        logger_output += f"Method: {solver_name(chosen_solver)};\t\tFunction: {function_name(chosen_function)};"
                        logger_output += f"\tBoundaries: <{boundaries[0]}, {boundaries[1]}); \tPrecision: {precision:.8f}; \tResult: {outcome};"
                        logger_output += f"\tDuration: {(time_difference)}\n"
                    input("Wciśnij dowolny klawisz by kontynuować...")
                case 'l':
                    logger_enabled = not logger_enabled
                case 'q':
                    if logger_enabled: print(logger_output)
                    break
                case _:
                    continue

        except ValueError:
            print("Podczas przetwarzania wystąpił błąd. Sprawdź poprawność wprowadzanych danych.")


def solver_name(solver) -> str:
    match solver:
        case nc.newton_cotes_quadrature:
            return "złożona kwadratura Newtona-Cotesa"
        case gl.gaussian_legendre_quadrature:
            return "wielomiany Legendre'a"


def choose_solver():
    solvers = [nc.newton_cotes_quadrature, gl.gaussian_legendre_quadrature]
    user_choice = input(f"Podaj, czy chcesz metodę: \n\
        \t(1) {solver_name(solvers[0])}\n\
        \t(2) {solver_name(solvers[1])}\n> ")
    if user_choice != '':
        return solvers[int(user_choice) - 1]


def choose_function():
    functions = [Example_Functions.with_square, Example_Functions.with_log, Example_Functions.with_sinus,
                 Example_Functions.with_sinus_complex]
    user_choice = input(f"Podaj, czy chcesz funkcję: \n\
        (1) {function_name(functions[0])}\n\
        (2) {function_name(functions[1])}\n\
        (3) {function_name(functions[2])}\n\
        (4) {function_name(functions[3])}\n> ")
    if user_choice != '':
        return functions[int(user_choice) - 1]


def function_name(func) -> str:
    match func:
        case Example_Functions.with_square:
            return "x^2 + 5x + 8"
        case Example_Functions.with_log:
            return "log(x+2) + x^2 - 6"
        case Example_Functions.with_sinus:
            return "4x + cos(x)"
        case Example_Functions.with_sinus_complex:
            return "sin(1/x) + 1"


class Example_Functions:
    with_square = lambda x: x ** 2 + 5 * x + 8;
    with_log = lambda x: log(x + 2) + x ** 2 - 6
    with_sinus = lambda x: 4 * x + cos(x)
    with_sinus_complex = lambda x: (1/math.sqrt(1 - x * x))


if __name__ == "__main__":
    main()
