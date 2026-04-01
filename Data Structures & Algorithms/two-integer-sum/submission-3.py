class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        done= {}
        for i,n1 in enumerate(nums):
            n2 = target - n1
            if n2 in done:
                return [done[n2],i]
            done[n1] = i