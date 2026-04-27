class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_strings = []
        res = []
        for string in strs:
            sorted_strings.append(str(sorted(list(string))))
        
        uniques = set(sorted_strings)
        print("Original: ", strs)
        print("Sorted Strings: ", sorted_strings)
        print("Unique Set: ", uniques)

        i = 0
        for string in uniques:
            res.append([])
            while string in sorted_strings:
                index = sorted_strings.index(string)
                res[i].append(strs[index])
                sorted_strings[index] = None
            i += 1
        
        return res
