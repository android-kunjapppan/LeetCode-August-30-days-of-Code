class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.it = combinations(characters, combinationLength)

        self.buffer = next(self.it, None)

        

    def next(self):

        res = ''.join(self.buffer)

        self.buffer = next(self.it, None)

        return res

        

    def hasNext(self):

        return self.buffer is not None


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
