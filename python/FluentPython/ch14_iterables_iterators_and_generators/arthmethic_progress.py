class ArthmeticProgression:

    def __init__(self, begin, step ,end =None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        while forever or result < self.end:
            result += self.step
            yield result

if __name__ == '__main__':
    arthmethic = ArthmeticProgression(1, 0.5, 10)

    for i in iter(arthmethic):
        print(i)