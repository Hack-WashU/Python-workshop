# Float (Floating-Point Numbers) Basics

def float_basics():
    # Floats: numbers with decimals
    temperature = 98.6
    distance = 10.5
    pi = 3.14159

    print("This is a float:", temperature)
    print("Another float:", distance)

    # Basic arithmetic with floats
    print("Add 1.5 to temperature:", temperature + 1.5)
    print("Multiply distance by 2:", distance * 2)
    print("Divide pi by 2:", pi / 2)

    # Rounding floats
    rounded_pi = round(pi, 2)  # Round to 2 decimal places
    print("Rounded pi to 2 decimal places:", rounded_pi)

    # Handling precision issues with floats
    result = 0.1 + 0.2
    print("0.1 + 0.2 equals:", result)  # This won't be exactly 0.3 due to precision issues

if __name__ == "__main__":
    float_basics()
