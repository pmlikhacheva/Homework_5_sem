import math

class ComplexNumber:
    def __init__(self, R, Im):
        self.R = R
        self.Im = Im
    
    def get_R(self):
        return self.R
    
    def set_R(self, R):
        self.R = R
    
    def get_Im(self):
        return self.Im
    
    def set_Im(self, Im):
        self.Im = Im
        
    def to_exponential_form(self):
        magnitude = math.sqrt(self.R**2 + self.Im**2)
        angle = math.atan2(self.Im, self.R)
        return f"{magnitude} * e^(i * {angle})"
    
    def __add__(self, other):
        R = self.R + other.R
        Im = self.Im + other.Im
        return ComplexNumber(R, Im)
    
    def __sub__(self, other):
        R = self.R - other.R
        Im = self.Im - other.Im
        return ComplexNumber(R, Im)

    def __mul__(self, other):
        R = self.R * other.R - self.Im * other.Im
        Im = self.R * other.Im + self.Im * other.R
        return ComplexNumber(R, Im)
    
    def __truediv__(self, other):
        denominator = other.R**2 + other.Im**2
        R = (self.R * other.R + self.Im * other.Im) / denominator
        Im = (self.Im * other.R - self.R * other.Im) / denominator
        return ComplexNumber(R, Im)


# Создание комплексных чисел
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)

# Получение и изменение действительной части
# print(c1.get_R())  # 2
# c1.set_R(6)
# print(c1.get_R())  # 6

# Получение и изменение мнимой части
# print(c1.get_Im())  # 3
# c1.set_Im(7)
# print(c1.get_Im())  # 7

# Представление числа в экспоненциальной форме
print(c1.to_exponential_form())  # 3.605551275463989 * e^(i * 0.982793723247329)

# Сложение двух комплексных чисел
c3 = c1 + c2
print(c3.get_R())  # 6
print(c3.get_Im())  # 8

# Вычитание двух комплексных чисел
c4 = c1 - c2
print(c4.get_R())  # -2
print(c4.get_Im())  # -2

# Умножение двух комплексных чисел
c5 = c1 * c2
print(c5.get_R())  # -7
print(c5.get_Im())  # 22

# Деление двух комплексных чисел
c6 = c1 / c2
print(c6.get_R())  # 0.5609756097560976
print(c6.get_Im())  # 0.04878048780487805
