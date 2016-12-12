from Node import *
from hashlib import sha256
hash_function = sha256

class Merkle:
    def __init__(self):
        self.cap_size = 10
        self.leaves=[]

    def add_leaf(self, leaf):
        node = Node(leaf)
        self.leaves.append(node)
        print self.__length()

        if self.__length() == self.cap_size:
            return "full"
        else:
            return "growing"

    def get_values(self):
        output_str = ''
        for l in self.leaves:
            output_str += str(l.value)
        return output_str

    def build(self):
        return "building"

    # playing with python private functions
    def __length(self):
        return len(self.leaves)
