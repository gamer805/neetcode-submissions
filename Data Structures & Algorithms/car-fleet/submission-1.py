class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_pos, car_speed = zip(*sorted(zip(position, speed))[::-1])
        stack = []
        prev_time = 0
        for position, speed in zip(car_pos, car_speed):
            curr_time = (target - position) / speed
            if len(stack) > 0 and prev_time >= curr_time:
                continue
            else:
                stack.append((position, speed))
                prev_time = curr_time
        
        return len(stack)