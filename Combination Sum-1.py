def combinationSum(nums, target):
    result = []
    generate_combinations(nums, target, [], result)
    return result

def generate_combinations(nums, target, current, result):
    if target == 0:
        result.append(current)
        return
    if target < 0:
        return
    for i in range(len(nums)):
        generate_combinations(nums[i:], target - nums[i], current + [nums[i]], result)

nums = [2, 3, 6, 7]
target = 7

result = combinationSum(nums, target)
print(result)
