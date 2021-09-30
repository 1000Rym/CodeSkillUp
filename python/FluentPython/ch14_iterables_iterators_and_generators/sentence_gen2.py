import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        #self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        """
        Use re.find method to save memory.
        """
        for match in RE_WORD.finditer(self.text):
            yield match.group() 

if __name__ == '__main__':
    s = Sentence("Hello world, I hate mosquoto!")
    iter1 = iter(s)
    iter2 = iter(s)

    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter2))
