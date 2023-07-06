#  Implement a function to find the longest palindrome substring in a given string.

def longestPalindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    indi = 0
    indj = 0

    for gap in range(n):
        for i in range(n - gap):
            j = i + gap

            if gap == 0:
                dp[i][j] = True
            elif gap == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

            if dp[i][j]:
                if j - i > indj - indi:
                    indi = i
                    indj = j

    return s[indi:indj + 1]

str=input("Enter any string: ")
print("The longest palindromic substring is:", longestPalindrome(str))