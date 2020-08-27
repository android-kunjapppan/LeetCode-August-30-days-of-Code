class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intvl = sorted([(x[0], i) for i, x in enumerate(intervals)], key=lambda x: x[0])
        
        starts, idx = [x[0] for x in intvl], [x[1] for x in intvl]
        
        res = []
        
        for x in intervals:
            pos = bisect.bisect_left(starts, x[1])
            if pos == len(starts):
                res.append(-1)
            else:
                res.append(idx[pos])
        return res
        
