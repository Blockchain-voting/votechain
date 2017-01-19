from hashlib import sha256
import string
import random
hash_function = sha256

class Node:
    def __init__(self, vote_obj):
        # hashes vote data with sha256 algorithms
        # need to update so that the data being encrypted is more than a single integer
        self.vote = vote_obj
        self.value = self.generate_hash_str(vote_obj)
        self.left_child = None       # pointer to left child node
        self.right_child = None      # pointer to right child node
        self.parent_node = None      # pointer to parent node
        self.side = None            # whether this node is left or right

    def empty(self):
        if self.left_child == None and self.right_child == None:
            return True
        else:
            return False

    def empty_left(self):
        if self.left_child == None:
            return True
        else:
            return False

    def empty_right(self):
        if self.right_child == None:
            return True
        else:
            return False

    # getters
    def get_children(self):
        return self.left_child, self.right_child

    def get_left_children(self):
        return self.left_child

    def get_right_children(self):
        return self.right_child

    def get_parent(self, new_parent):
        return self.parent_node

    # setters
    def set_left_child(self, new_child):
        self.left_child = new_child

    def set_right_child(self, new_child):
        self.right_child = new_child

    def set_parent(self, new_parent):
        self.parent_node = new_parent

    def print_node(self):
        print "Left Child %s, Right Child %s, Parent Node %s, Vote Value %s" % (self.left_child, self.right_child, self.parent_node, self.vote.choice)

    def generate_hash_str(self, vote_obj):
        vote_str = str(vote_obj.id) + str(vote_obj.choice)
        # print 'vote stringified', vote_str
        random_hex_str = ''.join(random.choice(string.hexdigits) for i in range(10))
        # print 'random hex', random_hex_str
        user_pub_key = vote_obj.signature
        # print 'user public', user_pub_key
        output_str = hash_function(vote_str + random_hex_str + user_pub_key).hexdigest()
        # print 'vote hash', output_str
        return output_str
