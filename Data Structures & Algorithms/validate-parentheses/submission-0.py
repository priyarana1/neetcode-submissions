class Solution:
    def isValid(self, s: str) -> bool:
        
        #make sure the indices of pairs match
        opening = ['(', '[', '{'] 
        closing = [')', ']', '}']


        stack = []

        for c in s:
            if c in opening:
                stack.append(c) #only push 

            if c in closing:
                if len(stack) == 0: #make sure there is something to compare first or it will throw error
                    return False
                
                top = stack[-1] #retrieve the top of stack

                if opening.index(top) != closing.index(c): #check if it matches its pair
                    return False
                stack.pop() #if it does then pop that and move on


        return len(stack) == 0 #stack must be empty


