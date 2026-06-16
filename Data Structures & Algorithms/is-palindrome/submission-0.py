class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        i = 0
        j = len(s) - 1
        
        while i < j:

            #if it's a blank space, then skip it
            while i < j and not s[i].isalnum():
                i+=1

            #if it's a blank space, then skip it
            while i < j and not s[j].isalnum():
                j-=1
            
            #if they aren't the same, return false
            if s[i] != s[j]:
                return False
            
            #if they are, iterate
            i+=1
            j-=1
            
        return True
        