class Vote:
    def __init__(self, e_id, choice, signature):
        self.id = int(e_id) - 1 #accounting for zero based index
        self.choice = int(choice)
        self.signature = signature
