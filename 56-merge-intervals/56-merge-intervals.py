class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        start off a merged list with first inter in it
        loop through the rest of intervals (start at i = 1):
            if start <= top's end:
                take top's start and whichever is max end
                set the top to that new inter
            else:
                push the inter to merged
        return the merged list
        """
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        for inter in intervals[1:]:
            top = merged[-1]
            if inter[0] <= top[1]:
                merged[-1] = [top[0], max(inter[1], top[1])]
            else:
                merged.append(inter)
        return merged