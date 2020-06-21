#!/usr/bin/env python3

my_values = [3,4,5,"test",98,8,8.9,"last_value"]
print(f"Printing values from List [{my_values}]")
print(f"Printing type of my_values [{type(my_values)}]")

'''
list -> []
tuple -> ()
dictionary -> {} with key value pair
set -> {}
'''


################################################################
#### List data structure
################################################################

my_list = []
print(f"Converting empty list to Boolean expected :: [False] :: is :: [{bool(my_list)}]")
my_list = [1,2,3,4,5,6,7,5,"python"]
print(f"Converting list to Boolean expected :: [True] :: is :: [{bool(my_list)}]")

#### accessing list on diffrent ways
print(my_list)
print(my_list[:])
print(my_list[2:])
print(my_list[-1])
print(my_list[-1][-2:])
my_values[-1] = "Python 3.7"
print(my_values[-1])

### getting list operations
print(dir(my_list))

print(f"Printing value index for first 5 [{my_list.index(5)}]")
print(f"Printing value index for next 5 [{my_list.index(5,5)}]")
index_of_5 = my_list.index(5)
next_index_of_5 = my_list.index(5, index_of_5 + 1)
print(f"Printing value index for index of 5 [{index_of_5}] ::> [{my_list[index_of_5]}]")
print(f"Printing value index for next index of 5 [{next_index_of_5}] ::> [{my_list[next_index_of_5]}]")
print(f"Printing my_list values [{my_values}]")

print(f"Printing occurrences of value [5] in my_values [{my_list.count(5)}] on index [{index_of_5}] and next index [{next_index_of_5}]")

print(f"Clearing in List of my_values values [{my_values}] and after clear we have [{my_values.clear()}]")
print(f"Printing List of my_values after clean method [{my_values}]")

### Copy lists
my_list_new = my_list
print(f"Printing copied List of my_values [{my_list}] to new List [{my_list_new}]")
my_list_new2 = my_list.copy()
print(f"Printing copied List of my_values.copy() [{my_list}] to new List [{my_list_new2}]")
##### above two methods do same thing but
# first method copy memory reference to it and second method 'copy' create new one.

print(f"Printing id of my_list [{id(my_list)}]")
print(f"Printing id of my_list_new [{id(my_list_new)}]")
print(f"Printing id of my_list_new2 [{id(my_list_new2)}]")
#### whats that mean if we modify the list of my_list 2nd list will also be modified
print(f"Printing last value of my_list [{my_list[-1]}]")
my_list[-1] = "Auggie changed"
print(f"Printing last value of my_list [{my_list[-1]}] and last value of my_list_new [{my_list_new[-1]}] they same as they pointing to same reference in memory")
print(f"Printing last value of my_list_new2 which been copied via copy() method [{my_list_new2[-1]}]")

### append() and insert() methods
my_list.append("new_last_element")
print(f"Printing values of my_list [{my_list}] and values of my_list_new [{my_list_new}] they will be same as they pointing to same reference in memory")
my_list_new.insert(3, "next_object_of_index_3")
print(f"Printing values of my_list [{my_list}] and values of my_list_new [{my_list_new}] they will be same as they pointing to same reference in memory")
print(f"Printing values of my_list_new2 [{my_list_new2}] as its diffrent List will stay unchanged")
### so better to use copy instead assignment

### differences between append and extend
### use extend to extend list be list

my_list.insert(-1,my_list_new2)
print(f"Printing values of my_list [{my_list}] after operation insert")

my_list.extend(my_list_new2)
print(f"Printing values of my_list [{my_list}] after operation extend")

my_list.extend("678")
print(f"Printing values of my_list [{my_list}] after operation extend with value")
### extend takes iterable object

my_list.remove(my_list_new2)
print(f"Printing values of my_list [{my_list}] after operation remove [{my_list_new2}]")
last_element = my_list.pop()
print(f"Printing values of my_list [{my_list}] after operation pop which removes last element [{last_element}]")
element = my_list.pop(9)
print(f"Printing values of my_list [{my_list}] after operation pop which removes element of index [9] [{element}]")

reverse = my_list.reverse()
print(f"Printing values of my_list [{my_list}] after operation reverse [{reverse}]")

my_list_to_sort=[3,9,0,1,4,6,11,46,91,4]
print(f"Printing values of my_list_to_sort [{my_list_to_sort}]")
sort = my_list_to_sort.sort()
print(f"Printing values of my_list_to_sort [{my_list_to_sort}] after operation sort [{sort}]")
reverse_sort = my_list_to_sort.sort(reverse=True)
print(f"Printing values of my_list_to_sort [{my_list_to_sort}] after operation reverse sort [{reverse_sort}]")


#################################
# tuple
##

