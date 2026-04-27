class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i = 0
        j = 1
        while True:
            print(f"Current indices: i={i}, j={j}")
            if sorted_nums[i] + sorted_nums[j] < target:
                i += 1
                j += 1
            elif sorted_nums[i] + sorted_nums[j] > target:
                i -= 1
            else:
                # find where the original indices were
                og_i = nums.index(sorted_nums[i])
                og_j = nums.index(sorted_nums[j])
                if og_i == og_j:
                    og_j = nums.index(sorted_nums[j], og_i + 1)
                    return [og_i, og_j]
                elif og_i > og_j:
                    return [og_j, og_i]
                else:
                    return [og_i, og_j]

# [-5, -4, -3, -2, -1]

