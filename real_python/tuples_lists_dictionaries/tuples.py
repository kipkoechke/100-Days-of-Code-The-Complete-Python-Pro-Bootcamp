#!/usr/bin/env python3

my_first_tuple = (1, 2, 3)

empty_tuple = ()

tuple_with_single_element = (1,)

print(len(my_first_tuple))

# Tuples Support Indexing and Slicing
name = ("D", "a", "v", "i", "d")
print(name[1])

print(name[2:4])

# Tuples Are Iterable
for n in name:
    print(n.upper())


# Returning Multiple Values From a Function
def adder_subtractor(num1, num2):
    return (num1 + num2, num1 - num2)


print(adder_subtractor(3, 2))
