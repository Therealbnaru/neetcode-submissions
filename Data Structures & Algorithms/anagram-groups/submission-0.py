class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGrouped = {}  # stores each anagram type and the words in that group

        for word in strs:  # go through every word
            sortedWord = ''.join(sorted(word))  # sort the letters of the word

            if sortedWord not in anagramGrouped:  # if this anagram group does not exist yet
                anagramGrouped[sortedWord] = []  # make a new empty group

            anagramGrouped[sortedWord].append(word)  # put the original word into that group

        return list(anagramGrouped.values())  # return all of the groups