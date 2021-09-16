import copy

class Bus: 
    def __init__(self, members=None):
        if members is None:
            self.members = []
        else:
            self.members = list(members)

    def pick(self, member):
        self.members.append(member)
    
    def drop(self, member):
        self.members.remove(member)

    def __call__(self):
        return self.members


if __name__ == '__main__':
    bus1 = Bus()
    bus1.pick("Lin")
    bus1.pick("Minna")
    bus1.pick("Alice")
    print(bus1())

    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(f'bus1:{id(bus1())}')
    print(f'bus2:{id(bus2())}')
    print(f'bus3:{id(bus3())}')