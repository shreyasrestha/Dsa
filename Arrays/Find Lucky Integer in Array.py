#Problem: Find Lucky Integer in Array
#Platform: LeetCode (1394)
#Difficulty: Easy
#Topic: Arrays

#TimeComplexity : O(n)

def findLucky(self, arr: List[int]) -> int:
        d=defaultdict(int)

        for i in arr:
            d[i]+=1
        m=-1
        for k,v in d.items():
            if k==v and k>m:
                m=k

        return m
