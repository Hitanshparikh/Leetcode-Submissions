class Solution:
    def divideArray(self, nums: List[int]) -> bool:        
        freq = [0] * 501
        
        for num in nums:
            freq[num] += 1
        
        for count in freq:
            if count % 2 != 0:
                return False
        
        return True