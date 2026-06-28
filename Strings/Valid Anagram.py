#Problem: Valid Anagram
#Platform: LeetCode
#Difficulty: Easy
#Topic: String

#Approach 1 (By using the sorted function)
#Time complexity = O(nlogn)

def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
  
#Approach 2 (By using Dictionary)
#Time Complexity= O(n)

def isAnagram(self, s: str, t: str) -> bool:
        s_d={}
        t_d={}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            s_d[s[i]] = s_d.get(s[i], 0) + 1
            t_d[t[i]] = t_d.get(t[i], 0) + 1

        return s_d==t_d

