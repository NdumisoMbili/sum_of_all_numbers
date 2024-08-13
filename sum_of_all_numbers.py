# Let the user enter a positive integer n
n = int(input("Enter a positive number: "))
total = 0 # The sum

# Calculate the sum using a for loop
for i in range(1, n+1):
    total += i

# Print the sum
print(f"The sum of numbers from 1 to {n} is {total}")