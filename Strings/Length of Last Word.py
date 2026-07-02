#Problem: Length of Last Word
#Platform: LeetCode (58)
#Difficulty: Easy
#Topic: String

#(By using the string functions)
#Time complexity = O(n)

def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        words=s.split(" ")
        return len(words[-1])  
