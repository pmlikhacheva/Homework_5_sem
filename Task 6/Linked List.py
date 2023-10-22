import pickle
import os

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

    def insert(self, index, value):
        if index < 0 or index > len(self):
            return None
        new_node = Node(value)

        if index == 0:
            new_node.set_next_pointer(self._head)
            if self._head is not None:
                self._head.set_prev_pointer(new_node)
            self._head = new_node
            
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
            
        self._len += 1

        
    def __getitem__(self, item):

        if item < 0 or item >= len(self):
            return None

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
            return None

        sum = Linked_list()
        for i in range(len(self)):
            sum.append(self[i])
        for i in range(len(other)):
            sum.append(other[i])

        return sum
    def __iter__(self):
        current_node = self._head
        while current_node is not None:
            yield current_node.get_val()
            current_node = current_node.get_next_ptr()
    
    #сохраням файл
    def save(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod #декоратор, который используется для создания метода,
    #который ничего не знает о классе или экземпляре, через который он был вызван.
    def load(filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл {filename} не существует")
        with open(filename, "rb") as file:
            return pickle.load(file)


class OpenLinkedList:
    def __init__(self, filename):
        
        self.filename = filename

    def __enter__(self):
        self.linked_list = Linked_list.load(self.filename)
        return self.linked_list

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.linked_list.save(self.filename)

            

list = Linked_list([6, 7, 8])
list.save("2.txt")
list.load("2.txt") #работает
#list.load("3.txt") не работает - такой файл не существует

print(list) #[6, 7, 8]

with OpenLinkedList("2.txt") as list:
    list.append(1)
    list.append(2)
    list.append(3)

print(list) #[6, 7, 8, 1, 2, 3]