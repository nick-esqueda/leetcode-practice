class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        use stack to keep track of cars that are traveling slow enough to create a fleet
        iterating backwards through a sorted car array:
            unpack pos and speed from each car
            calculate how long it would take for car to get to the target
            if curr car gets to target in less or equal time than the car on top of stack, continue to next car
            else, add car to stack
        return fleet count
        """
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=lambda x: x[0])
        
        sta = [cars[-1]]
        i = len(cars) - 2
        while i >= 0:
            cur_pos, cur_speed = cars[i]
            curr_t = (target - cur_pos) / cur_speed
            sta_pos, sta_speed = sta[-1]
            sta_t = (target - sta_pos) / sta_speed
            
            if curr_t > sta_t:
                sta.append(cars[i])
                
            i -= 1
            
        return len(sta)

