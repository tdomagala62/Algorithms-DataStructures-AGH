import random
import time


class Element:
    def __init__(self, priority, data):
        self.__priority = priority
        self.__data = data

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __repr__(self):
        return str(self.__priority) + " : " + str(self.__data)


class Heap:
    def __init__(self, reserved_size=5, tab=None):
        if tab is None:
            self.reserved_size = reserved_size
            self.tab = [None for i in range(reserved_size)]
            self.heap_size = 0
        else:
            self.tab = tab
            self.heap_size = len(self.tab)
            self.reserved_size = self.heap_size
            for i in range(self.parent(self.heap_size - 1), -1, -1):
                if self.left(i) < self.heap_size and self.right(i) < self.heap_size:
                    self.fix_heap(i)

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
            self.tab[grater_idx], self.tab[start_idx] = self.tab[start_idx], self.tab[grater_idx]
            self.fix_heap(grater_idx)

    def sort_heap(self):
        while not self.is_empty():
            self.dequeue()

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.reserved_size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


class SelectSort:
    def __init__(self, tab):
        self.tab = tab

    def swap_sort(self):
        for i in range(len(self.tab)):
            m = self.tab.index(min(self.tab[i:]))
            self.tab[i], self.tab[m] = self.tab[m], self.tab[i]

    def shift_sort(self):
        for i in range(len(self.tab)):
            m = self.tab.index(min(self.tab[i:]))
            self.tab.insert(i, self.tab.pop(m))


if __name__ == "__main__":
    # TEST 1
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    my_data = []
    for i in data:
        my_data.append(Element(i[0], i[1]))
    sort_heap = Heap(tab=my_data.copy())
    sort_heap.print_tab()
    sort_heap.print_tree(0, 0)
    sort_heap.sort_heap()
    print(sort_heap.tab)
    print("Sortowanie niestabilne")

    # TEST 2
    long_list = [0]*10000
    for i in range(10000):
        num = random.randint(0, 99)
        long_list[i] = num
    long_list_copy = long_list.copy()
    t_start = time.perf_counter()
    heap = Heap(tab=long_list_copy)
    heap.sort_heap()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # TEST 3 swap_sort()
    select1 = SelectSort(my_data.copy())
    select1.swap_sort()
    print(select1.tab)
    print("Sortowanie niestabilne")

    long_list_copy2 = long_list.copy()
    t_start = time.perf_counter()
    select2 = SelectSort(long_list_copy2)
    select2.swap_sort()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # TEST 4 shift_sort()
    select3 = SelectSort(my_data.copy())
    select3.shift_sort()
    print(select3.tab)
    print("Sortowanie stabilne")

    long_list_copy3 = long_list.copy()
    t_start = time.perf_counter()
    select4 = SelectSort(long_list_copy3)
    select4.shift_sort()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

