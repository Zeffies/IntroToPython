# Write a program that passes a list of numbers to a function.
def gauss_addition(number):
    num1_pop = 0
    num2_pop = -1
    part_sum = 0
    many_part_sum = 0
    current_number = number[-1]
    biggest_number = number[-1]
    num1 = number[num1_pop]
    num2 = number[num2_pop]
    final_sum = 0
# The function should use a while loop to keep popping the first 
  # and last numbers from the list and calculate the sum of those two numbers.
    while current_number > ((biggest_number/2)):
        if number:
            num1 = number.pop(0)
            num2 = number.pop(-1)
        part_sum = num2 + num1
        if number:
            if current_number > ((biggest_number/2)):
                current_number = number[num2_pop]
        elif current_number == ((biggest_number/2)+1):
            current_number = current_number - 1
        many_part_sum = many_part_sum + 1
        final_sum = final_sum + part_sum
        print(many_part_sum)
    print('This is how many partial sums there were: ' + str(many_part_sum))
    print('The final sum is: ' + str(final_sum))
# The function should print out the current numbers that are being added,
  # and print their partial sum.
# The function should keep track of how many partial sums there are.
# The function should then print out how many partial sums there were.
# The function should perform Gauss' multiplication, and report the final answer.
# Prove that your function works, by passing in the range 1-100,
  # and verifying that you get 5050.
gauss_addition(list(range(1,103)))
# Your function should work for any set of consecutive numbers,
  # as long as that set has an even length.
# Bonus: Modify your function so that it works for any set of 
  # consecutive numbers, whether that set has an even or odd length.

