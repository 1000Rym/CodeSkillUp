class Demo:
    count = 10
    @classmethod
    def classmeth(cls,num):
        return  cls.count + num

    @staticmethod
    def staticmeth(num):
        return Demo.count +num # The line of code is not clean.
    

if __name__ == "__main__":
    print(Demo.classmeth(2))
    print(Demo.staticmeth(3))