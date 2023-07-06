#  Implement a function to check if a given string is a palindrome.

def ispalindrome(s):
    i=0 
    j=len(s)-1
    while(i<j):
        if(s[i]!=s[j]):
            return False 
        i+=1
        j-=1
    return True

s=input("Enter s string:")
if(ispalindrome(s)):
    print(s, "is palindrome.")
else:
    print(s, "is not palindrome")
        
        
    