class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(list(s1))
        print("S1", sorted_s1)
        for i in range(0, len(s2)):
            sliced = sorted(list(s2[i:i+len(s1)]))
            print(sliced)
            if sliced == sorted_s1:
                return True
        
        return False