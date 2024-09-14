# Functions that work with sets & set methods


# Functions look like this:
# some_func(a)

# Functions are not bound to a type, for example the length (len) function
# works fine with strings, lists & tuples. 

# Functions don't just accept anything as the input though, for example if the length function
# was given an integer or a float, it would crash and raise a 'TypeError'.

# In this reference code I list all the most commonly used functions that can take a set as an input.
# There will be a fair amount of similarity for how the functions work here, to how they worked with lists/tuples.

# -all-
# Returns True if everything in the sethas a boolean value of True, otherwise False.
binary_nums = {1, 0, 1, 1, 0}
binary_nums_v2 = {1, 1, 1, 1}
print(all(binary_nums)) # False, because there are 0's in the list
print(all(binary_nums_v2), "\n") # True, because everything in the list has a boolean value of True!


# -any-
# Returns True if anything in the set has a boolean value of True, otherwise False.
strs_set = {"", 55, 22}
strs_set_v2 = {"", 0, False}
print(any(strs_set))  # True, because 2 of the items have a boolean value of True
print(any(strs_set_v2), "\n") # False, because nothing in the set is True


# -bool-
# Returns either True or False. The only set to return False is an empty one
print(bool(set())) # False
print(bool({1,2,3}), "\n") # True

# -dir-
# Returns all the attributes a set has (All the things you can do with it!).
# print(dir(set))
# Commented these out because they #print a lot!


# -enumerate-
# This returns a collection of Tuples where each character of the sequence is paired
# with its index. We usually use this when iterating over strings (See Section 14 - Looping)
abcs = {"A", "B", "C", "D"}
enumerated_set = list(enumerate(abcs))
print(enumerated_set, "\n")


# -help-
# Returns some quick scrollable documentation for the string.
# Useful if you dont fancy looking it up online!
# #print(help(set)) # Commented out because it prints a lot!


# -isinstance-
# Returns True if the first argument 'is' a member of the second argument, False otherwise.
print(isinstance({6,5,4}, set)) # True, because {6, 5, 4} is a set.
print(isinstance({3, 2, 1}, list), "\n") # False, because {3, 2, 1}, is a set.


# -len-
# Returns the length of the List/Tuple
names = {"Alex", "Chris", "Sue", "Alison"}
print(len(names))


# -list-
# Converts its input to a list, in this case it changes a takes the set and returns a list.
a_set = {99,88,77,66}
now_a_list = list(a_set)
print(now_a_list, "\n")


# -map-
# Applies a function to each item in a sequence, and is often passed into a list/tuple.
# In this example, each country in the set is passed to the len() function, then the results are stored in a list.
# In this instance we only have {5,6} in the set as the other 5 and 6 are removed.
countries = ["Spain", "France", "Italy", "Sweden"]
length_countries = set(map(len, countries))
print(length_countries, "\n")


# -max-
# Returns the largest element of the set (numerically or alphabetically).
print(max({1,2,3,4,5})) # Returns 5


# -min-
# Returns the smallest element of the set (numerically or alphabetically).
print(min({1,2,3,4,5})) # Returns 1


# -sorted-
# Returns a sorted list of the input sequence. Ensure the elements of the set are either
# all numerical, or all strings (or any valid type), or a TypeError could be raised.
# Remember that sorted() returns a list, but it will happily accept a set as its input.
nums = {5,4,5,6,8,9,1,2,-1}
print(sorted(nums))

# Or you can sort in reverse
print(sorted(nums, reverse=True), "\n")


# -sum-
# Returns the sum of the input sequence.
# Dont forget that the duplicates get removed!
some_nums = {20,20,20,10,5,5,10,8,2}
print(sum(some_nums))


# -tuple-
# Converts its input to a tuple
this_is_a_set = {"Turing", "Lovelace", "Babbbage"}
this_is_a_tuple = tuple(this_is_a_set)
print(this_is_a_tuple, "\n")


# -type-
# Returns the type of its input. Very useful for checking!
print("This is a set", type({1,1,1}), "\n")


# -zip-
# Zips together n sequences (such as a set) and returns tuples of the zipped members.
# In this instance i've passed them to the set function to return a set of tuples.
# Note: if one input is longer than the other, then the 'zipping' stops at the end of the shortest one.
evens = {2,4,6,8,10}
odds = {1,3,5,7,9}
print(set(zip(odds, evens)), "\n")



#######################


# Methods look like this
# primes.some_method()

# Suppose 'primes' is a set, then 'some_method' is a function that belongs to the set type,

# Another easy way of telling apart a method and a function is that methods have dots between them and the variable.
# Some methods take additional inputs, whilst some do not. In this reference code I have included all set methods.

# I've roughly arranged these into sections, and added newline characters to break them up.

# -- Line : Adding items to sets.
# -- Line : Removing items from sets.
# -- Line : Subset, Superset & Disjoint checking.
# -- Line : Removing items from sets.
# -- Line : Union, Intersection, Difference & Symmetric Difference Operations.



# -add-
# Adds a single item to the set.
# This is an in-place operation, so it directly changes the set, without returning anything.
set_a = {1,2,3}
print("Before Adding: ", set_a)
set_a.add("X")
print("After Adding: ", set_a, "\n")


