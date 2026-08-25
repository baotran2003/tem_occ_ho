if __name__ == "__main__":
    #1. remove
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    # car.clear()
    # print("remove function: ", car)

    #2. copy
    x = car.copy()
    x["age"] = 21
    print("Copy function: ", x)
    print("Car Copy function: ", car)

    #3. fromKeys:
    x = ('key1', 'key2', 'key3')
    y = 0

    thisdict = dict.fromkeys(x, y)

    print("from_key function: ", thisdict)

    #4. get
    x1 = car.get("a", 0)
    print("year car: ", x1)

    #5. items: Returns a list containing a tuple for each key value pair
    x2 = car.items()
    print(x2)

    #6. get keys:
    x3 = car.keys()
    print(x3)

    #7. pop: Removes the element with the specified key
    car.pop("model")
    print(car)

    #8. pop_item: Removes the last inserted key-value pair
    car.popitem()
    print("PopItem function:", car)

    #9. add item
    car["year"] = 1964
    car["model"] = "Mustang"
    print(car)

    # set default: Get the value of a key if the key exists, or add the key with its default value if the key does not exist.
    x = car.setdefault("age", "12")
    print("Set default: ", x)
    print(car)

    # update
    car.update({"color": "White"})
    print(car)

    # value
    print(car.values())
    print(type(car.values()))

