class DictHash:

    def __init__(self):
        self.dict = dict()

    def store(self, nyckel, data):
        self.dict[nyckel] = data

    def search(self, nyckel):
        return self.dict[nyckel]
