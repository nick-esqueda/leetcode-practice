class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        loop through inters:
            newI: [1,2]
            ints:   ...[3,4]
            if end is less than inters[i] start:
                push newInter to merged
                return merged + inters[i:]

            newI:         [7,9]
            ints: ...[4,5]
            if start is greater than inters[i] end:
                push inters[i] to merged

            else (the start is less than or equal to inters[i] start, or start is within inters[i] range):
                take the min start val and max end value
                reassign newInter to those values
            
        append newInter to inters
        return merged
        """
        
        merged = []
        for i, currInter in enumerate(intervals):
            if newInterval[1] < currInter[0]:
                merged.append(newInterval)
                return merged + intervals[i:]
            elif newInterval[0] > currInter[1]:
                merged.append(currInter)
            else:
                newInterval = [min(newInterval[0], currInter[0]), max(newInterval[1], currInter[1])]
        merged.append(newInterval)
        return merged
