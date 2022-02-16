import json

def main():
    # Multi-line string (JSON)
    json_str = """{
        "Name": "Benedict Thousand",
        "Contact Number": 2211692,
        "Email": "daramgworld@gmail.com",
        "Hobbies":["Gaming", "Reading", "Hiking"]
        }"""
    
    # json.loads(): Convert Json string to python dictionary
    converted_dict = json.loads(json_str)
    for key, value in converted_dict.items():
        print("key:{}, value:{}".format(key,value))
        
    # json.load(file): Open from a json file.
    json_file = open('data.json')
    data = json.load(json_file)
    employees = data['employees']
    for employee in employees:
        for key, value in employee.items():
            print('{}: {}'.format(key, value), end=" ")
        print()
        
    # json.dump(): covert dict to json
    dict_values = {(1, 2, 3):'Hello', 2:'to',
                    3:'the', 4:'world',
                    5:'you', 6:float('nan')}
    
    # skip keys to skip invalidate type key
    # allow_nan to sport nan
    # add indent for pretty print(add indentation in front of lines.)
    json_str2 = json.dumps(dict_values,
                         skipkeys = True,
                         allow_nan = True,
                         indent = 10)
    
    print('Serialized json_str2:{}'.format(json_str2))
    
    # add separators to change item separator to . and key value sparators to =.
    # add sort_keys to sort the keys in serialized string.
    dict_values = {'c':'Me', 'b':'Like',
            'a':'Books'}

    json_str3 = json.dumps(dict_values, 
                           indent= 10,
                           separators = ('. ', "="), 
                           sort_keys=True)
    print('Serialized json_str3:{}'.format(json_str3))
    

if __name__ == '__main__':
    main()