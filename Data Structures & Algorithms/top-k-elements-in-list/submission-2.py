class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        buckets = [[] for _ in range(len(nums)+1)]
        for num,f in freq.items():
            buckets[f].append(num)
        result = []
        for f in range(len(buckets)-1,0,-1):
            for num in buckets[f]:
                result.append(num)
                if len(result)==k:
                    return result
            
