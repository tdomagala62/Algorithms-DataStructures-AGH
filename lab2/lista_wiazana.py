
class Node:

    def __init__(self, data_, next_=None):
        self.data = data_
        self.next = next_


class LinkedList:

    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, data_):
        self.head = Node(data_, self.head)

    def append(self, data_):
        last_node = self.head
        if last_node is None:
            self.head = Node(data_)
            return
        while last_node.next:
            last_node = last_node.next
        last_node.next = Node(data_)

    def remove(self):
        if self.head:
            self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            return
        prev_node = None
        last_node = self.head
        while last_node.next:
            prev_node = last_node
            last_node = last_node.next
        prev_node.next = None

    def is_empty(self):
        return self.head is None

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
