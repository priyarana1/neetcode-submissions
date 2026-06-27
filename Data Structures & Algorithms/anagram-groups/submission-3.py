class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

      
      all = defaultdict(list) #map is filled with empty lists for all keys

      for s in strs: #iterate through each word
        count = 26 * [0] #the keys will be 26 index arrays defaulted to 0 for now

        for c in s: #iterate through each character
            index = ord(c) - ord('a') #find ascii position for that character to get index 
            count[index] += 1

        all[tuple(count)].append(s) #lists cant be keys in dictionaries, append the word to that map
        ans = []

      for map, words in all.items():
        ans.append(words)

      return ans
            
                