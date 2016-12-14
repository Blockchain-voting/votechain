class Vote:
    def __init__(self, e_id, choice, public_key):
        self.id = int(e_id)
        self.choice = choice
        self.public_key = public_key
