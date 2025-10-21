import random

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


## 🎯 YOUR TASKS - CREATE THE ROBOT


## 📝 PART 1: BASIC ROBOT FUNCTIONS (30 points)

### Task 1.1: Check Valid Position
# - Checks if position (x, y) is inside the map (0 to 8)
# - Returns `True` if valid, `False` if outside
def is_valid_position(x, y) :
    map_size = 9
    if 0 <= x < map_size and 0 <= y < map_size:
        return True
    else:
        return False

print(is_valid_position(5, 5))   # Output: True
print(is_valid_position(0, 7))   # Output: True
print(is_valid_position(9, 5))   # Output: False
print(is_valid_position(-1, 5))  # Output: False


## Task 1.2: Calculate Distance
# - Calculates Manhattan distance between two points
# - Formula: |x2 - x1| + |y2 - y1|
# - Returns the distance
def calculate_distance(x1, y1, x2, y2):
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance

distance = calculate_distance(0, 0, 3, 4)
print(distance)  # Output: 7


### Task 1.3: Find Nearest Wheat
# - Searches the entire 9x9 map for wheat
# - Finds the wheat closest to robot's position
# - Use `farm_map.get_cell(x, y)` to check each cell (returns 1 if wheat)
# - Returns (x, y) tuple of nearest wheat
# - Returns None if no wheat found
def find_nearest_wheat(farm_map, robot_x, robot_y):

**Example**:
```python
farm = FarmMap(num_wheat=5)
nearest = find_nearest_wheat(farm, 0, 0)
print(nearest)  # Output: (2, 0) or whatever is closest
```

# **Hint**: Loop through all positions (0-8 for both x and y), check each cell, calculate distance, keep track of the closest one.

# ---

# ## 📝 PART 2: ROBOT CLASS (40 points)

# ### Task 2.1: Create Robot Class

# Create a class with these specifications:

# ```python
# class Robot:
#     """
#     Properties:
#     - x: int (current x position, starts at 0)
#     - y: int (current y position, starts at 0)
#     - energy: int (battery level, starts at 100)
#     - wheat_collected: int (starts at 0)
    
#     Methods to implement:
#     - __init__(self)
#     - get_position(self)
#     - move(self, direction)
#     - harvest(self, farm_map)
#     - get_status(self)
#     """
    
#     def __init__(self):
#         # TODO: Initialize robot at position (0, 0)
#         # TODO: Set energy to 100
#         # TODO: Set wheat_collected to 0
#         pass
    
#     def get_position(self):
#         # TODO: Return tuple (x, y) of current position
#         pass
    
#     def move(self, direction):
#         """
#         Moves robot one step in given direction
        
#         Parameters:
#         - direction: string ("UP", "DOWN", "LEFT", "RIGHT")
        
#         Rules:
#         - UP means y-1, DOWN means y+1
#         - LEFT means x-1, RIGHT means x+1
#         - Check if new position is valid (use is_valid_position function)
#         - If valid: update position, reduce energy by 1
#         - If invalid: don't move, don't use energy
        
#         Returns: True if moved, False if couldn't move
#         """
#         # TODO: Calculate new position based on direction
#         # TODO: Check if valid using is_valid_position()
#         # TODO: If valid, update x and y, reduce energy
#         # TODO: Return True/False
#         pass
    
#     def harvest(self, farm_map):
#         """
#         Harvests wheat at current position
        
#         Parameters:
#         - farm_map: FarmMap object
        
#         Rules:
#         - Check if current position has wheat using farm_map.get_cell(x, y)
#         - If yes: remove wheat using farm_map.remove_wheat(x, y)
#         - Increase wheat_collected by 1
        
#         Returns: True if harvested, False if no wheat
#         """
#         # TODO: Check if wheat at current position
#         # TODO: If yes, remove it and increase counter
#         # TODO: Return True/False
#         pass
    
#     def get_status(self):
#         """Returns formatted status string"""
#         # TODO: Return something like:
#         # "Robot at (3, 4) | Energy: 85 | Wheat: 5"
#         pass
# ```

# **Test Your Robot**:
# ```python
# farm = FarmMap(num_wheat=5)
# robot = Robot()

