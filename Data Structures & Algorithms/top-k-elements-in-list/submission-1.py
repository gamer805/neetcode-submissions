class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        sorted_data = list(dict(sorted(counts.items(), key=lambda item: item[1])).keys())

        return sorted_data[len(sorted_data)-k:]