### Define Tuple
empty_tuple = ()
my_tuple = (4,1,8)
print(f"Printing Tuples my_tuple :: [{my_tuple}] and empty_tuple :: [{empty_tuple}]")
print(f"Printing Tuples my_tuple as Boolean as its not empty tuple [{bool(my_tuple)}] == True")
print(f"Printing Tuples empty_tuple as Boolean as its empty tuple [{bool(empty_tuple)}] == False")
print(f"Printing Tuples operations \n{dir(my_tuple)}")

my_tuple_new = (4,1,4,[3,7,0],8,9.9)
print(f"Printing Tuples my_tuple_new :: [{my_tuple_new}]")
index = 2
print(f"Printing Tuples my_tuple_new value per index [{index}] :: [{my_tuple_new[index]}]")
index = 3
print(f"Printing Tuples my_tuple_new value per index [{index}] :: [{my_tuple_new[index]}] and last element from lits in Tuple my_tuple_new :: [{my_tuple_new[index][-1]}]")


my_tuple = 3,4,4,8
print(f"Printing Tuples my_tuple [{my_tuple}] and type [{type(my_tuple)}]")

#################################
#### dictionaries

my_dict = {}
print(f"Printing Dictionary my_dict [{my_dict}] and type of it [{type(my_dict)}]")
print(f"Printing operations we can perform on dictionaries \n{dir(my_dict)}")
print(f"Printing Boolean operations on dictionaries [{bool(my_dict)}] if Empty equal [False]")
my_dict = {'fruits': 'apple', 'vegetable': 'potato', 1 : 'one', 'two': 2, 'list': [1,2,3,4,5]}
print(f"Printing Dictionary my_dict [{my_dict}]")
print(f"Printing Boolean operation for not empty Dictionary [{bool(my_dict)}] if not Empty equal to [True]")
print(f"Printing values of my_dict [{my_dict}] accessed via key [fruits] : [{my_dict['fruits']}]")
print(f"Printing values of my_dict [{my_dict}] accessed via key [two] and get() method [{my_dict.get('two')}]")
my_dict['three'] = 3
print(f"Printing values of my_dict [{my_dict}] after adding key [three] [{my_dict.get('three')}]")
my_dict['vegetable'] = 'onion'
print(f"Printing values of my_dict [{my_dict}] after updating key [vegetable] [{my_dict.get('vegetable')}]")
print(f"Printing values of my_dict all keys: [{my_dict.keys()}]")
print(f"Printing values of my_dict all values: [{my_dict.values()}]")
print(f"Printing values of my_dict all items: [{my_dict.items()}]")
my_dict2 = {'four':4,'five':5}
print(f"Adding my_dict [{my_dict}] to my_dict2 [{my_dict2}]")
my_dict.update(my_dict2)
print(f"with update() method [{my_dict}]")
print(f"Removing value base on key [vegetable]:[{my_dict.pop('vegetable')}] give us [{my_dict}]")
print(f"Printing my_dict after using popitem() method which will remove item [{my_dict.popitem()}] my_dict = [{my_dict}]")
print(f"Printing my_dict after using popitem() method which will remove item [{my_dict.popitem()}] my_dict = [{my_dict}]")
keys = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict3 = dict.fromkeys(keys)
print(f"Printing my_dict3 after creating dictionary from list of keys [{keys}] >>>> [{my_dict3}]")
my_dict3['a'] = 'hello world'
print(f"Printing my_dict3 after updating key 'a' value [{my_dict3.get('a')}] and dictionary [{my_dict3}]")
print(f"Printing my_dict [{my_dict}] and updating key:value if key doesn't exist 'one':111 [{my_dict.setdefault('one',1)}] \nnew item added [{my_dict}]\n[{my_dict.setdefault(1,'oneOnOne')}] no change expected [{my_dict}]")


################################
#### Sets

my_set_hm = {3,4,5,6,7,40,5,8,1,0.3,0}
my_set = {4,5,7,2,7,0}
print(f"Printing Set [{my_set}] with order sequence and no duplicates.")
print(f"Printing Set [{my_set}] with Boolean [{bool(my_set)}] should be [True]")
empty_set = {}
print(f"Printing Set empty_set [{empty_set}] with Boolean [{bool(empty_set)}] should be [False]")
print(f"Printing Set [{my_set}] operations {dir(my_set)}")
empty_set2 = set({})
print(f"Printing empty_set2 [{empty_set2}]")
my_list = [2,0,4,5,1,4,9,23,99]
empty_set2 = set(my_list)
print(f"Printing empty_set2 [{empty_set2}]")
print(f"Printing my_set [{my_set}] union with my_set_hm [{my_set_hm}] union is [{my_set.union(my_set_hm)}]")
print(f"Printing my_set [{my_set}] intersection with my_set_hm [{my_set_hm}] intersection is [{my_set.intersection(my_set_hm)}]")
print(f"Printing my_set [{my_set}] difference with my_set_hm [{my_set_hm}] difference is [{my_set.difference(my_set_hm)}]")