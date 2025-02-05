#Big O Notation

# Insertion: O(1)
# Deletion: O(1)
# Search: O(n)
# Access: O(n)

class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    def set_link_node(self, link_node):
        self.link_node = link_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_link_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_link_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_link_node()
        else:
            while current_node:
                next_node = current_node.get_link_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_link_node(next_node.get_link_node())
                    current_node = None
                else:
                    current_node = next_node

    def reversePrint(curr):

        if curr is None:
            return
        
        reversePrint(curr.next)

        print(curr.data, end="\n")
