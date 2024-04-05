
class Node:

    def __init__(self, data_, previous_=None, next_=None):
        self.data = data_
        self.prev = previous_
        self.next = next_


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def destroy(self):
        self.head = None
        self.tail = None

    def add(self, data_):
        new_node = Node(data_, next_=self.head)
        if self.head:
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def append(self, data_):
        new_node = Node(data_, previous_=self.tail)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

    def remove_end(self):
        if self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def length(self):
        if self.head is None:
            return 0
        length = 1
        last_node = self.head
        while last_node.next:
            length += 1
            last_node = last_node.next
        return length

    def get(self):
        return self.head.data

    def __str__(self):
        if self.head is None:
            return "Empty list!"
        result = ""
        last_node = self.head
        while last_node.next:
            result += ("-> " + str(last_node.data)+"\n")
            last_node = last_node.next
        result += ("-> " + str(last_node.data))
        return result


def main():
    data = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]

    uczelnie = LinkedList()
    uczelnie.append(data[0])
    uczelnie.append(data[1])
    uczelnie.append(data[2])
    uczelnie.add(data[3])
    uczelnie.add(data[4])
    uczelnie.add(data[5])
    print(uczelnie)
    print(uczelnie.length())
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(data[0])
    uczelnie.remove_end()
    print(uczelnie)


main()
