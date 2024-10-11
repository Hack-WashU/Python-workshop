# list_basics.py

def list_basics():
    # Lists: collection of items
    numbers = [1, 2, 3, 4, 5]
    print("This is a list:", numbers)

    # Accessing elements in the list
    print("First item in the list:", numbers[0])

    # Adding an item to the list
    numbers.append(6)
    print("List after adding 6:", numbers)

    # Taking out an item of the list
    numbers.pop(1)
    print("List after removing 2nd item:", numbers)  

    #Taking out a specific iten of the list
    numbers.remove(1)
    print("List after removing 1:", numbers)  

    for x in numbers:
        print(x)

if __name__ == "__main__":
    list_basics()
