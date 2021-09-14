class Averager():
    
    def __init__(self) :
        self.series = []

    def __call__(self, new_value) :
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

def make_avg():
    series = []
    
    def avg(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    
    return avg

def advanced_avg():
    total = 0
    count = 0 

    def avg(new_value): 
        nonlocal total, count
        count += 1
        total += new_value
        return total/count
    
    return avg

        

        

if __name__ == '__main__':
    avg_class = Averager()
    print(avg_class(10))
    print(avg_class(11))

    avg_func = make_avg()
    print(avg_func(20))
    print(avg_func(21))

    avg_adv = advanced_avg()
    print(avg_adv(30))
    print(avg_adv(31))
    