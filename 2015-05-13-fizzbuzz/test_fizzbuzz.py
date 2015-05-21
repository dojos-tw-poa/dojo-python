import pytest
from fizzbuzz import FizzBuzz


# assert <esperado> == <como chegar ao resultado>

def test_fizzbuzz_returns_1_given_1():
    fizzbuzz = FizzBuzz()
    assert 1 == fizzbuzz.generate_response(1)


def test_fizzbuzz_returns_fizz_given_3():
    fizzbuzz = FizzBuzz()
    assert "Fizz" == fizzbuzz.generate_response(3)


def test_fizzbuzz_returns_buzz_given_5():
    fizzbuzz = FizzBuzz()
    assert "Buzz" == fizzbuzz.generate_response(5)


def test_fizzbuzz_returns_fizzbuzz_given_15():
    fizzbuzz = FizzBuzz()
    assert "FizzBuzz" == fizzbuzz.generate_response(15)
