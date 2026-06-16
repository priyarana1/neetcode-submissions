class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list) #ensures that program wont throw an error whenever you access a key that isnt there
        #it will default just add the key with an empty list
        #count = defaultdict(int) --> automatically adds key with value 0


        #iterate through all the words: key = sorted word, value = list with actual world
        for word in strs:
            key = "".join(sorted(word)) #sorted(word) returns list of characters
            # "".join breaks the list and just appends the characters into a single string
            anagrams[key].append(word)

        return list(anagrams.values())        