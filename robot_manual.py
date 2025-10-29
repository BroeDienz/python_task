import random
random.seed(42)  # For consistent results
import time

# Copy the FarmMap class here (provided above)
class FarmMap:
    """This class is ALREADY DONE - just copy and use it!"""
    
    def __init__(self, num_wheat=10):
        self.size = 9
        self.map = self._create_map()
        self.total_wheat = num_wheat
        self._place_wheat(num_wheat)
    
    def _create_map(self):
        """Creates a 9x9 grid filled with 0"""
        return [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def _place_wheat(self, num_wheat):
        """Randomly places wheat on the map"""
        placed = 0
        while placed < num_wheat:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.map[y][x] == 0:  # Empty cell
                self.map[y][x] = 1  # Place wheat
                placed += 1
    
    def get_cell(self, x, y):
        """Returns what's at position (x, y): 0=empty, 1=wheat"""
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.map[y][x]
        return -1  # Out of bounds
    
    def remove_wheat(self, x, y):
        """Removes wheat from position (x, y)"""
        if self.map[y][x] == 1:
            self.map[y][x] = 0
            return True
        return False
    
    def count_remaining_wheat(self):
        """Counts how many wheat are left on map"""
        count = 0
        for row in self.map:
            count += sum(row)
        return count
    
    def display(self, robot_x, robot_y):
        """Displays the map with robot position"""
        print("\n    ", end="")
        for i in range(self.size):
            print(f"{i:3}", end=" ")
        print()
        
        for y in range(self.size):
            print(f"{y} ", end="")
            for x in range(self.size):
                if x == robot_x and y == robot_y:
                    print("[ R ]", end="")
                elif self.map[y][x] == 1:
                    print("[ W ]", end="")
                else:
                    print("[ . ]", end="")
            print()
        print()

# Your code here:
# - is_valid_position()
def is_valid_position(x, y) :
    map_size = 9
    if 0 <= x < map_size and 0 <= y < map_size:
        return True
    else:
        return False

# - calculate_distance()
def calculate_distance(x1, y1, x2, y2):
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance

# - find_nearest_wheat()
def find_nearest_wheat(farm_map, robot_x, robot_y):
    min_distance = 999
    nearest_wheat = None
    
    for x in range(9):
        for y in range(9):
            if farm_map.get_cell(x, y) == 1:  # Found wheat
                distance = calculate_distance(robot_x, robot_y, x, y)
                if distance < min_distance:
                    min_distance = distance
                    nearest_wheat = (x, y)
    
    return nearest_wheat

# - Robot class
class Robot:   
    def __init__(self):
        self.x = 0
        self.y = 0
        self.energy = 100
        self.wheat_collected = 0

    
    def get_position(self):
        return (self.x, self.y) 
    
    def move(self, direction):
        new_x, new_y = self.x, self.y
        if direction == "UP":
            new_y -= 1
        elif direction == "DOWN":
            new_y += 1
        elif direction == "LEFT":
            new_x -= 1
        elif direction == "RIGHT":
            new_x += 1
        else:
            return False  # Invalid direction
        
        if is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.energy -= 1
            return True
        else:
            return False
    
    def harvest(self, farm_map):
        if farm_map.get_cell(self.x, self.y) == 1:
            if farm_map.remove_wheat(self.x, self.y):
                self.wheat_collected += 1
                return True
        return False
    
    def get_status(self):
        return f"Robot at ({self.x}, {self.y}) | Energy: {self.energy} | Wheat: {self.wheat_collected}"

# - move_robot_to()
def move_robot_to(robot, farm, target_x, target_y):
    print(f"moving target from {robot.get_position()} to ({target_x}, {target_y})")
    
    if robot.x == target_x and robot.y == target_y:
        print("Arrived at target!")
        return True
    
    # move horizontally X
    while robot.x != target_x and robot.energy > 0:
        if robot.x < target_x:
            if robot.move("RIGHT"):
                print(f"Moving Right, now at {robot.get_position()}")
            else:
                print("Cannot move Right, stopping.")
                return False
        else:
            if robot.move("LEFT"):
                print(f"Moving Left... now at {robot.get_position()}")
            else:
                print("Cannot move Left, stopping.")
                return False
        farm.display(robot.x, robot.y)
        time. sleep(0.4)  
        print(robot.get_status())
    
    # move vertically Y
    while robot.y != target_y and robot.energy > 0:
        if robot.y < target_y:
            if robot.move("DOWN"):
                print(f"moving Down, now at {robot.get_position()}")
            else:
                print("cannot move Down, stopping.")
                return False
        else:
            if robot.move("UP"):
                print (f"moving Up, now at {robot.get_position()}")
            else:
                print("canoot move Up, stopping.")
                return False
        farm.display(robot.x, robot.y)
        time. sleep(0.4)  
        print(robot.get_status())    
            
            
    # Check if arrived
    if robot.x == target_x and robot.y == target_y:
        print("arrived at target!")
        return True
    else:
        print("cannot reach target, out of energy.")
        return False

# - patrol_and_harvest()
def manual_partrol_harvest(robot, farm):
    
    print("\n manual patrol and harvest \n")
    harvest = 1
    
    while farm.count_remaining_wheat() > 0 and robot.energy > 0:
        print(f"\n--- harvest roound {harvest} ---\n")
        print(f"wheat remaning on farm: {farm.count_remaining_wheat()}")
        farm.display(robot.x, robot.y)
        print(robot.get_status())
        
        #manual move to target
        event = input("Enter direction (w/a/s/d/g or e ): ").strip().lower()
        moved = False
        if event == ("w"):
            moved = robot.move("UP")
            
        elif event == ("s"):
            moved = robot.move("DOWN")
            
        elif event == ("a"):
            moved = robot.move("LEFT")
            
        elif event == ("d"):
            moved = robot.move("RIGHT")
            
        elif event == "g":
            harvested = robot.harvest(farm)
            farm.display(robot.x, robot.y)
            print(robot.get_status())
            if harvested:
                print("wheat harvested!")
            else:
                print("no wheat to harvest here.")
            time.sleep(0.4)  
            continue
            
        elif event == "e":
            print("quitting manual patrol.")
            break
        
        # harvest wheat
        if moved:
            farm.display(robot.x, robot.y)
            print(robot.get_status())
            time.sleep(0.4)
        else:
            if event in ["w", "s", "a", "d", "g", "e"]:
                print("cannot move in that direction.")
            time.sleep(0.4)
                
        
        harvest += 1
    print("\n--- patrol and harvest complete ---\n")
    print(f"final position: {robot.get_position()}")

# Test everything
print("🤖 FARMING ROBOT SYSTEM")
print("="*50)

farm = FarmMap(num_wheat=5)
robot = Robot()

print("\n📊 INITIAL STATUS:")
farm.display(robot.x, robot.y)
print(robot.get_status())
print(f"Wheat on map: {farm.count_remaining_wheat()}")

print("\n" + "="*50)
print("🚜 STARTING MANUAL HARVEST...")
print("="*50 + "\n")

manual_partrol_harvest(robot, farm)

print("\n" + "="*50)
print("📊 FINAL STATUS:")
print("="*50)
farm.display(robot.x, robot.y)
print(robot.get_status())
print(f"Wheat on map: {farm.count_remaining_wheat()}")

if farm.count_remaining_wheat() == 0:
    print("\n🎉 SUCCESS! All wheat harvested!")
else:
    print(f"\n⚠️  {farm.count_remaining_wheat()} wheat remaining")