# print(robot.get_status())
# print(robot.get_position())  # Should be (0, 0)

# robot.move("RIGHT")
# print(robot.get_position())  # Should be (1, 0)
# print(robot.energy)          # Should be 99

# robot.move("DOWN")
# robot.move("DOWN")
# print(robot.get_position())  # Should be (1, 2)

# result = robot.harvest(farm)
# print(f"Harvested: {result}")
# print(robot.get_status())
# ```

# ---

# ## 📝 PART 3: AUTOMATED HARVESTING (30 points)

# ### Task 3.1: Move Robot to Target

# Write a function `move_robot_to(robot, target_x, target_y)` that:
# - Moves robot from current position to target position
# - Move step by step (one cell at a time)
# - Strategy: Move horizontally first, then vertically
# - Print each move
# - Stop if robot runs out of energy

# **Example**:
# ```python
# robot = Robot()
# farm = FarmMap(num_wheat=5)

# move_robot_to(robot, 3, 4)
# # Should print:
# # Moving RIGHT... now at (1, 0)
# # Moving RIGHT... now at (2, 0)
# # Moving RIGHT... now at (3, 0)
# # Moving DOWN... now at (3, 1)
# # Moving DOWN... now at (3, 2)
# # Moving DOWN... now at (3, 3)
# # Moving DOWN... now at (3, 4)
# # Arrived at target!
# ```

# **Hint**:
# ```python
# # Move horizontally
# while robot.x < target_x:
#     robot.move("RIGHT")
#     print(f"Moving RIGHT... now at {robot.get_position()}")

# while robot.x > target_x:
#     # TODO: move LEFT
#     pass

# # Then move vertically
# while robot.y < target_y:
#     # TODO: move DOWN
#     pass

# while robot.y > target_y:
#     # TODO: move UP
#     pass
# ```

# ### Task 3.2: Automatic Patrol and Harvest (MAIN CHALLENGE!)

# Write a function `patrol_and_harvest(robot, farm_map)` that:
# - Automatically harvests ALL wheat on the map
# - Uses all the functions you created before

# **Algorithm**:
# ```
# 1. WHILE there is wheat on map AND robot has energy > 0:
   
#    a. Find nearest wheat using find_nearest_wheat()
   
#    b. If no wheat found, break
   
#    c. Move robot to that wheat using move_robot_to()
   
#    d. Harvest the wheat using robot.harvest()
   
#    e. Print status
   
# 2. Print final summary
# ```

# **Example**:
# ```python
# robot = Robot()
# farm = FarmMap(num_wheat=10)

# print("Initial Map:")
# farm.display(robot.x, robot.y)
# print(robot.get_status())

# patrol_and_harvest(robot, farm)

# print("\nFinal Map:")
# farm.display(robot.x, robot.y)
# print(robot.get_status())
# print(f"Wheat remaining: {farm.count_remaining_wheat()}")
# ```

# **Expected Output**:
# ```
# Initial Map:
#     0   1   2   3   4   5   6   7   8
# 0 [ R ] [ . ] [ W ] [ . ] [ . ] [ W ] [ . ] [ . ] [ . ]
# 1 [ . ] [ . ] [ . ] [ W ] [ . ] [ . ] [ . ] [ . ] [ W ]
# ...

# Robot at (0, 0) | Energy: 100 | Wheat: 0

# 🎯 Target: Wheat at (2, 0)
# Moving RIGHT... now at (1, 0)
# Moving RIGHT... now at (2, 0)
# 🌾 Harvested wheat! Total: 1

# 🎯 Target: Wheat at (5, 0)
# Moving RIGHT... now at (3, 0)
# Moving RIGHT... now at (4, 0)
# Moving RIGHT... now at (5, 0)
# 🌾 Harvested wheat! Total: 2

# ...continues...

# ✅ All wheat harvested!

# Final Map:
#     0   1   2   3   4   5   6   7   8
# 0 [ . ] [ . ] [ . ] [ . ] [ . ] [ . ] [ . ] [ . ] [ . ]
# 1 [ . ] [ . ] [ . ] [ . ] [ . ] [ . ] [ . ] [ . ] [ . ]
# ...

