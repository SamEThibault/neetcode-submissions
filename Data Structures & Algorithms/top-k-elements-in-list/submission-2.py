class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_d = {}

        # first pass: populate hash map {num: freq}
        for num in nums:
            if num in nums_d:
                nums_d[num] += 1
            else:
                nums_d[num] = 1
        
        # sort nums based on their occurrences
        most_frequent = sorted(set(nums), key=lambda x: nums_d[x], reverse=True)

        return most_frequent[:k]