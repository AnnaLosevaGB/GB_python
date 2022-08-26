class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        sign = '+' if self.imaginary > 0 else '-'
        return f'{self.real} {sign} {abs(self.imaginary)}i'

    def __add__(self, other):
        n_1 = self.real + other.real
        n_2 = self.imaginary + other.imaginary
        return Complex(n_1, n_2)

    def __mul__(self, other):
        n_1 = self.real * other.real - self.imaginary * other.imaginary
        n_2 = self.real * other.imaginary + self.imaginary * other.real
        return Complex(n_1, n_2)


num_1 = Complex(3, 1)
num_2 = Complex(2, -3)
print(num_1 + num_2)
print(num_1 * num_2)
print(num_1)
