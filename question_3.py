"""
**SUBSTRING WITH CONCATENATION OF ALL WORDS**

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.

"""

"#Solution"

#Decalre a map to store the words
#Decalre a list to store the indices
#Decalre a variable to store the word length
# traverse through all possible substrings in "s" and check if it is a concatenation of all words
# if it is, add the starting index to the list

# create a temporary map and initialize it with original map to store every possible substring
# extract from the words from the substring and if the words is not present in the temporary map, break,
# else if it is present, we decrese its corresponding count

# after traversing the substing, we traverse temp map for any word whose count is not 0, if it is, we add the starting index to the result


def findSubstring(s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # size of word in words
        size_of_word = len(words[0])

        count_of_words = len(words)
        print("word count is ", count_of_words)

        # total chars present in word
        total_wordSize = size_of_word * count_of_words

        results = []

        # if total num of chars in words is greater than that of string "s"
        if total_wordSize > len(s):
                return results
        
        # Map stores the words present in words
        # against it's occurrences inside "words"
        hash_map = dict()

        for i in range(count_of_words):
                if words[i] in hash_map:
                        hash_map[words[i]] += 1
                else:
                        hash_map[words[i]] = 1

        for i in range(0, len(s) - total_wordSize + 1, 1):
                temp_hash_map = hash_map.copy()
                j = i
                count = count_of_words

                # traversing the substring
                while j < i + total_wordSize:
                        # word extraction
                        word = s[j:j + size_of_word]
                        if word in temp_hash_map:
                                temp_hash_map[word] -= 1
                                if temp_hash_map[word] == 0:
                                        count -= 1
                        else:
                                break
                        j += size_of_word

                # Store the starting index of that substring
                # when all the words in the list are in substring
                if count == 0:
                        results.append(i)

                return print("Outpur is ", results)


# testing the function
findSubstring("barfoothefoobarman", ["foo","bar"])
findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
        