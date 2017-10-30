class Buckets(object):
    def __init__(self, length, default):
        self.default = default
        self.buckets = [default] * length

    def add(self, index, element):
        self.buckets[index].append(element)

    def find(self, index, element):
        return element in self.buckets[index]

    def clear(self, index):
        self.buckets[index] = self.default
