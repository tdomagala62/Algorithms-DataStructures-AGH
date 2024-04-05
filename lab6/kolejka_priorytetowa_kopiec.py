class Element:
    def __init__(self, priority, data):
        self.__priority = priority
        self.__data = data

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __str__(self):
        return str(self.__priority) + " : " + str(self.__data)


class Heap:
    def __init__(self, reserved_size=5):
        self.reserved_size = reserved_size
        self.tab = [None for i in range(reserved_size)]
        self.heap_size = 0

    def append(self):
        new_size = 2 * self.reserved_size
        new_tab = [self.tab[i] if i < self.heap_size else None for i in range(new_size)]
        self.reserved_size = new_size
        self.tab = new_tab

    def is_empty(self):
        return self.heap_size == 0

    def left(self, parent_idx):
        return 2 * parent_idx + 1

    def right(self, parent_idx):
        return 2 * parent_idx + 2

    def parent(self, child_idx):
        return (child_idx - 1) // 2

    def peek(self):
        return self.tab[0]

    def enqueue(self, element):
        if self.heap_size == self.reserved_size:
            self.append()
        element_idx = self.heap_size
        self.tab[element_idx] = element
        parent_idx = self.parent(element_idx)
        while element_idx and self.tab[element_idx] > self.tab[parent_idx]:
            temp = self.tab[element_idx]
            self.tab[element_idx] = self.tab[parent_idx]
            self.tab[parent_idx] = temp
            element_idx = parent_idx
            parent_idx = self.parent(element_idx)
        self.heap_size += 1

    def dequeue(self):
        if self.heap_size == 0:
            return None
        temp = self.tab[0]
        self.tab[0] = self.tab[self.heap_size - 1]
        self.tab[self.heap_size - 1] = temp
        self.heap_size -= 1
        self.fix_heap(0)
        return temp

    def fix_heap(self, start_idx):
        left_idx = self.left(start_idx) if self.left(start_idx) < self.heap_size else None
        right_idx = self.right(start_idx) if self.right(start_idx) < self.heap_size else None
        if left_idx and right_idx:
            grater_idx = left_idx if left_idx and self.tab[left_idx] > self.tab[right_idx] else right_idx
        elif left_idx:
            grater_idx = left_idx
        elif right_idx:
            grater_idx = right_idx
        else:
            return
        if self.tab[grater_idx] > self.tab[start_idx]:
            temp = self.tab[grater_idx]
            self.tab[grater_idx] = self.tab[start_idx]
            self.tab[start_idx] = temp
            self.fix_heap(grater_idx)

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.reserved_size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


if __name__ == "__main__":
    h1 = Heap()
    stringg = "GRYMOTYLA"
    lst = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    for idx, num in enumerate(lst):
        h1.enqueue(Element(num, stringg[idx]))
    h1.print_tree(0, 0)
    h1.print_tab()
    first = h1.dequeue()
    print(h1.peek())
    h1.print_tab()
    print(first)
    while True:
        element = h1.dequeue()
        if element is None:
            break
        print(element)
    h1.print_tab()
