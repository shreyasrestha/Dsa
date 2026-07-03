#Problem: Contains Duplicate
#Platform: LeetCode (217)
#Difficulty: Easy
#Topic: Arrays

# Approach 1 (By sorting)
#Time complexity : O(nlogn)
def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True

        return False
