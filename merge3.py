list_of_dictionaries = [{
    'name': 'Name1',
    'age': 15
}, {
    'name': 'Name2',
    'age': 40
}, {
    'name': 'Name3',
    'age': 30
}]
# List is sorted by 'name' and 'age' key
SortByAgeAndName = sorted(list_of_dictionaries,
                          key=lambda k: (k['age'], k['name']))

print('Sorted By Name and age: ', SortByAgeAndName, '\n')
# [{'name': 'Bart', 'age': 10}, {'name': 'Milhouse', 'age': 10}, {'name': 'Homer', 'age': 39}]

# List is sorted by only 'age' key
SortByAge = sorted(list_of_dictionaries, key=lambda k: (k['age']))

print('Sorted By age: ', SortByAge)
# [{'name': 'Milhouse', 'age': 10}, {'name': 'Bart', 'age': 10}, {'name': 'Homer', 'age': 39}]