# Problem 14 - Lattice Paths
import math

print('Find Number of Lattice Paths for Square Grids ie. 3 x 3, 4 x 4')


def get_lattice_path(number):

    n = 2 * number
    k = number

    lattice_coefficient = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    number_of_paths = str(int(lattice_coefficient))

    print("\nLooking for Number of Paths in a " + str(number) + " x " + str(number) + " Grid.")
    return number_of_paths + " Path(s) Found. "


num = int(input("Please Enter the Number for the Width and Height of the Table "))
print(get_lattice_path(num))
