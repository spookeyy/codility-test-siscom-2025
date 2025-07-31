"""
**LONGEST PALINDROMIC SUBSTRING**

 Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""


"#Solution"


def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        #return longestPlalindrome from the string "s"
        longestP = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub == sub[::-1] and len(sub) > len(longestP):
                    longestP = sub
        return print("This is the longest palindromestring: ",longestP) if len(longestP) > 0 else longestP

longestPalindrome("babad")
longestPalindrome("dgoohddil")
longestPalindrome("cbbd")
longestPalindrome("tactoaa")