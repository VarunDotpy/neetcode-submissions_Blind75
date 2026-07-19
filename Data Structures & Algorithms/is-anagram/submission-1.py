class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
       
        #if len of both strings not same, then not anagram

        # if len(s) != len(t):
        #     return False
        
        # #use hashmap to solve the problem
        # #create a hashmap, keys = character, value = number of occurences
        # countS = {}
        # countT = {}
        
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i],0) #.get(key, def value) def value in case value(the char) doesnt exist yet
        #     countT[t[i]] = 1 + countT.get(t[i],0)
        
        # for char in countS: #iterating through the keys
        #     if countS[char] != countT.get(char,0): #if the count of the same characters doesnt match, means its not anagram
        #         return False    #.get() used because in case the key doesnt exist in the count hashmap yet

        # return True

        #another solution : using sort, just sort all strings and do a simple == comparison
        return sorted(s) == sorted(t)
             