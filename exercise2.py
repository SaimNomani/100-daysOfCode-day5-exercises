# you are going to write a program that calculates the highest score from a List of scores.
#
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
#
# The highest score in the class is: x
#
# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
#
# Example Output
# The highest score in the class is: 91
###########################################################
scores = (input("input list of student scores: \n")).split()
highest_score = -1
for score in scores:
    score_float = float(score)
    if (score_float > 100) or (score_float < 0):
        print("invalid score")
        highest_score = -1
        break
    else:
        if score_float > highest_score:
            highest_score = score_float
if highest_score != -1:
    print(f"highest score in class is: {highest_score}")
