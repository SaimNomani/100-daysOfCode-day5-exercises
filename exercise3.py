# You are going to write a program that calculates the sum of all the even numbers from 1 to x. Thus,
#
end_point = int(input("Enter the endpoint up to which you want to add even numbers:\n"))
starting_point = 1
if end_point <= starting_point:
    print("end point must be greater than 1.\n")
else:
    sumOfEvenNos = 0
    for n in range(1, end_point + 1):
        if n % 2 == 0:
            sumOfEvenNos += n
    print(f"sum of even number from {starting_point} to {end_point} is: {sumOfEvenNos}")
