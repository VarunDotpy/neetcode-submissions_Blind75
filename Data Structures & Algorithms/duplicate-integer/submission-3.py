class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #empty set
        for value in nums:
            if value in seen:
                return True
                break
            else:
                seen.add(value)
        return False

            
        