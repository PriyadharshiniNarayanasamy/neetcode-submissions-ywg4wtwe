class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        res = 0
        while l<r:
            if heights[l]< heights[r]:
                area = (r-l) * heights[l]
                res = max(res,area)
                l+=1
            else:
                area = (r-l) * heights[r]
                res = max(res,area)
                r-=1
            
        return res

            