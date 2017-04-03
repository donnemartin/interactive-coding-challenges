from collections import OrderedDict


class Node(object):

    def __init__(self, key, parent=None, terminates=False):
        self.key = key
        self.terminates = False
        self.parent = parent
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = Node('')

    def find(self, word):
        if word is None:
            raise TypeError('word cannot be None')
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node if node.terminates else None

    def insert(self, word):
        if word is None:
            raise TypeError('word cannot be None')
        node = self.root
        parent = None
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = Node(char, parent=node)
                node = node.children[char]
        node.terminates = True

    def remove(self, word):
        if word is None:
            raise TypeError('word cannot be None')
        node = self.find(word)
        if node is None:
            raise KeyError('word does not exist')
        node.terminates = False
        parent = node.parent
        while parent is not None:
            # As we are propagating the delete up the 
            # parents, if this node has children, stop
            # here to prevent orphaning its children.
            # Or
            # if this node is a terminating node that is
            # not the terminating node of the input word, 
            # stop to prevent removing the associated word.
            if node.children or node.terminates:
                return
            del parent.children[node.key]
            node = parent
            parent = parent.parent

    def list_words(self):
        result = []
        curr_word = ''
        self._list_words(self.root, curr_word, result)
        return result

    def _list_words(self, node, curr_word, result):
        if node is None:
            return
        for key, child in node.children.items():
            if child.terminates:
                result.append(curr_word+key)
            self._list_words(child, curr_word+key, result)