class Solution():
    def two_sum(nums, target):
        for i in nums:
            for j in nums:
                if nums[i] == target - nums[j]:
                    return {i,j}
return {}

def main():
    nums = {7,12,17,2}
    target = 9 
