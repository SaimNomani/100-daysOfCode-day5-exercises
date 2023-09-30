# You are going to write a program that calculates the average student height from a List of heights.
#
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#
# e.g.
#
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#
# There are a total of 7 heights in student_heights
#
# 1146 ÷ 7 = 163.71428571428572
#
# Average height rounded to the nearest whole number = 164
#
#
# Example Input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
#
# Example Output
# 171
######################################################################
student_heights = (input("enter list of student heights: \n")).split()
sumOfHeights = 0
for height in range(0, len(student_heights)):
    student_heights[height] = int(student_heights[height])
    sumOfHeights += student_heights[height]
avgHeight = round(sumOfHeights / len(student_heights))
print(avgHeight)
