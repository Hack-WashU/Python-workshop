# dict_basics.py

def dict_basics():
    # Dictionaries: key-value pairs
    person = {
        "name": "Alice",
        "age": 25
    }
    print("This is a dictionary:", person)

    # Accessing a value by its key
    print("Name:", person["name"])

    # Adding a new key-value pair
    person["city"] = "New York"
    print("Updated dictionary:", person)

    for x in person.keys():
        print(f"Key {x} corresponds to {person[x]}")

if __name__ == "__main__":
    dict_basics()
