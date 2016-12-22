from Node import *
from hashlib import sha256
hash_function = sha256

class Merkle:
    def __init__(self, root=False, prev_block=''):
        self.cap_size = 10
        self.leaves=[]
        self.prev_block = prev_block  # hash value of previous block
        self.proof_work = ''          # hash value of current block (simulated proof of work)

        if root:
            self.prev_block = hash_function(''.join(random.choice(string.hexdigits) for i in range(10))).hexdigest()
            print self.prev_block

    def add_leaf(self, leaf):
        node = Node(leaf)
        self.leaves.append(node)
        print self.__length()

        if self.__length() == self.cap_size:
            return "full", node.value
        else:
            return "growing", node.value

    def get_values(self):
        output_str = ''
        for l in self.leaves:
            output_str += str(l.value)
        return output_str

    def build(self):
        self.proof_work = hash_function(''.join(i.value for i in self.leaves)).hexdigest()
        return "building"

    # playing with python private functions
    def __length(self):
        return len(self.leaves)
