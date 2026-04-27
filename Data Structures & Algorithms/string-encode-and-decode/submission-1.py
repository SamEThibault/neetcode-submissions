class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            num_chars = str(len(s)).zfill(3)
            res += num_chars
            for c in s:
                res += str(c)
        return res


    def decode(self, string):
        res = []
        i = 0
        while i < len(string):
            length = int(string[i:i+3])
            i += 3
            res.append(string[i : i + length])
            i += length
        return res