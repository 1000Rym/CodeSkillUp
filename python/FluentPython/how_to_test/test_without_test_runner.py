"""
A Normal test way withtout test runner.
"""
def test_sum_list():
    assert sum([1,2,3]) == 6, "Shoule be 6"

def test_sum_tuple():
    assert sum((1,2,2)) == 6, "should be 6"

if __name__ == '__main__':
    test_sum_list()
    test_sum_tuple()
    print("Test Finished")