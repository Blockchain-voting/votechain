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
        self.snapshot = []              # snapshot of last time chain was counted
        self.active_tree = Merkle(True) # pointer to open tree, setting first block as root

    # add vote to tree
    # need to get the id of the tree
    def vote(self, v):
        return_str = self.active_tree.add_leaf(v)
        if return_str[0] == "full":
            self.cap_tree()
        return return_str[1] #return hash of vote

    def count(self):
        """
        1 - Check each block is linked correctly
        2 - Compare current hashes against snapshot hashes
            Take snapshot of block hashes
        3 - In each block sum votes
        """
        chain = True
        proof = True
        hashes = True
        votes = []

        # verifying all proof of work is still valid
        if len(self.chain) > 1:
            for i in range(1, len(self.chain)):
                if self.chain[i - 1].proof_work != self.chain[i].prev_block:
                    chain = False
        else:
            print "chain is still too short to properly verify"

        # verifying the node proof of work match their stored value
        for b in self.chain:
            if b.validate() == False:
                proof = False

        # verifying the tree values match stored values
        if len(self.snapshot) > 1:
            for i in range(len(self.snapshot)):
                if self.snapshot[i] != self.chain[i].proof_work:
                    hashes = False
        else:
            for b in self.chain:
                self.snapshot.append(b.proof_work)
            print self.snapshot

        # if any of the checks return false then return false and empty votes
        if chain != True or proof != True or hashes != True:
            return False, votes
        else:
            # run through all trees and count their votes to return with True condition
            for b in self.chain:
                votes.append(b.count())
            return {'secure':True,'votes':votes}


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
