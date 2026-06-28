#Problem: Valid Anagram 
#Platform: LeetCode (125)
#Difficulty: Easy
#Topic: String

#Approach 1
#time complexity : O(n^2)

def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s.lower():
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                string+=i

        return string==string[::-1]
