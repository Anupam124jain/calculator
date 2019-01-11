import calculator

class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.sub(4, 2)

    def test_multiply(self):
        assert 100 == calculator.mul(10, 10)

    def test_devide(self):
        assert 2 == calculator.div(4, 2)

if __name__ == '__main__':
    TestCalculator()
