# Function (Method) Basics

def greet():
    # A simple function without parameters
    print("Hello, World!")

def add_numbers(a, b):
    # A function with parameters that returns a value
    return a + b

def print_greeting(name="User"):
    # A function with a default parameter
    print(f"Hello, {name}!")

class Dog:
    # A simple class with methods
    def __init__(self, name):
        # This method is called when an object is instantiated
        self.name = name

    def bark(self):
        # A method inside a class
        print(f"{self.name} says Woof!")

if __name__ == "__main__":
    # Calling the greet function
    greet()  # Output: Hello, World!
    
    # Calling the add_numbers function with arguments
    result = add_numbers(5, 3)
    print("Sum:", result)  # Output: Sum: 8
    
    # Calling print_greeting with and without an argument
    print_greeting()  # Output: Hello, User!
    print_greeting("Alice")  # Output: Hello, Alice!
    
    # Using the Dog class and its methods
    my_dog = Dog("Buddy")
    my_dog.bark()  # Output: Buddy says Woof!
