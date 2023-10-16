## Контрольные вопросы:
- Как можно описать взаимоотношения __родительского__ и __дочернего__ классов?
  
Взаимоотношения родительского и дочернего классов можно описать как отношение предок-потомок, где дочерний класс наследует атрибуты и методы родительского класса. Дочерний класс может расширить функциональность родительского класса, добавляя свои собственные атрибуты и методы.
Также отношение наследования можно описать логически с точки зрения принципа подстановки Лисков:
> "Пусть q(x) является свойством, верным относительно объектов x некоторого типа T. Тогда q(y) также должно быть верным для объектов y типа S, где S является подтипом типа T."

Т.е. наследующий класс должен дополнять, а не замещать поведение базового класса.
С точки зрения программирования, потомок расширяет предка, но с точки зрения логики потомок должен уточнять предка, являться его представителем.

- В чем плюсы и минусы использования __наследования__?

Плюсы:

  - Повторное использование кода: можно использовать уже существующий код в родительском классе в дочерних классах.
  - Упрощение кода: наследование позволяет создавать иерархию классов, что делает код более организованным и понятным.
  - Расширяемость: можно легко добавлять новые функции и свойства в дочерние классы, не затрагивая родительский класс.
  - Логическая связность: классы связаны в четкую иерархическую структуру.

Минусы:
  - Создание жесткой связи между классами: изменение родительского класса может повлиять на все дочерние классы.
  - Усложнение структуры программы: слишком глубокая иерархия наследования может сделать код сложным для понимания.
  - Иногда родительские классы никак не используются в программе. Это необязательно плохо, но хотелось бы сократить такие моменты.

- Как __наследование__ сочетается с __инкапсуляцией__ данных?

Наследование сочетается с инкапсуляцией данных, так как дочерний класс может наследовать приватные свойства и методы родительского класса. Однако, доступ к этим приватным элементам может быть ограничен в дочернем классе.

- Для чего используется ключевое слово `super()`?

Ключевое слово super() используется в Python для вызова методов родительского класса. 

- Какую роль играет порядок классов __предков__ при __множественном наследовании__?

Если два или более класса имеют общего потомка, то порядок наследования определяет, какие методы будут вызываться при обращении к ним из дочернего класса. Порядок наследования можно указать при определении класса с помощью списка базовых классов в круглых скобках.

- Зачем нужна __обработка исключений__? В каких случаях ее использование некорректно?

Обработка исключений используется для обработки ошибок и случаев, которые могут возникнуть во время выполнения программы. Она позволяет предусмотреть альтернативный сценарий выполнения программы при возникновении ошибки, чтобы избежать аварийного завершения программы.

- Зачем в блоке `try` использовать раздел `finally`?

Ключевое слово finally в блоке try используется для указания кода, который должен быть выполнен в любом случае, независимо от того, возникло исключение или нет.

- Что нужно сделать, чтобы реализовать свое собственное __исключение__?

Исключение через try-catch:

```
try:
    исполяем какой-то код
except Exception as e:
    обработка исключения
else:
    код, который будет исполнен в случае, когда не возникает исключения
finally:
    код, который гарантированно будет исполнен последним (всегда исполняется)
```

Исключение через raise:

```
raise IOError("текст исключения")
```

А если нам нужно собственное исключение, то можем сделать так:

```
class MyException(Exception):
    pass

a = 3
b = 0
try:
    if b == 0:
        raise MyException("b = {}, you can't do that".format(b))
except MyException as Err:
    print(Err)
    print("it's fine")
```

Т.е. мы создаем класс, который наследуется от какого-нибудь класса в иерархии исключений.

## Задания:
1) Реализовать структуру наследования классов геометрических фигур (__shape.py__). Каждый класс должен обладать методами `.area()` и 
`.perimeter()` для вычисления площади и периметра соответственно. Среди обязательных для реализации структур: круг, треугольник, прямоугольник, квадрат, ромб. Для простоты можно конструировать фигуры из точек, передающихся в порядке обхода фигуры по часовой стрелке.

Shape.py

3) Дополнить класс комплексных чисел из прошлого задания системой исключений: выбросом `ValueError` при вводе некорректных значений в сеттер класса, выбросом своего исключения в случае попытки перевода в экспоненциальную форму, когда это невозможно.
4) Написать программу калькулятор, которая считывает два комплексных числа и проводит с ними арифметические операции с обработкой вылезающих исключений: например если в процессе деления возникнет `ZeroDivisionError`, программа должна продолжить работу, предложив пользователю выбрать другую операцию.   

Calculator.py