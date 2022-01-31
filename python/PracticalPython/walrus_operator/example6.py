cities = ['Seol', 'Busan', 'DeaJeon', 'Yongnin', 'Seongnam']

if any((target_city := city).startswith('S') for city in cities):
    print("The city starts with S is", target_city)
else:
    print("Target city not found.")