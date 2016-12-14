class Vote:
    def __init__(self, e_id, choice, public_key):
        self.id = int(e_id) - 1 #accounting for zero based index
        self.choice = int(choice)
        self.public_key = public_key
