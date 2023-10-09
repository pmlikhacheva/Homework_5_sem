import math

class ComplexNumber:
    def __init__(self, R, Im):
        self.R = R
        self.Im = Im
    
    def get_R(self):
        return self.R
    
    def set_R(self, R):
        if not isinstance(R, (int, float)):
            raise ValueError("Действительная часть должна быть числом!")
        self.R = R
    
    def get_Im(self):
        return self.Im
    
    def set_Im(self, Im):
        if not isinstance(Im, (int, float)):
            raise ValueError("Мнимая часть должна быть числом!")
        self.Im = Im
        
    def to_exponential_form(self):
        if self.R == 0 and self.Im == 0:
            raise ValueError("Нельзя конвертировать нулевое комплексное число в экспоненциальную форму!")
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
        if denominator == 0:
            raise ZeroDivisionError("Деление на ноль!")
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

def calculator():
    try:
        R1 = float(input("Введите действительную часть первого комплексного числа: "))
        Im1 = float(input("Введите мнимую часть первого комплексного числа: "))
        complex1 = ComplexNumber(R1, Im1)

        R2 = float(input("Введите действительную часть второго комплексного числа: "))
        Im2 = float(input("Введите мнимую часть второго комплексного числа:: "))
        complex2 = ComplexNumber(R2, Im2)

        print("Комплексное число 1:", complex1.to_exponential_form(),' или ', complex1.get_R(), '+ i*', complex1.get_Im())
        print("Комплексное число 2:", complex2.to_exponential_form(),' или ', complex2.get_R(), '+ i*', complex2.get_Im())

        operation = input("Введите оператор (+, -, *, /): ")

        if operation == "+":
            result = complex1 + complex2
            print("Ответ:", result.to_exponential_form(),' или ', result.get_R(), '+ i*', result.get_Im())
        elif operation == "-":
            result = complex1 - complex2
            print("Ответ:", result.to_exponential_form(),' или ', result.get_R(), '+ i*', result.get_Im())
        elif operation == "*":
            result = complex1 * complex2
            print("Ответ:", result.to_exponential_form(), ' или ', result.get_R(), '+ i*', result.get_Im())
        elif operation == "/":
            try:
                result = complex1 / complex2
                print("ReОтветsult:", result.to_exponential_form(),' или ', result.get_R(), '+ i*', result.get_Im())
            except ZeroDivisionError:
                print("Деление на ноль!")
        else:
            print("Неверный оператор!")

    except ValueError as e:
        print("Ошибка:", str(e))


calculator()
