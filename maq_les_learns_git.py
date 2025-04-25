import numpy as np
import sys

def print_message():
    print("Hello world!")


if __name__ == "__main__":

    # Task 1: take two integers from the command line
    # that will be the matrix arguments
    itot = input('Please input a "itot" integer:')
    jtot = input('Please input a "jtot" integer:')

    # Task 2: adjust the print message and show the itot and jtot input.
    print_message()

    # Task 3: generate np arrays x and y that go from 0 to 1 in itot and
    # jtot steps.

    # Task 4: generate a 2D np array a with random numbers
    random_2d = np.random.random((itot,jtot))
    # Task 5: plot the array a with axes x and y using pcolormesh.

    # Task 6: calculate the mean of the array a and print it to the screen.
    np.mean(x)
    np.mean(y)
    # Task 7: calculate the variance of the array a and print it to the screen.
    itot = int(2)
    jtot = int(3)

    a = np.random.random((itot, jtot))

    var_a = np.var(a)
    print(f"Variance of array: {var_a:.6f}")


