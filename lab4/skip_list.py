from random import random


def random_level(p, max_level):
    lvl = 1
    while random() < p and lvl < max_level:
        lvl = lvl + 1
    return lvl


class Element:
    def __init__(self, max_level, key, data, level=None):
        self.key = key
        self.data = data
        self.levels = level if level else random_level(0.5, max_level)
        self.next = [None for i in range(self.levels)]


class SkipList:
    def __init__(self, max_level):
        self.head = Element(max_level, None, None, max_level)
        self.max_level = max_level

    def search(self, search_key):
        element = self.head
        for lvl in range(self.max_level - 1, -1, -1):
            while element.next[lvl] and search_key > element.next[lvl].key:
                element = element.next[lvl]
            if element.next[lvl] and element.next[lvl].key == search_key:
                return element.next[lvl].data
        return None

    def insert(self, insert_key, data):
        previous_levels = [None for i in range(self.max_level)]
        element = self.head
        for lvl in range(self.max_level - 1, -1, -1):
            while element.next[lvl] and insert_key > element.next[lvl].key:
                element = element.next[lvl]
            if element.next[lvl] and element.next[lvl].key == insert_key:
                element.next[lvl].data = data
                return
            previous_levels[lvl] = element
        new_element = Element(self.max_level, insert_key, data)
        for lvl in range(new_element.levels):
            new_element.next[lvl] = previous_levels[lvl].next[lvl]
            previous_levels[lvl].next[lvl] = new_element

    def delete(self, delete_key):
        previous_levels = [None for i in range(self.max_level)]
        element = self.head
        for lvl in range(self.max_level - 1, -1, -1):
            while element.next[lvl] and delete_key > element.next[lvl].key:
                element = element.next[lvl]
            previous_levels[lvl] = element
        if element.next[0] and element.next[0].key == delete_key:
            next_element = element.next[0]
            for i in range(next_element.levels):
                previous_levels[i].next[i] = next_element.next[i]
            return
        return None

    def __str__(self):
        element = self.head.next[0]
        result = ""
        while element:
            result += ("(" + str(element.key) + ":" + str(element.data) + ") ")
            element = element.next[0]
        return result

    def display_list_(self):
        node = self.head.next[0]  # pierwszy element na poziomie 0
        keys = []                 # lista kluczy na tym poziomie
        while node:
            keys.append(node.key)
            node = node.next[0]

        for lvl in range(self.max_level-1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while node:
                while node.key > keys[idx]:
                    print("  ", end=" ")
                    idx += 1
                idx += 1
                print("{:2d}".format(node.key), end=" ")
                node = node.next[lvl]
            print("")


if __name__ == "__main__":
    skip_list = SkipList(3)
    for i in range(1, 16):
        skip_list.insert(i, chr(64 + i))
    skip_list.display_list_()
    print(skip_list.search(2))
    skip_list.insert(2, "Z")
    print(skip_list.search(2))
    skip_list.delete(5)
    skip_list.delete(6)
    skip_list.delete(7)
    print(skip_list)
    skip_list.insert(6, "W")
    print(skip_list)

    skip_list2 = SkipList(3)
    for i in range(15, 0, -1):
        skip_list2.insert(i, chr(64 + 16 - i))
    skip_list2.display_list_()
    print(skip_list2.search(2))
    skip_list2.insert(2, "Z")
    print(skip_list2.search(2))
    skip_list2.delete(5)
    skip_list2.delete(6)
    skip_list2.delete(7)
    print(skip_list2)
    skip_list2.insert(6, "W")
    print(skip_list2)
