#Problem: Remove element
#Platform: LeetCode
#Difficulty: Easy
#Topic:Array,Two Pointers

#Time complexity= O(n)

def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)

        j=0
        

        for i in range(n):
            if nums[i]!=val:
                
                nums[j]=nums[i]
                
                j+=1
        return j
