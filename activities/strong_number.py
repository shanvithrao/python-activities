# Strong Number
# A number is called a Strong number if the sum of the factorial of its digits equals the number itself.
# Example: 145 => 1! + 4! + 5! = 1 + 24 + 120 = 145

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_strong_number(num):
    temp = num
    digit_sum = 0
    while temp > 0:
        digit = temp % 10
        digit_sum += factorial(digit)
        temp //= 10
    return digit_sum == num

# Test
numbers = [1, 2, 145, 40585, 100]
for n in numbers:
    result = "Strong Number" if is_strong_number(n) else "Not a Strong Number"
    print(f"{n} => {result}")

