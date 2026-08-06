class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        #Creating car with both position and speed as pair 
        for i in range(len(position)):
            pos = position[i]
            sp = speed[i]
            cars.append([pos, sp])
        cars.sort(reverse = True)

        fleet = 0
        last_time = 0
        #Calculating formula and checking if the time for car to reach target is lesser than fastest car's time, if no then there is +1 fleet
        for p,s in cars:
            time = (target - p) / s

            if time > last_time:
                fleet = fleet + 1
                last_time = time
        return fleet


        