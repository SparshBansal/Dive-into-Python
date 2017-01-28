# ==================== LIST DATA CONTAINER =========================
a_list = [2,'three' , 4.0]

# print a List
print a_list

# Slicing a List - a_list[a : b] -- a inclusive and b exclusive
print a_list[0:2]

# ******* Add single items to the List **************

a_list.append('five')
print a_list

# insert at a given index list.insert(idx , element)
a_list.insert(0 , 'first')
print a_list

# ******** Add mulitple items to a List *************

# using + operator returns a new list
b_list = a_list + ['use' , '+' , 'operator']
print a_list
# print b_list

a_list.extend([6.0,7,'eight'])
print a_list

# ******** Remove items from a list ****************

# remove the last item from the List
a_list.pop()
print a_list

# remove an element from the given index
del a_list[4]
print a_list

# remove a given element from the List
a_list.remove(6.0)
print a_list

# ********* Finding elements in a list *************

# check if an element exists in the list
print 'three' in a_list

# get the index of an element -- throws exception if element not found
print a_list.index('three')


# =============== TUPLES DATA CONTAINER ==========================

a_tuple = (1,'two' , 3)

print a_tuple

# tuples are immutable therefore we cannot add or remove elements from tuples

# ************* Slicing a tuple **********************
# generates a new tuple -- immutable
b_tuple = a_tuple[1:2]

print a_tuple
# print b_tuple

# ************** Finding elements in a tuple *********

# check if an element exists in the tuple
print 3 in a_tuple

# get the index of an element -- throws exception if element not found
print a_tuple.index(3)

# Tuples can be used to assign multiple values at once -- can be used to return
# multiple values at once from a function
(x,y,z) = a_tuple
print x,y,z

# =============== SETS DATA CONTAINER ==========================

b_set = {'elements' , 'may' , 'also' , 1,2,3 }

# Set from a list
a_set = set(a_list)
print a_set

# Empty Set
empty_set = set()
print empty_set

# ********** Add elements to set ************

# Single item
empty_set.add(4)
print empty_set

# Multiple items -- update method can also take lists etc
empty_set.update({2,4,'six'})
print empty_set

# ***********Remove elements from sets *******

# discard and remove

# discard -- doesnt raise exceptions
empty_set.discard(4)
print empty_set

# remove -- raises an exception if the element is not found
empty_set.remove('six')
print empty_set

# pop removes an arbitrary element from the set
empty_set.pop()
print empty_set

# ********** Finding elements in set *********
print 'six' in empty_set


# ********* Set operations *******************
empty_set.update({2,4,'six'})


# Union -- symmetric operation ie. a.union(b) = b.union(a)
u_set = a_set.union(empty_set)
print u_set

# Intersection -- symmetric
i_set = a_set.intersection(empty_set)
print i_set

# difference -- asymmetric
d_set = a_set.difference(empty_set)
print d_set

# issubset
print empty_set.issubset(a_set)

# issuperset
print empty_set.issuperset(a_set)


# ==================== DICTIONARY DATA CONTAINER =========================

a_dictionary = {'server' : 'http://localhost:3000' ,
                'database' : 'http://localhost:27017'}

print a_dictionary

# Access elements
print a_dictionary['server']

# Modifying elements of dictionary
a_dictionary['server'] = 'Not available. Sorry'
print a_dictionary

# Adding items to dictionary
a_dictionary['user'] = 'google'
print a_dictionary

# Dictionaries may have mixed values
a_dictionary['list'] = [2,3,'four']
print a_dictionary

# Removing elements from a dictionary
del a_dictionary['list']
print a_dictionary
