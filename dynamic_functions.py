##########################################################################################
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.
# Don't call the function, you just need to define it.
def all_positives(numbers):
  # positive_num = number **2
  for num in numbers:
    if num> 0:
      
      print(True)
    else:
      print(False)

#############################################################################################
# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list (stored in the variable numbers) as long as they are greater than 0 and less than 1000, and returns the result of said sum.

def sum_less(total,numbers):
  # numbers = range(0,1000)
  # total = 0
  for n in numbers:
    if n > 0 and n < 1001:
      total += n
  return(total)
      
##########################################################################################
# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
# numbs = [1,2,3,4,5,6,7,8,9,10,11,22,21,24,43]

def count_even(numbs):
  count = 0
  for n in numbs:
    if n % 2 ==0:
      count += n
    else:
      pass
  return(count)