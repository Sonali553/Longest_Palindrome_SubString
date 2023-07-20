def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]
def longest_pldSubstring(s):
    longest = ""
    for i in range(len(s)):
        palindrome1 = expand(s, i, i)
        palindrome2 = expand(s, i, i + 1)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2
    return longest
print(longest_pldSubstring("aaaabaaa"))
print(longest_pldSubstring("abba"))
