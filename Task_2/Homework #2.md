## Контрольные вопросы:
- Как расшифровывается __ООП__, в чем заключается идея __объекта__?

ООП - объектно-ориентированное программирование. Объект представляет собой конкретный экземпляр класса. Класс определяет общие свойства и методы для группы объектов, а объекты являются конкретными представителями этого класса.

- В чем опасность __переменных класса__?

Может возникнуть неявная зависимость. В Python есть возможность изменения значения переменных класса извне класса. Это может привести к неожиданным результатам и нарушению инкапсуляции. Чтобы избежать этого можно использовать инкапсуляцию (т.е. сделать интерфейс для взаимодействия пользователя с реализацией) и делать переменные класса приватными, добавляя перед их именами двойное подчеркивание __. Такие переменные становятся недоступными для прямого доступа извне класса.

- Как называются __переменные__ и __функции__, принадлежащие __экземпляру класса__? 

Переменная экземпляра класса - поле, атрибут.

Функция экземпляра класса - метод.

- Что такое __инициализатор класса__ и чем он отличается от __конструктора__?

Инициализатор класса - это специальный метод, который вызывается при создании нового объекта класса. Он имеет имя __init__() и используется для инициализации атрибутов объекта. Конструктор - это также специальный метод, который вызывается при создании нового объекта класса. __new()__.

- Какую роль играет ключевое слово `self`?
  
Ключевое слово self в Python используется для ссылки на текущий объект класса. Оно позволяет обращаться к атрибутам и методам объекта внутри класса. Когда вызывается метод объекта, self автоматически передается в качестве первого аргумента, чтобы указать, что метод вызывается для конкретного объекта.


- Как переменная `__dict__` связана с остальными __переменными класса__? Что это говорит нам о природе объектов в __Python__?

Переменная __dict__ в Python является словарем, который содержит все атрибуты объекта класса и их значения. Она позволяет получить доступ к атрибутам объекта и изменять их значения. Таким образом, __dict__ связана с остальными переменными класса и позволяет управлять ими.


- В чем заключается основная идея __инкапсуляции__?

Инкапсуляция - изоляция данных от пользователя. По сути мы создаем перегородку между пользователем и реализацией, давая пользователю доступ с помощью интерфейса. Это позволяет контролировать доступ к атрибутам и методам класса и обеспечивает безопасность.

- Можно ли сказать что __инкапсуляция__ в полной мере присутствует в __Python__? Каким образом мы её добиваемся?

В Python инкапсуляция не является строгой, так как все атрибуты и методы класса доступны извне. Однако, можно исользовать двойное подчеркивания перед именами переменных, что делает их приватными и не доступными для прямого доступа извне класса.

## Задания:
См. Classes.py
1) Создайте класс для хранения комплексных чисел с инициализатором.
2) Обеспечьте его необходимыми геттерами и сеттерами.
3) Реализуйте методы, позволяющие представлять комплексное число в экспоненциальной форме.
4) Добавьте функции, позволяющие складывать, вычитать, умножать и делить два комплексных числа, результатом работы которых будет новое комплексное число.