# Robot at (8, 8) | Energy: 23 | Wheat: 10
# Wheat remaining: 0
# ```

# ---

# ## 🧪 COMPLETE TEST PROGRAM

# Use this to test everything:

# ```python
# import random
# random.seed(42)  # For consistent results

# # Copy the FarmMap class here (provided above)

# # Your code here:
# # - is_valid_position()
# # - calculate_distance()
# # - find_nearest_wheat()
# # - Robot class
# # - move_robot_to()
# # - patrol_and_harvest()

# # Test everything
# print("🤖 FARMING ROBOT SYSTEM")
# print("="*50)

# farm = FarmMap(num_wheat=10)
# robot = Robot()

# print("\n📊 INITIAL STATUS:")
# farm.display(robot.x, robot.y)
# print(robot.get_status())
# print(f"Wheat on map: {farm.count_remaining_wheat()}")

# print("\n" + "="*50)
# print("🚜 STARTING AUTOMATIC HARVEST...")
# print("="*50 + "\n")

# patrol_and_harvest(robot, farm)

# print("\n" + "="*50)
# print("📊 FINAL STATUS:")
# print("="*50)
# farm.display(robot.x, robot.y)
# print(robot.get_status())
# print(f"Wheat on map: {farm.count_remaining_wheat()}")

# if farm.count_remaining_wheat() == 0:
#     print("\n🎉 SUCCESS! All wheat harvested!")
# else:
#     print(f"\n⚠️  {farm.count_remaining_wheat()} wheat remaining")
# ```

# ---

# ## 🎯 GRADING CRITERIA

# **Part 1 (30 points)**:
# - Task 1.1: 10 points (is_valid_position)
# - Task 1.2: 10 points (calculate_distance)
# - Task 1.3: 10 points (find_nearest_wheat)

# **Part 2 (40 points)**:
# - Robot.__init__: 5 points
# - Robot.get_position: 5 points
# - Robot.move: 15 points (most important!)
# - Robot.harvest: 10 points
# - Robot.get_status: 5 points

# **Part 3 (30 points)**:
# - Task 3.1: 10 points (move_robot_to function)
# - Task 3.2: 20 points (patrol_and_harvest - the main challenge!)

# **Bonus (10 points)**:
# - Robot returns to (0, 0) after harvesting all wheat
# - Add energy efficiency: choose path that uses less energy
# - Handle case when robot runs out of energy

# ---

# ## 💡 KEY CONCEPTS YOU'LL LEARN

# ### Function Chaining:
# ```
# is_valid_position()  →  used by move()
# calculate_distance()  →  used by find_nearest_wheat()
# find_nearest_wheat()  →  used by patrol_and_harvest()
# move()  →  used by move_robot_to()
# move_robot_to()  →  used by patrol_and_harvest()
# harvest()  →  used by patrol_and_harvest()
# ```

# ### Breaking Big Problems:
# ```
# BIG PROBLEM: "Harvest all wheat automatically"
#     ↓
# MEDIUM: "Find wheat, go there, harvest, repeat"
#     ↓
# SMALL: "Move one step", "Check cell", "Remove wheat"
# ```

# ---

# ## 💡 HELPFUL HINTS

# ### For find_nearest_wheat:
# ```python
# min_distance = 999  # Start with very large number
# nearest_wheat = None

# for y in range(9):
#     for x in range(9):
#         if farm_map.get_cell(x, y) == 1:  # Found wheat!
#             distance = calculate_distance(robot_x, robot_y, x, y)
#             if distance < min_distance:
#                 min_distance = distance
#                 nearest_wheat = (x, y)

# return nearest_wheat
# ```

# ### For Robot.move:
# ```python
# new_x = self.x
# new_y = self.y

# if direction == "UP":
#     new_y = self.y - 1
# elif direction == "DOWN":
#     new_y = self.y + 1
# # ... etc

# if is_valid_position(new_x, new_y):
#     self.x = new_x
#     self.y = new_y
#     self.energy -= 1
#     return True
# return False
# ```

# **Good luck! 🤖🌾**