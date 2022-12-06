class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        
        for i in range(len(intervals) - 1):
            start, end = intervals[i]
            next_start, next_end = intervals[i + 1]
            
            if end > next_start:
                return False
            
        return True
            