import pytest


import solution

class TestNumbersExercises:

    # Addition Exercise
    # @pytest.mark.skip
    def test_add_positive_numbers(self):
        assert solution.add(1, 2) == 3

    @pytest.mark.skip
    def test_add_negative_numbers(self):
        assert solution.add(-2, -3) == -5

    # Subtraction Exercise
    @pytest.mark.skip
    def test_subtract_two_numbers(self):
        assert solution.subtract(5, 3) == 2

    # Multiplication Exercise
    @pytest.mark.skip
    def test_multiply_two_numbers(self):
        assert solution.multiply(5, 5) == 25

    # Division Exercise
    @pytest.mark.skip
    def test_divide_two_numbers(self):
        assert solution.divide(25, 5) == 5

    # Modulus Exercise
    @pytest.mark.skip
    def test_remainder_when_zero(self):
        assert solution.remainder(25, 5) == 0

    @pytest.mark.skip
    def test_remainder_when_not_zero(self):
        assert solution.remainder(13, 5) == 3

    # Float Division Exercise
    @pytest.mark.skip
    def test_float_division(self):
        assert solution.float_division(10, 2) == 5.0

    # String to Number Exercise
    @pytest.mark.skip
    def test_string_to_number_positive(self):
        assert solution.string_to_number("1") == 1

    @pytest.mark.skip
    def test_string_to_number_negative(self):
        assert solution.string_to_number("-5") == -5

    # Even Exercise
    @pytest.mark.skip
    def test_is_even_true(self):
        assert solution.is_even(6) is True

    @pytest.mark.skip
    def test_is_even_false(self):
        assert solution.is_even(5) is False

    # Odd Exercise
    @pytest.mark.skip
    def test_is_odd_true(self):
        assert solution.is_odd(9) is True

    @pytest.mark.skip
    def test_is_odd_false(self):
        assert solution.is_odd(6) is False
