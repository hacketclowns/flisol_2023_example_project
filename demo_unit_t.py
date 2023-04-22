import unittest


def simple_sum(first_value, second_value):
    # Requirements:
    # 1. Not accept negative inputs.
    # 2. accept only int numbers, not float.
    total = first_value + second_value
    return total


def multiple_sum(first_value, second_value, *args):
    # Requirements:
    # 1. Accept negative inputs.
    # 2. accept only int numbers, not float.
    total = first_value + second_value
    if len(args):
        total = total + sum(args)
    return total


class SumFunctionsTests(unittest.TestCase):
    def test_simple_sum(self):
        pass

    def test_simple_sum__with_float_numbers(self):
        pass

    def test_simple_sum__with_negative_numbers(self):
        pass

    # Test cases for `multiple_sum` function.
    def test_multiple_sum(self):
        pass

    def test_multiple_sum__with_negative_inputs(self):
        pass

    def test_multiple_sum__with_float_numbers(self):
        pass

    def test_multiple_sum__missing_case(self):
        pass


if __name__ == "__main__":
    unittest.main()
