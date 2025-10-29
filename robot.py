import random
import time

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

## Task 1.2: Calculate Distance
# - Calculates Manhattan distance between two points
# - Formula: |x2 - x1| + |y2 - y1|
# - Returns the distance


### Task 1.3: Find Nearest Wheat
# - Searches the entire 9x9 map for wheat
# - Finds the wheat closest to robot's position
# - Use `farm_map.get_cell(x, y)` to check each cell (returns 1 if wheat)
# - Returns (x, y) tuple of nearest wheat
# - Returns None if no wheat found

# **Exa÷mple**:
# ```python
# Output: (2, 0) or whatever is closest
# ```

# **Hint**: Loop through all positions (0-8 for both x and y), check each cell, calculate distance, keep track of the closest one.

# ---

# ## 📝 PART 2: ROBOT CLASS (40 points)

# ### Task 2.1: Create Robot Class

# Create a class with these specifications:

# ```python
        # TODO: Initialize robot at position (0, 0)
        # TODO: Set energy to 100
        # TODO: Set wheat_collected to 0
        # TODO: Return tuple (x, y) of current position
        # TODO: Calculate new position based on direction
        # TODO: Check if valid using is_valid_position()
        # TODO: If valid, update x and y, reduce energy
        # TODO: Return True/False
        # TODO: Check if wheat at current position
        # TODO: If yes, remove it and increase counter
        # TODO: Return True/False
        # TODO: Return something like:
        # "Robot at (3, 4) | Energy: 85 | Wheat: 5"
        
    
# ```

# **Test Your Robot**:
# ```python
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