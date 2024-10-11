def control_flow_basics():
    x = 10
    # If-Else Statement
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is 5 or less")

    # Elif Statement
    if x > 15:
        print("x is greater than 15")
    elif x > 5:
        print("x is greater than 5 but less than or equal to 15")
    else:
        print("x is 5 or less")

    # For Loop
    for i in range(5):
        print("For loop iteration:", i)

    # While Loop
    count = 0
    while count < 3:
        print("While loop iteration:", count)
        count += 1

if __name__ == "__main__":
    control_flow_basics()
