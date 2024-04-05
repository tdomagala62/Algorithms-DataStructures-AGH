
# Global variable
size = 4


class Node:
    def __init__(self, data=None):
        self.tab = [None for i in range(size)]
        self.tab[0] = data
        self.elements = 0
        self.next = None

    def insert(self, index, data):
        # Works
        last_elem = self.tab[size-1]
        for i in range(min(self.elements-1, size-2), index-1, -1):
            self.tab[i+1] = self.tab[i]
        self.tab[index] = data
        self.elements += 1
        return last_elem

    def remove(self, index):
        pass


class UnrolledLinkedList:
    def __init__(self):
        self.first = None

    def calculate_tab(self, index):
        current_node = self.first
        node_number = 0
        while index > current_node.elements:
            index -= current_node.elements
            if current_node.next is None:
                return node_number, current_node.elements
            current_node = current_node.next
            node_number += 1
        return node_number, index

    def get(self, index):
        tab_number, tab_index = self.calculate_tab(index)
        current_node = self.first
        for i in range(tab_number):
            current_node = current_node.next
        return current_node[tab_index]

    def insert(self, index, data):
        if self.first is None:
            self.first = Node(data)

        # tab_number, tab_index = self.calculate_tab(index)
        # current_node = self.first
        # previous_node = None
        # for i in range(tab_number):
        #     previous_node = current_node
        #     current_node = current_node.next
        # if current_node is None:
        #     current_node = Node()
        #     previous_node.next = current_node
        #     # dokonczyc
        # if current_node.elements == size:
        #     pass
        # else:
        #     # gdy first = None
        #     # gdy jest full size
        #     #
        #     pass


    def delete(self):
        pass

    def display(self):
        current_node = self.first
        while current_node is not None:
            print(current_node.tab, end="")
            current_node = current_node.next


if __name__ == "__main__":
    list1 = UnrolledLinkedList()
    list1.insert(2, "0")
    list1.display()
    print(list1.calculate_tab(2))
