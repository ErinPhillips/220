"""
Name: Erin Phillips
weighted_average.py

Problem: This program computes students' weighted average and
        class average using numeric data from a text file.

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    class_grade_sum = 0
    num_students = 0

    for line in in_file:
        new_list = line.split(": ")
        values = new_list[1].split()
        grade_sum = 0
        weight_sum = 0

        for i in range(0, len(values) - 1, 2):
            weight = float(values[i])
            test_grade = float(values[i + 1])
            weight_sum = weight_sum + weight
            grade_sum = grade_sum + (test_grade * weight)

        if weight_sum == 100:
            average = grade_sum / 100
            class_grade_sum = class_grade_sum + average
            num_students = num_students + 1
            print(new_list[0] + "'s", "average:",
                  round(average, 1), file=out_file)

        elif weight_sum > 100:
            print(new_list[0] + "'s", "average: Error: The weights are more than 100.",
                  file=out_file)

        else:
            print(new_list[0] + "'s", "average: Error: The weights are less than 100.",
                  file=out_file)

    total_class_avg = round(class_grade_sum / num_students, 1)
    print("Class average:", total_class_avg, file=out_file)
    in_file.close()
    out_file.close()


def main():
    file1 = input('input file name: ')
    file2 = input('output file name: ')
    weighted_average(file1, file2)


if __name__ == '__main__':
    main()
