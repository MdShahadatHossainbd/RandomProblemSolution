# Python3 program to find
# concentration of a solution
# using given Mass and Volume

# Function to calculate
# concentration from the given mass of solute and volume of a solution
def get_concentration(mass, volume):
    if (volume == 0):
        return -1;
    else:
        return (mass / volume) * 1000;

    # Driver code


mass = 100.00;
volume = 500.00;

print(get_concentration(mass, volume))

# This code is contributed by Pratima Pandey
