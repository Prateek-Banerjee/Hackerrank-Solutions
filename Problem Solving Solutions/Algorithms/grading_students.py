#!/bin/python3
#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    final_grades = []
    for i in grades:
        if i >= 38:
            j=i
            while True:
                if j%5==0:
                    if j-i<3: 
                        final_grades.append(j)
                    else:
                        final_grades.append(i)
                    break
                elif j%5!=0: j+=1
        else:
            final_grades.append(i)
    print(*final_grades, sep="\n")
if __name__ == '__main__':
    grades_count = int(input())
    grades = list()
    for _ in range(grades_count):
        grades_item = int(input())
        grades.append(grades_item)
    result = gradingStudents(grades)