

# define a function
def fibonacci(number):
  if number == 0:
    return 0
  if number == 1:
    return 1
  else:
    return fibonacci(number-1) + fibonacci(number-2)

# print the Fibonacci sequence
number = int(input("Enter the number of terms: "))
print(fibonacci(number))