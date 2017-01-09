from Merkle import *
from hashlib import sha256
hash_function = sha256

# Handler (i.e. blockchain) for each election.
# Manages opening, closing of elections
# Adds votes, verifies votes, etc
# holds the chain and all the pointers
class Handler:
    def __init__(self, name, el_id, options):
        self.name = name                # name of the election
        self.id = el_id                 # id of the election
        self.options = options          # choices for the election
        self.chain = []                 # list of trees
        self.active_tree = Merkle(True) # pointer to open tree, setting first block as root

    # add vote to tree
    # need to get the id of the tree
    def vote(self, v):
        return_str = self.active_tree.add_leaf(v)
        if return_str[0] == "full":
            self.cap_tree()
        return return_str[1] #return hash of vote

    # if tree is length of 10
    def cap_tree(self):
        # build the tree
        print self.active_tree.build()
        # add previous blocks hash to this block
        # self.active_tree.prev_block = self.chain[-1].proof_work
        # inert into chain
        self.chain.append(self.active_tree)
        # create a new merkle tree
        self.active_tree = Merkle(False, self.active_tree.proof_work)

        print 'Number of blocks', len(self.chain)

    # change the name of the election
    def change_name(self, new_name):
        self.name = new_name

        # change the options for this elections
        # takes the whole set of options, NOT a single one to add or remove
        def change_options(self, new_opt):
            self.options = new_opt
