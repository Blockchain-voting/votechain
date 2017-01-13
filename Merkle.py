from Node import *
from hashlib import sha256
hash_function = sha256

class Merkle:
    def __init__(self, root, prev_block=''):
        self.cap_size = 15
        self.leaves = []
        self.tree = []
        self.prev_block = prev_block  # hash value of previous block
        self.proof_work = ''          # hash value of current block (simulated proof of work)
        
        if root:
            self.prev_block = hash_function(''.join(random.choice(string.hexdigits) for i in range(10))).hexdigest()
            print "random hash %s" % self.prev_block
        else:
            print "previous hash %s" % prev_block

    def add_leaf(self, leaf):
        node = Node(leaf)
        self.leaves.append(node)
        print len(self.leaves)

        if len(self.leaves) == self.cap_size:
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

    def validate(self):
        if self.proof_work == hash_function(''.join(i.value for i in self.leaves)).hexdigest():
            return True
        else:
            return False

    def count(self):
        vote_list = []
        for n in self.tree:
            vote_list.append({'id':n.vote.id, 'choice':n.vote.choice, 'public key':n.vote.public_key})
        return vote_list

    def __build(self):
        # defining temp root and children nodes
        root = self.leaves[0]

        # appending root to tree
        self.tree.append(root)

        print len(self.tree)

        # i - left | i + 1 - right
        for i in range(1, len(self.leaves), 2):
            # setting variables for new left and right node
            left = self.leaves[i]
            right = self.leaves[i + 1]
            print "iteration %s" % i

            # getting parent with traverse function
            parent_id = self.__traverse()
            parent = self.tree[parent_id]

            # setting left and right child of parent
            parent.set_left_child(left)
            parent.set_right_child(right)

            # setting parent of left and right children
            left.set_parent(parent)
            right.set_parent(parent)

            # adding nodes to tree
            self.tree.append(left)
            self.tree.append(right)

            print len(self.tree)

        self.__print_tree()

    # fancy word for a loop
    def __traverse(self):
        for i in range(len(self.tree)):
            if self.tree[i].empty() == True:
                print i
                return i
            else:
                print "not this node, move along"

    def __print_tree(self):
        for i in range(len(self.tree)):
            print "Node - %s" % i
            self.tree[i].print_node()

    def __verify_tree(self):
        print 'validating'
