
key_range = range(1, 50)
keys = []
for key in key_range: 
    keys.append(key) 

my_dict2 = dict.fromkeys(keys, 0)

for key in my_dict2.keys(): 
    if key % 2 == 0:  
        value = key + 1 
        my_dict2[key] = value
    elif key % 7 == 0: 
        value = key - 1
        my_dict2[key] = value
    else: 
        value = key
        my_dict2[key] = value
    if key % 2 == 0 and key % 7 == 0: 
        value = key * 2
        my_dict2[key] = value
    else: 
        value = key 
        my_dict2[key] = value


print(my_dict2) 
