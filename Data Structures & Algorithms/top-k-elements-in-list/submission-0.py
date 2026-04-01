class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket= [[] for _ in range(len(nums) + 1)]
        for n, count in freq.items():
            bucket[count].append(n)
        result = []
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result

        