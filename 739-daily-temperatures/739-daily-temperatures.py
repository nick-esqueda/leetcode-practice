class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        while stack and the curr temp is greater than temp on top of stack:
            pop stack
            reassign the specified idx to curr i - top i
        put curr temp and index on stack
        """
        forecast = [0] * len(temperatures)
        
        sta = []
        for curr_i, curr_temp in enumerate(temperatures):
            while sta and curr_temp > sta[-1][1]:
                sta_i, sta_temp = sta.pop()
                forecast[sta_i] = curr_i - sta_i
            sta.append((curr_i, curr_temp))
            
        return forecast
                
