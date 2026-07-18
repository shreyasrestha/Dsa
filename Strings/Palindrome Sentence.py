#Problem: Palindrome Sentence
#Platform: GeeksforGeeks
#Difficulty: Easy
#Topic: String


#Time complexity = O(n)

def isPalinSent(self, s):
	    
		string=""
		for i in s.lower():
		    if i !=" " and i.isalnum():
		        string+=i
		        
	    return string==string[::-1]

