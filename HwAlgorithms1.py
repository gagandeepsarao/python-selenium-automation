#Level 1
#Solution1

def foo_bar(n: int):
    for i in range(1, 101):
        if i % 3 == 0 and i % 7 == 0:
            print("BinGo")
        elif i % 3 == 0:
            print("Bin")
        elif i % 7 == 0:
            print("Go")
        else:
            print(i)

foo_bar(100)


#Solution 2:

def sum_numbers(n: int):
    final_sum = 0
    for i in range(n + 1):
        current_num  = n % 10
        final_sum  = final_sum + current_num
        n = n // 10
    return final_sum

print(f'Sum is {sum_numbers(1234567)} ')

#Level2
#Solution1

def find_max(a: int, b: int, c: int):
    max_num  = a
    if b > a:
        max_num = b
        if b < c:
            max_num = c
    return max_num

print(find_max(9,3,5))
print(find_max(3,8,2))
print(find_max(1,4,9))

#Solution 2

def leap_year(year: int):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
    return False

#Solution 3

def generate_fibonacci_sequence(n: int):
# Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]
# Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):
# Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]
        next_num = fib_sequence[i-1] + fib_sequence[i-2]
# Append the new Fibonacci number to the list using the append() function
        fib_sequence.append(next_num)

    return fib_sequence

print(f'Fibonnaci sequence is {generate_fibonacci_sequence(9)}')

