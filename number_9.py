# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product ABC.
# Function to generate pythagorean
# triplets smaller than limit


# Function to generate numbers
def pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000-a-b
            if (a**2+b**2) == c**2:
                return a*b*c


# printing the result
print("The Product of ABC is: " + str(pythagorean_triplet()))
