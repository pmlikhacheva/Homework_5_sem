class Node:
    def __init__(self, value, prev_pointer=None, next_pointer=None):
        self._val = value
        self._prev_ptr = prev_pointer
        self._next_ptr = next_pointer

    def get_value(self):
        return self._val

    def set_value(self, x):
        self._val = x

    def get_prev_pointer(self):
        return self._prev_ptr

    def set_prev_pointer(self, x):
        self._prev_ptr = x

    def get_next_pointer(self):
        return self._next_ptr

    def set_next_pointer(self, x):
        self._next_ptr = x


class Linked_list:
    ###
    # №2
    ###
    def __init__(self, values=None):
        self._head = None
        self._tale = None
        self._len = 0
        if values is not None:
            for value in values:
                self.append(value)

    def __len__(self):
        return self._len

    def append(self, x):
        curr_node = Node(x, self._tale)
        if len(self) == 0:
            self._head = curr_node
        else:
            self._tale.set_next_pointer(curr_node)
        self._tale = curr_node
        self._len += 1

    def pop(self):
        if len(self) > 1:
            res = self._tale.get_value()
            self._tale = self._tale.get_prev_pointer()
            self._tale.set_next_pointer(None)
            self._len -= 1
        elif len(self) == 1:
            res = self._tale.get_value()
            self._tale = None
            self._head = None
            self._len -= 1
        else:
            res = None
        return res
    ###
    # №3
    ###
    
    def insert(self, index, value):
        if index < 0 or index > len(self):
            return None #здесь должно быть исключение
        new_node = Node(value)
        # если мы добавляем элемент с индексом 0, то мы добавляем его в начало,
        # тогда новый элемент будет связан только с одним элементом, который
        # раньше был началом списка
        if index == 0:
            new_node.set_next_pointer(self._head)
            if self._head is not None:
                self._head.set_prev_pointer(new_node)
            self._head = new_node
        # если мы добавляем элемент с индексом len(self), то мы добавляем его в
        # конец, тогда новый элемент будет связан только с одним элементом, который
        # раньше был концом списка
        elif index == len(self):
            new_node.set_prev_pointer(self._tale)
            if self._tale is not None:
                self._tale.set_next_pointer(new_node)
            self._tale = new_node
        else:
            curr_node = self._head
            for i in range(index - 1):
                curr_node = curr_node.get_next_pointer()
            next_node = curr_node.get_next_pointer()

            new_node.set_prev_pointer(curr_node)
            new_node.set_next_pointer(next_node)

            curr_node.set_next_pointer(new_node)
            next_node.set_prev_pointer(new_node)
            
        # увеличиваем длину списка
        self._len += 1

        
    def __getitem__(self, item):
        ### №1
        #1. Проверяем, есть ли вообще такой индекс в списке
        #2. Если искомый элемент во второй половине списка, то нам ничего не мешает
        # попробовать достать его с конца списка
        ###
        if item < 0 or item >= len(self): #А так можно или это red flag?
            return None #здесь должно быть исключение

        curr_node = self._head
        if item < len(self) // 2:
            for i in range(item):
                curr_node = curr_node.get_next_pointer()
        else:
            curr_node = self._tale
            for i in range(len(self) - item - 1):
                curr_node = curr_node.get_prev_pointer()

        return curr_node.get_value()


    def __str__(self):
        return "[" + ", ".join(str(self[i]) for i in range(len(self))) + "]"
    
    def __add__(self, other):
        if not isinstance(other, Linked_list):
            return None #здесь должно быть исключение

        sum = Linked_list()
        for i in range(len(self)):
            sum.append(self[i])
        for i in range(len(other)):
            sum.append(other[i])

        return sum


list1 = Linked_list([6, 7, 8])
print(list1)
list1.insert(1, 10)
print(list1)

list2 = Linked_list([1, 2, 3])
list = list1 + list2
print(list)  # [6, 10, 7, 8, 1, 2, 3]

###
    # 1. обращение к элементу по индексу должно занимать не более чем N/2;
    # 2. Инициализиация листа заданным набором чисел;
    # 3. Метод insert();
    # 4. Переопределим оператор сложения двух листов как их конкатенацию.
###