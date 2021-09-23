"""
Erin Phillips
mean.py

Problem: This program calculates the Root-Mean-Square, the Harmonic Mean, and the Geometric Mean.

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""

# Take user input and output 3 different types of mean.
# Input is from user. User will specify number of values, then enter the values when prompted.
# Output is calculation of RMS Average, Harmonic Mean, and Geometric Mean.


# step 2: define a function, main()
# step 3: assign variables for number of values, num
# step 4: assign variables for accumulators, acc1, acc2, acc3
# step 5: create a loop with range as num, loop will take user input of values
# step 6: create equations for rms average, harmonic mean, and geometric mean
#         using the values input.
# step 7: import math library for square root function
# step 8: print rms average, harmonic mean, and geometric mean
#         round to 3 decimal places

from math import sqrt


def main():
    num = eval(input("Specify the number of values to be entered: "))
    rms_acc = 0
    harm_acc = 0
    geo_acc = 1
    for i in range(num):
        values = eval(input("Enter value " + str(i + 1) + ": "))
        rms_acc = (rms_acc + values ** 2)
        rms_avg = sqrt(rms_acc / num)
        harm_acc = harm_acc + 1 / values
        harm_mean = num / harm_acc
        geo_acc = geo_acc * values
        geo_mean = geo_acc ** (1 / num)

    print(round(rms_avg, 3))
    print(round(harm_mean, 3))
    print(round(geo_mean, 3))


if __name__ == '__main__':
    main()
