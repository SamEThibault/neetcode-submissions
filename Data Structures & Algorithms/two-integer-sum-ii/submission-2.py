class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers) - 1):
            exists = True
            j = i + 1
            while numbers[i] + numbers[j] < target:
                j += 1
                if j == len(numbers):
                    exists = False
                    break

            if exists and numbers[i] + numbers[j] == target:
                return [i+1, j+1]
        
            
        