from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 20
        b = 10
        cal = Calculator()

        # act
        result = cal.subtract(a,b)

        # assert 
        expected = 10
        assert result == expected

    def test_multiply(self):
        # arrange 
        a = 100
        b = 5
        cal = Calculator()

        # act
        result = cal.multiply(a,b)

        # assert
        expected = 500
        assert result == expected

    def test_divide(self):
        # arrange
        a = 100
        b = 5
        cal = Calculator()

        # act
        result = cal.divide(a,b)

        # assert 
        expected = 20
        assert result == expected


    def test_divide_zero(self):
        # arrange
        a = 100
        b = 0
        cal = Calculator()

        # act and assert using pytest.raises to catch the ZeroDivisionError
        with pytest.raises(ZeroDivisionError, match="Division by zero error"):
            cal.divide(a, b)
