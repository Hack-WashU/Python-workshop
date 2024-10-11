def tuple_basics():
    # Tuples: ordered, immutable collections
    my_tuple = (1, 2, 3, "apple")
    print("This is a tuple:", my_tuple)

    # Accessing elements
    print("First element:", my_tuple[0])
    print("Last element:", my_tuple[-1])

    # Tuples are immutable, so they cannot be modified after creation
    # The following would raise an error: my_tuple[0] = 10

if __name__ == "__main__":
    tuple_basics()
