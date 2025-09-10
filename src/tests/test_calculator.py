"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

# TODO: ajoutez les tests
def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(5, 3) == 2

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(4, 3) == 12

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(10, 2) == 5
    assert my_calculator.division(10, 0) == "Erreur : division par zéro"