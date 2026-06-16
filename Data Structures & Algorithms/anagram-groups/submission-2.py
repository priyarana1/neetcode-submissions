class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:

            #each string has to get an array of 26 values, each indicating
            #the frequency of all letters
            count = [0] * 26 # a - z all have a value of 0

            #ascii of current character - ascii of lowercase a
            for c in s:
                count[ord(c) - ord("a")] += 1 #you are making the count of each character
                #every time you come across that character, you increase the frequency by one
                #how do you know which index? subtract that ascii value by the 1st

            #the value is the list of strings with this map
            #python lists cannot be dictionary keys, so convert to a tuple
            #the keys have to be immutable- if you change a key you mess a bunch of stuff up
            res[tuple(count)].append(s)
                
        return list(res.values())