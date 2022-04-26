import numpy as np
import newton_cotes as nc
import gaussian_legendre as gl


def main():
    # a = 0
    # b = 10
    # print(nc.newton_cotes_quadrature(test_function, a, b, 0.00001))
    # print(gl.gaussian_legendre_quadrature(test_function, a, b, 2))
    # print(gl.gaussian_legendre_quadrature(test_function, a, b, 3))
    # print(gl.gaussian_legendre_quadrature(test_function, a, b, 4))
    # print(gl.gaussian_legendre_quadrature(test_function, a, b, 5))
    chosen_solver = nc.newton_cotes_quadrature
    chosen_function = Example_Functions.log
    logger_enabled = False
    logger_output = ""
    user_input = ""
    precision = 0.00001
    boundaries = [0, 10]
    while user_input != "q":
        try:
            print()
            print("Wybrana funkcja:", function_name(chosen_function))
            print("Wybrana metoda:", solver_name(chosen_solver))
            print(f"Przedział: <{boundaries[0]}, {boundaries[1]})")
            print(f"Dokładność/liczba węzłów: {precision:.8f}")
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
                    boundaries = float(input(f"Podaj przedział, oddzielając liczby spacją [<{boundaries[0]}, {boundaries[1]})]: ").split()) or boundaries
                case '4':
                    precision = float(input(f"Podaj dokładność/węzły [{precision:.8f}]: ").replace(",", ".")) or precision
                case '5':
                    if chosen_solver == gl.gaussian_legendre_quadrature:
                        if not (2 <= precision <= 5):
                            print("Dokładność dla tej metody musi się mieścić w przedziale <2, 5>")
                            input("Wciśnij dowolny klawisz by kontynuować...")
                            continue
                        precision = int(precision)
                    outcome = chosen_solver(chosen_function, boundaries[0], boundaries[1], precision)
                    print("Wynik:", outcome)
                    logger_output += f"Method: {solver_name(chosen_solver)}; \tFunction: {function_name(chosen_function)};"
                    logger_output += f"\tBoundaries: <{boundaries[0]}, {boundaries[1]}); \tPrecision: {precision:.8f}; \tResult: {outcome} \n"
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
    user_choice = input(f"Podaj, czy chcesz metodę: \n\
        \t(1) {solver_name(nc.newton_cotes_quadrature)}\n\
        \t(2) {solver_name(gl.gaussian_legendre_quadrature)}\n> ")
    match user_choice:
        case '1': return nc.newton_cotes_quadrature
        case '2': return gl.gaussian_legendre_quadrature


def choose_function():
    user_choice = input(f"Podaj, czy chcesz funkcję: \n\
        \t(1) {function_name(Example_Functions.log)}\n> ")
    match user_choice:
        case "1":
            return Example_Functions.log

def function_name(func) -> str:
    match func:
        case Example_Functions.log: return "log(x+2) + x^2 * 6"

class Example_Functions:
    def log(x):
        return np.log(x + 2) + x ** 2 - 6
    
def scientific_to_normal(number) -> str:
    return format(number, 'f')

if __name__ == "__main__":
    main()
