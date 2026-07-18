
#Problem: Reverse a String
#Platform: GeeksforGeeks
#Difficulty: Easy
#Topic: String
#Time complexity = O(n)

class Solution:
    def reverseString(self, s: str) -> str:
        # code here
        n=len(s)
        j=n-1
        i=0
        l=[]
        for c in s:
            l.append(c)
        while i<j:
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
            
        res="".join(l)
        return res
