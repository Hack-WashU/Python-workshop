def set_basics():
    # Sets: unordered collections of unique elements
    my_set = {1, 2, 3, 3, "apple"}
    print("This is a set:", my_set)  # Duplicates are automatically removed

    # Adding elements
    my_set.add("banana")
    print("Set after adding 'banana':", my_set)

    # Removing elements
    my_set.remove("apple")
    print("Set after removing 'apple':", my_set)

if __name__ == "__main__":
    set_basics()
