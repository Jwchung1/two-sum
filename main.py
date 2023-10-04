from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        match = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == match:
                result.append(i)
                result.append(j)
                return result
    return []