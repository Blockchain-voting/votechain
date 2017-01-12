from Node import *
from hashlib import sha256
hash_function = sha256

class Merkle:
    def __init__(self, root, prev_block=''):
        self.cap_size = 15
        self.leaves=[]
        self.tree=[]
        self.prev_block = prev_block  # hash value of previous block
        self.proof_work = ''          # hash value of current block (simulated proof of work)
        print "root: %s" % root
        if root:
            self.prev_block = hash_function(''.join(random.choice(string.hexdigits) for i in range(10))).hexdigest()
            print "random hash %s" % self.prev_block
        else:
            print "previous hash %s" % prev_block

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
        # self.tree = list(self.leaves)

        self.__build()

    # playing with python private functions
    def __length(self):
        return len(self.leaves)

    def __build(self):
        # defining temp root and children nodes
        root = self.leaves[0]

        # appending root to tree
        self.tree.append(root)

        # i - left | i + 1 - right
        for i in range(1, self.__length(), 2):
            left = self.leaves[i]
            right = self.leaves[i + 1]

            for n in self.tree:
                if n.empty() == True:
                    n.left_child = left
                    n.right_child = right
                    left.parent = n
                    right.parent = n

                self.tree.append(left)
                self.tree.append(right)
            print len(self.tree)
