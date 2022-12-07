class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        starts = sorted([start for start, end in intervals])
        ends = sorted([end for start, end in intervals])
        
        rooms = max_rooms = 0
        s = e = 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            max_rooms = max(max_rooms, rooms)
            
        return max_rooms
 
            
            
            
            
        