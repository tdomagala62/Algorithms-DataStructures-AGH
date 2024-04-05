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


def insertion_sort(tab):
    for i in range(1, len(tab)):
        j = i
        while j > 0 and tab[j] < tab[j-1]:
            tab[j], tab[j-1] = tab[j-1], tab[j]
            j -= 1


def shell_sort(tab):
    n = len(tab)
    max_value = (2 * n/3) + 1
    k = 1
    while 3**k < max_value:
        k += 1
    k -= 1
    h = int((3**k - 1)/2)
    while h > 0:
        for i in range(h, n, h):
            j = i
            while j > 0 and tab[j] < tab[j-h]:
                tab[j], tab[j - h] = tab[j - h], tab[j]
                j -= h
        h = h // 3


if __name__ == "__main__":

    data = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    my_data = []
    for i in data:
        my_data.append(Element(i[0], i[1]))

    long_list = [0] * 100
    for i in range(100):
        num = random.randint(0, 99)
        long_list[i] = num

    # TEST AGLORYTMU INSERTION SORT
    print("Insertion sort")
    insertion_result = my_data.copy()
    insertion_sort(insertion_result)
    print(insertion_result)
    print("Sortowanie stabilne")
    insertion_result2 = long_list.copy()
    t_start = time.perf_counter()
    insertion_sort(insertion_result2)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print()

    # TEST AGLORYTMU SHELL SORT
    print("Shell sort")
    shell_result = my_data.copy()
    shell_sort(shell_result)
    print(shell_result)
    print("Sortowanie stabilne")
    shell_result2 = long_list.copy()
    t_start = time.perf_counter()
    shell_sort(shell_result2)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    print()
    print("Czas sortowania kopcowego: ~ 0.1984135")