# -update-
# Adds multiple items from an iterable to a set. (Similar to list.extend())
# This is an in-place operation, so it directly changes the set, without returning anything.
set_a = {"a", "b", "c"}
print("Before Updating: ", set_a)
set_a.update({"S", "D"})
print("After Updating: ", set_a, "\n")


# -copy-
# Whilst not strictly 'adding' to a set, i've added it here as it seems the most fitting!
# This method returns a new set, with a copy of the elements from another.
copy_of_a = set_a.copy()
print("A copy of set_a: ", copy_of_a, "\n")



# -isdisjoint-
# Returns True if set_a and set_b are disjoint (Their intersection is empty).
set_a = {4, 5, 6, 3}
set_b = {10, -1, 0}
print("Is disjoint: ", set_a.isdisjoint(set_b)) # True because there are no overlapping elements.
print("Is not disjoint: ", {10,20}.isdisjoint({10,45}), "\n") # False because 10 is in both.


# -issubset-
# Returns True if set_a is a subset of set_b (All items from set_a are also in set_b).
set_a = {10,20,30}
set_b = {0, 10, 20, 30, 40}
print("Is subset:", set_a.issubset(set_b)) # True because all of set_a is in set_b.
print("Is not a subset:", {10,20}.issubset({10,30,40}), "\n") # False because 20 is not in the second set.


# -issuperset-
# Returns True if set_a is a superset of set_b (All elements from set_b are in set_a).
set_a = {-1, 0, 1, 2}
set_b = {-1, 2}
print("Is superset: ", set_a.issuperset(set_b)) # True because all of set_b is in set_a.
print("Is not a superset: ", {1,2,8}.issuperset({10,2}), "\n") # False, because 10 is not in the first set.


# -pop-
# Removes and returns a random item from the set.
# This is an in-place operation, so it directly changes the set.
primes = {7,11,13,5}
print("Before Popping: ", primes)
print("Popped Element: ", primes.pop())
print("After Popping: ", primes, "\n")


# -remove-
# Removes a single item from the set, raising a KeyError if the item does not exist in the set.
# This is an in-place operation, so it directly changes the set.
primes = {7,11,13,5}
print("Before Removing: ", primes)
primes.remove(7)
# primes.remove(17) # Raises a KeyError.
print("After Removing: ", primes, "\n")


# -discard-
# Removes a single item from the set, and will NOT raise a KeyError if the item doesn't exist.
# This is an in-place operation, so it directly changes the set.
primes = {7,11,13,5}
print("Before Discarding: ", primes)
primes.discard(5)
primes.discard(17) # Doesn't raise a KeyError this time.
print("After Discarding: ", primes, "\n")


# -clear-
# Clears all items from a set, leaving it empty.
# This is an in-place operation, so it directly changes the set.
primes = {19, 23, 5}
print("Before Clearing: ", primes)
primes.clear()
print("After Clearing: ", primes, "\n")


# -difference-
# Returns a new set which is the difference of set_one and set_two
set_one = {10,9,8,7}
set_two = {6,10,9,0}
set_diff = set_one.difference(set_two) # 10, 9, 8, 7, take away 6, 10, 9, 0. We are left with {8,7}
print("Difference", set_diff)
print("Difference with operator:", set_one - set_two, "\n") # The minus operator can also be used.


# -difference_update-
# Similar to difference, except this time it updates set_one in place to contain the difference
# of set_one and set_two.
set_one = {10,9,8,7}
set_two = {6,10,9,0}
print("Before difference update:", set_one)
set_one.difference_update(set_two)
print("After difference update:", set_one, "\n")


# -intersection-
# Returns a new set which is the intersection of set_one and set_two
set_one = {10,9,8,7}
set_two = {6,10,9,0}
set_inter = set_one.intersection(set_two) # Gives only elements that exist in both, so {9, 10}.
print("Intersection: ", set_inter)
print("Intersection with operator:", set_one & set_two, "\n") # The ampersand operator can also be used.


# -intersection_update-
# Similar to intersection, except this time it updates set_one in place to contain the intersection
# of set_one and set_two.
set_one = {10,9,8,7}
set_two = {6,10,9,0}
print("Before intersection update:", set_one)
set_one.intersection_update(set_two)
print("After intersection update:", set_one, "\n")


# -symmetric_difference-
# Returns a new set which is the symmetric difference of set_one and set_two
set_one = {10,9,8,7}
set_two = {6,10,9,0}
set_sym_diff = set_one.symmetric_difference(set_two) # Gives items that exist in one of the sets but not both, so {0, 6, 7, 8}
print("Symmetric difference: ", set_sym_diff)
print("Symmetric difference with operator: ", set_one ^ set_two, "\n") # The symmetric difference operator can also be used.


# -symmetric_difference_update-
# Similar to symmetric difference, except this time it updates set_one in place to contain the symmetric difference
# of set_one and set_two.
set_one = {10,9,8,7}
set_two = {6,10,9,0}
print("Before symmetric difference update:", set_one)
set_one.symmetric_difference_update(set_two)
print("After symmetric difference update:", set_one, "\n")


# -union-
# Returns a new set which is the union of set_one and set_two
set_one = {10,9,8,7}
set_two = {6,10,9,0}
set_union = set_one.union(set_two) # A combination of all elements from both sets.
print("Set union: ", set_union)
print("Set union with operator: ", set_one | set_two) # The pipe operator can also be used.