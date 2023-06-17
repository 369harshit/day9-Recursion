def combinationSum(nums, target):
    result = []
    nums.sort()  # Sort the input list to handle duplicates
    generate_combinations(nums, target, [], result)
    return result


def generate_combinations(nums, target, current, result):
    if target == 0:
        result.append(current[:])  # Append a copy of the current combination to the result
        return
    if target < 0:
        return
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate numbers to avoid duplicate combinations
        current.append(nums[i])
        generate_combinations(nums[i+1:], target - nums[i], current, result)  # Use i+1 to avoid reusing the same element
        current.pop()  # Backtrack by removing the last element from the current combination


nums = [1,1,1,2,2]
target = 4

result = combinationSum(nums, target)
print(result)
