import array

nums = array.array('h', [-2,-1, 0,1,2])
memv = memoryview(nums)
memv[0] = 0
print(memv.tolist())

memv2 = memv.cast('B')
print(memv2.tolist())