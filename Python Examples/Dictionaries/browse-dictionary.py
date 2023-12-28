#LOOP THROUGH KEYS AND VALUES
for key, value in my_dictionary.items():
    print(f'key: {key}, Value: {value}')
    
#TRAVEL ONLY KEYS OR VALUES:
for key in my_dictionary.keys():
    print(f'key: {key}')
for value in my_dictionary.value():
    print(f'Value: {value}')