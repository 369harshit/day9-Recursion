import math

def get_kth_permutation(n, k):
    numbers = list(range(1, n+1))
    result = []

    k-= 1  # Adjust k to 0-based index
    factorial = math.factorial(n)

    for i in range(n, 0, -1):
        factorial //= i
        index = k // factorial
        result.append(numbers[index])
        numbers.pop(index)
        k %= factorial

    return result

# Example usage:
n = 3
k = 3
permutation = get_kth_permutation(n ,k)
print(permutation)
