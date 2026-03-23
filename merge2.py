def Merge_2_dict(dict_1, dict_2):
    d = {**dict_1, **dict_2} # Using ** to do the same thing
    return d
    
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'d': 3, 'c': 4}
dict_3 = Merge_2_dict(dict_1, dict_2) # Here dict_3 becomes the third dict

print(dict_3) # Print our new dictionary