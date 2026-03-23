def Merge_2_Dict(dict1, dict2):
	return(dict1.update(dict2)) # dict1 gets changed 
    
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
 
# Merge these 2 dicts
Merge_2_Dict(dict1, dict2)

# Here our dict1 gets changed and no new dict is created 
print(dict2)