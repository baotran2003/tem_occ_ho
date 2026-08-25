
if __name__ == "__main__":
    s1 = {"a", "b", "c"}

    # 1. add
    s1.add("d")
    print("Method add:", s1)

    #2. remove: return KeyError if x doesn't exist
    s1.remove("d")
    print("Method remove: ", s1)

    #3. discard
    s1.discard("t")
    print("Method discard: ", s1)

    #4. get element
    my_set = {10, 20, 30, 40, 50}
    item = my_set.pop()
    print(item)
    print(my_set)

    #5. check x in s
    my_set_1 = {1, 2, 3, "apple", "banana"}
    print("apple" in my_set_1)

    #6. update: add elements of a list to a set, changing origin set, doesn't return new set
    thisset = {"apple", "banana", "cherry"}
    mylist = ["kiwi", "orange"]
    thisset.update(mylist)
    print(thisset)

    # 2. union fuction: combines to sets and return a new set with all unique elements or Use |
    s2 = {"b", "c", "d", "e"}
    print("Method union:", s1.union(s2))

    # 3. Intersection: returns a new set containing elements that are common to both sets. or use &
    print("Method Intersection: ", s1.intersection(s2))
    #3.1 Intersection_update: change origin set instead of returning new set
    s1.intersection_update(s2)
    print("Method Intersection_update: ", s1)

    #4. Different function: return a set containing elements that are in the first set but not in the second or Use -
    print("Method different: ", s1.difference(s2))

    #5. symmetric_difference method: keep only element that are NOT present in both sets
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}

    set3 = set1.symmetric_difference(set2)

    print("symmetric_difference method: ", set3)

    #5. Clear function: removes all elements from a set, leaving it empty.
    s3 = {1, 4, 5}
    print("Method Clear:", s3.clear())