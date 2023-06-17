def print_subset_sums(nums):
    n = len(nums)
    total_subsets = 2 ** n  # Total number of subsets

    for i in range(total_subsets):
        subset_sum = 0

        for j in range(n):
            if i & (1 << j):  # Check if jth bit is set in i
                subset_sum += nums[j]

        print(subset_sum ,end=" ")

# Example usage
nums = [1, 2, 3]
print_subset_sums(nums)
