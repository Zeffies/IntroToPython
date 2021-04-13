# Write a function that takes in two numbers, and adds them together.
def add_calc(num1, num2):
     calced = num1 + num2
     print('%d + %d = %d' % (num1, num2, calced))
     return calced
# Make your function print out a sentence showing the two numbers, 
# and the result.
# Call your function with three different sets of numbers.
test_calced = add_calc(30, 70)
print(test_calced)
test_calced = add_calc(21, 23)
print(test_calced)
test_calced = add_calc(315, 73)
print(test_calced)
