from hashlib import sha256
import string
import random
hash_function = sha256

class Node:
    def __init__(self, vote_obj):
        # hashes vote data with sha256 algorithms
        # need to update so that the data being encrypted is more than a single integer
        self.value = self.generate_hash_str(vote_obj)
        self.leftChild = None       # pointer to left child node
        self.rightChild = None      # pointer to right child node
        self.parentNode = None      # pointer to parent node
        self.siblingNode = None     # pointer to sibling node
        self.side = None            # whether this node is left or right

    def print_node(self):
        print "Left Child %s, Right Child %s, Parent Node %s, Sibling %s, Side %s" % (self.leftChild, self.rightChild, self.parentNode, self.siblingNode, self.side)

    def generate_hash_str(self, vote_obj):
        vote_str = str(vote_obj.id) + str(vote_obj.choice)
        # print 'vote stringified', vote_str
        random_hex_str = ''.join(random.choice(string.hexdigits) for i in range(10))
        # print 'random hex', random_hex_str
        user_pub_key = vote_obj.public_key
        # print 'user public', user_pub_key
        output_str = hash_function(vote_str + random_hex_str + user_pub_key).hexdigest()
        print 'vote hash', output_str
        return output_str
