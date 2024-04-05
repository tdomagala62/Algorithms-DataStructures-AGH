
class Queue:
    def __init__(self):
        self.tab = [None for i in range(5)]
        self.size = 5
        self.write_idx = 0
        self.read_idx = 0

    def next_index(self, index):
        if index == self.size-1:
            return 0
        else:
            return index+1

    def is_empty(self):
        return self.read_idx == self.write_idx

    def realloc(self):
        new_size = 2*self.size
        new_tab = [self.tab[i] if i < self.write_idx else None for i in range(new_size)]
        rewrite_data_size = self.size-self.read_idx
        for i in range(rewrite_data_size):
            new_tab[new_size-i-1] = self.tab[self.size-i-1]
        self.tab = new_tab
        self.read_idx = new_size-rewrite_data_size
        self.size = new_size

    def peek(self):
        return None if self.is_empty() else self.tab[self.read_idx]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            previous_index = self.read_idx
            self.read_idx = self.next_index(self.read_idx)
            return self.tab[previous_index]

    def enqueue(self, data):
        self.tab[self.write_idx] = data
        self.write_idx = self.next_index(self.write_idx)
        if self.read_idx == self.write_idx:
            self.realloc()

    def __str__(self):
        result = "["
        iterator = self.read_idx
        while iterator != self.write_idx:
            result += str(self.tab[iterator])
            result += " " if self.next_index(iterator) != self.write_idx else ""
            iterator = self.next_index(iterator)
        return result + "]"

    def display_list(self):
        print("TEST", self.tab)


def main():
    queue1 = Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    queue1.enqueue(4)
    print(queue1.dequeue())
    print(queue1.peek())
    print(queue1)
    queue1.enqueue(5)
    queue1.enqueue(6)
    queue1.enqueue(7)
    queue1.enqueue(8)
    queue1.display_list()
    while not queue1.is_empty():
        print(queue1.dequeue())
    print(queue1)


main()
