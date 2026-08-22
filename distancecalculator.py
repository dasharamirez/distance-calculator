import math

# Ask the user to enter the coordinates of the first point
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))

    # Ask the user to enter the coordinates of the second point
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # Find the differences between the x and y coordinates
    distance_x = x2 - x1
    distance_y = y2 - y1

    # Compute the distance using the distance formula
    distance = math.sqrt(math.pow(distance_x, 2) + math.pow(distance_y, 2))

    # Display the result rounded to two decimal places
    print(f"The distance between the two points is: {distance:.2f}")

except ValueError:
    # Tell the user to enter numbers if the input is invalid
    print("Error: Enter numbers only.")