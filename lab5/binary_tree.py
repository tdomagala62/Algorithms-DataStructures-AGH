
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __search(self, key, node):
        if key == node.key:
            return node.value
        elif key < node.key and node.left:
            return self.__search(key, node.left)
        elif node.right:
            return self.__search(key, node.right)
        else:
            return None

    def search(self, key):
        if self.root is None:
            return None
        else:
            return self.__search(key, self.root)

    def insert(self, key, value, node=None):
        if node is None:
            if self.root is None:
                self.root = Node(key, value)
                return
            else:
                node = self.root
        if node:
            if key < node.key:
                if node.left:
                    self.insert(key, value, node.left)
                else:
                    node.left = Node(key, value)
            elif key > node.key:
                if node.right:
                    self.insert(key, value, node.right)
                else:
                    node.right = Node(key, value)
            else:
                node.value = value

    def delete(self, key):
        if self.root is None:
            return
        else:
            is_left = False
            previous_node = None
            current_node = self.root

            while current_node.key != key:
                previous_node = current_node
                if key > current_node.key:
                    is_left = False
                    current_node = current_node.right
                else:
                    is_left = True
                    current_node = current_node.left
                if current_node is None:
                    #print("nie znaleziono")
                    return

            if current_node.left and current_node.right:
                previous_search_node = None
                search_node = current_node.right
                while search_node.left is not None:
                    previous_search_node = search_node
                    search_node = search_node.left
                search_node.left = current_node.left
                if previous_search_node is not None:
                    previous_search_node.left = search_node.right
                    search_node.right = current_node.right
                if previous_node:
                    if is_left:
                        previous_node.left = search_node
                    else:
                        previous_node.right = search_node
                else:
                    self.root = search_node

            elif current_node.left is None and current_node.right is None:
                if previous_node:
                    if is_left:
                        previous_node.left = None
                    else:
                        previous_node.right = None
                else:
                    self.root = None

            else:
                if previous_node:
                    if is_left:
                        previous_node.left = current_node.left if current_node.left else current_node.right
                    else:
                        previous_node.right = current_node.left if current_node.left else current_node.right
                else:
                    self.root = current_node.left if current_node.left else current_node.right

    def print(self, node=None):
        first_node = False
        if node is None:
            first_node = True
            node = self.root
            if node is None:
                return
        if node.left:
            self.print(node.left)
        print(str(node.key) + " " + str(node.value) + ",", end="")
        if node.right:
            self.print(node.right)
        if first_node:
            print("")

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self.__print_tree(node.left, lvl + 5)

    def __height(self, node, max_height=-1):
        if node.left is None and node.right is None:
            return max_height + 1
        elif node.left and node.right:
            left_height = self.__height(node.left, max_height + 1)
            right_height = self.__height(node.right, max_height + 1)
            return left_height if left_height > right_height else right_height
        elif node.left:
            return self.__height(node.left, max_height + 1)
        else:
            return self.__height(node.right, max_height + 1)

    def height(self):
        if self.root is None:
            return -1
        else:
            return self.__height(self.root)


if __name__ == '__main__':
    tree = Tree()
    data = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key, value in data.items():
        tree.insert(key, value)
    tree.print_tree()
    tree.print()
    print(tree.search(24))
    tree.insert(20, "AA")
    tree.insert(6, "M")
    tree.delete(62)
    tree.insert(59, "N")
    tree.insert(100, "P")
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, "R")
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    tree.print()
    tree.print_tree()
