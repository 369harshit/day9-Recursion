def is_palindrome(s):
    return s == s[::-1]


def partition_palindrome(s):
    n = len(s)
    result = []
    partition = []

    def backtrack(start):
        if start >= n:
            # Make a copy of the partition before appending
            result.append(partition[:])
        else:
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    partition.append(substring)
                    backtrack(end)
                    partition.pop()  # Remove the last added substring for backtracking

    backtrack(0)
    return result


# Example usage:
input_string = "aab"
partitions = partition_palindrome(input_string)
print("[",end=" ")
for partition in partitions:
    print(partition ,end=" ")
print("]",end=" ")
    
