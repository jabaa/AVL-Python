__author__ = 'Thomas Sablik'

from math import log10
from math import floor


def spaces(x):
    spaces_string = ""
    for i in range(x):
        spaces_string += " "
    return spaces_string


class Node(object):
    l_child = None
    r_child = None
    height = 0

    def __init__(self, key):
        self.key = key


class AVL(object):
    def __init__(self, key=None):
        if key is None:
            self.root = None
        else:
            self.root = Node(key)

    def __repr__(self):
        nodes_string = ""
        height = -1
        if self.root is not None:
            node_width = floor(log10(self.get_max())) + 1
        else:
            return nodes_string

        nodes = []
        if self.root is not None:
            nodes.append(self.root)
            height = self.root.height
            width = ((2 ** height) * 2) - 1
            nodes_string = spaces(node_width * ((width - 1) // 2)) + "{0:^{1}}".format(str(self.root.key),node_width) + spaces(node_width * ((width - 1) // 2)) + "\n"
        for i in range(1, height+1):
            new_nodes = []
            for j in nodes:
                if j is None:
                    new_nodes.append(None)
                    nodes_string += spaces(node_width * (2**(height - i) - 1))
                    nodes_string += spaces(node_width)
                    nodes_string += spaces(node_width * (2**(height - i) - 1))
                    nodes_string += spaces(node_width)
                    new_nodes.append(None)
                    nodes_string += spaces(node_width * (2**(height - i) - 1))
                    nodes_string += spaces(node_width)
                    nodes_string += spaces(node_width * (2**(height - i) - 1))
                else:
                    if j.l_child is not None:
                        new_nodes.append(j.l_child)
                        nodes_string += spaces(node_width * (2**(height - i) - 1))
                        nodes_string += "{0:^{1}}".format(str(j.l_child.key),node_width)
                        nodes_string += spaces(node_width * (2**(height - i) - 1))
                    else:
                        new_nodes.append(None)
                        nodes_string += spaces(node_width * (2**(height - i) - 1))
                        nodes_string += spaces(node_width)
                        nodes_string += spaces(node_width * (2**(height - i) - 1))
                    nodes_string += spaces(node_width)
                    if j.r_child is not None:
                        new_nodes.append(j.r_child)
                        nodes_string += spaces(node_width * (2**(height - i) - 1))
                        nodes_string += "{0:^{1}}".format(str(j.r_child.key),node_width)
                        nodes_string += spaces(node_width * (2**(height - i) - 1))
                    else:
                        new_nodes.append(None)
                        nodes_string += spaces(node_width * (2**(height - i) - 1))
                        nodes_string += spaces(node_width)
                        nodes_string += spaces(node_width * (2**(height - i) - 1))
                nodes_string += spaces(node_width)
            nodes_string = nodes_string[:-node_width]
            nodes_string += "\n"
            nodes = new_nodes.copy()
        return nodes_string

    def insert(self, key):
        node = Node(key)
        is_inserted = False
        edited_nodes = []
        if self.root is not None:
            curr_node = self.root
            edited_nodes.append(curr_node)
        else:
            self.root = node
            is_inserted = True

        while not is_inserted:
            if node.key >= curr_node.key:
                if curr_node.r_child is not None:
                    curr_node = curr_node.r_child
                    edited_nodes.append(curr_node)
                else:
                    curr_node.r_child = node
                    is_inserted = True
            else:
                if curr_node.l_child is not None:
                    curr_node = curr_node.l_child
                    edited_nodes.append(curr_node)
                else:
                    curr_node.l_child = node
                    is_inserted = True

        for curr_node in reversed(edited_nodes):
            curr_node.height = max(self.get_height(curr_node.l_child), self.get_height(curr_node.r_child)) + 1

    def get_max(self):
        if self.root is None:
            return None
        else:
            curr_node = self.root
            while curr_node.r_child is not None:
                curr_node = curr_node.r_child
            return curr_node.key

    @staticmethod
    def get_height(node):
        if node is None:
            return -1
        else:
            return node.height
