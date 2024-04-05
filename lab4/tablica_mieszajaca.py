
class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.__tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hash(self, key):
        value = 0
        if isinstance(key, (int, float)):
            value = key
        elif isinstance(key, str):
            for i in key:
                value += ord(i)
        else:
            raise ValueError("Invalid key")
        return value % self.size

    def collision(self, occupied_index, i):
        index = self.hash(occupied_index + self.c1*i + self.c2*(i**2))
        return index

    def search(self, key):
        start_index = self.hash(key)
        if self.__tab[start_index] is not None and self.__tab[start_index].key == key:
            return self.__tab[start_index].data
        else:
            for i in range(1, self.size):
                index = self.collision(start_index, i)
                if self.__tab[index] is None:
                    continue
                if self.__tab[index].key == key:
                    return self.__tab[index].data
            return None

    def insert(self, element):
        start_index = self.hash(element.key)
        if self.__tab[start_index] is None or self.__tab[start_index].key == element.key:
            self.__tab[start_index] = element
            return
        else:
            for i in range(1, self.size):
                index = self.collision(start_index, i)
                if self.__tab[index] is None or self.__tab[index].key == element.key:
                    self.__tab[index] = element
                    return
            print("Brak miejsca")
            #raise Exception("Lack of space!")

    def remove(self, key):
        start_index = self.hash(key)
        if self.__tab[start_index] is not None and self.__tab[start_index].key == key:
            self.__tab[start_index] = None
            return
        else:
            for i in range(1, self.size):
                index = self.collision(start_index, i)
                if self.__tab[index] is None:
                    continue
                if self.__tab[index].key == key:
                    self.__tab[index] = None
                    return
            print("Brak danej")
            #raise Exception("Data do not exist!")

    def __str__(self):
        result = "{"
        for i in range(self.size):
            comma = 0 if i == self.size-1 else 1
            if self.__tab[i] is None:
                result += ("None" + comma*", ")
            else:
                result += (str(self.__tab[i].key) + ":" + str(self.__tab[i].data) + comma*", ")
        return result + "}"


def test1(size, c1=1, c2=0):
    hashTable1 = HashTable(size, c1, c2)
    for i in range(1, 16):
        num = i
        if i == 6:
            num = 18
        elif i == 7:
            num = 31
        hashTable1.insert(Element(num, chr(64+i)))
    print(hashTable1)
    print(hashTable1.search(5))
    print(hashTable1.search(14))
    hashTable1.insert(Element(5, 'Z'))
    print(hashTable1.search(5))
    hashTable1.remove(5)
    print(hashTable1)
    print(hashTable1.search(31))
    hashTable1.insert(Element('test', 'W'))
    print(hashTable1)


def test2(size, c1=1, c2=0):
    hashTable1 = HashTable(size, c1, c2)
    for i in range(1, 16):
        hashTable1.insert(Element(i*13, chr(64 + i)))
    print(hashTable1)


if __name__ == "__main__":
    print("Test 1:")
    test1(13)
    print("Test 2:")
    test2(13)
    print("Test 3:")
    test2(13, 0, 1)
    print("Test 4:")
    test1(13, 0, 1)


