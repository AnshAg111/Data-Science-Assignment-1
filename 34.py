#  Implement a function to find the longest common prefix among a list of strings

def longestCommonPrefix(strs):
    s = strs[0]

    for i in range(1, len(strs)):
        c = 0
        t = ""
        while c < len(strs[i]) and c < len(s) and strs[i][c] == s[c]:
            t += s[c]
            c += 1
        s = t

    return s

strs = ["flower","flow","flight"]
print("The longest commen prefix in the given list of strings is:",longestCommonPrefix(strs))