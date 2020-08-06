class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ht = {}
        dups = []
        for x in nums:
            if x in ht:
                dups.append(x)
            else:
                ht[x] = x
        return list(set(dups))
