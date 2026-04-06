class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if str(num) in counts:
                counts[str(num)] += 1
            else:
                counts[str(num)] = 1
        print(counts)
        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        print(sorted_counts)
        final_counts = []
        count = 0
        for key in sorted_counts.keys():
            if count >= k:
                break
            final_counts.append(key)
            count += 1
        return final_counts