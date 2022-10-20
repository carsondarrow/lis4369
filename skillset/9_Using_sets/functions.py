def get_requirements():
    print("\nPython Sets - like mathematical sets!")
    print("Program Requirements:")
    print("1. Sets (Python data structure): mutable, heterogeneous, unordered sequence of elements, *but* cannot hold duplicate values.")
    print("2. Sets are mutable/changeable-- that is, can insert, update, delete.")
    print("3. While sets are mutable/changeable, they *cannot* contain other mutable items like list, set, or dictionary--")
    print("\tthat is, elements contained in set must be immutable.")
    print("4. Also, since sets are unordered, cannot use indexing (or, slicing) to access, update, or delete elements.")
    print("5. Two methods to create sets:")
    print("\ta. Create set using curly brackets \{set\}: my_set = \{1, 3.14, 2.0, 'four', 'Five'\}")
    print("\tb. Create set using set() function: my_set = set(<iterable>)")
    print("\tExamples:")
    print("\tmy_set1 = set([1, 3.14, 2.0, 'four', 'Five']) # set with list")
    print("\tmy_set2 = set([1, 3.14, 2.0, 'four', 'Five')) #set with tuple")
    print("5. Note: An \"iterable\" is *any* object, which can be iterated over-- that is, lists, tuples, or even strings.")
    print("6. Create a program that mirrors the following IPO (input/process/output) format.")

def using_sets():
    my_set = {1, 3.14, 2.0, 'four', 'Five'}
    print("Print my_set created using curly brackets:")
    print(my_set)

    print("\nPrint type of my set:")
    print(type(my_set))

    my_set1 = set([1, 3.14, 2.0, 'four', 'Five'])
    print("\nPrint my_set1 created using set() function with list:")
    print(my_set1)

    print("\nPrint type of my_set1:")
    print(type(my_set1))

    my_set2 = set((1, 3.14, 2.0, 'four', 'Five'))
    print("\nPrint my_set2 created using set() function with tuple:")
    print(my_set2)

    print("\nPrint type of my_set2:")
    print(type(my_set2))

    print("\nLength of my_set:")
    print(len(my_set))

    print("\nDiscard 'four'")
    my_set.discard('four')
    print(my_set)

    print("\nRemove 'Five':")
    my_set.remove('Five')
    print(my_set)

    print("\nLength of my_set:")
    print(len(my_set))

    print("\nAdd element to set (4) using add() method:")
    my_set.add(4)
    print(my_set)

    print("\nLength of my_set:")
    print(len(my_set))

    print("\nDisplay minimum number:")
    print(min(my_set))

    print("\nDisplay maximum number:")
    print(max(my_set))

    print("\nDisplay sum of numbers:")
    print(sum(my_set))

    print("\nDelete all set elements:")
    my_set.clear()
    print(my_set)

    print("\nLength of my_set:")
    print(len(my_set))