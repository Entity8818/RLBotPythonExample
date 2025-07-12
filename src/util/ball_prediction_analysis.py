from typing import Callable

import math

def distance(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2)

def find_best_scoring_path(my_car, ball, other_cars, goal_location):
    # Step 1: Scan positions
    my_pos = my_car.position
    ball_pos = ball.position
    # Step 2: Calculate direct path to ball
    path_to_ball = distance(my_pos, ball_pos)
    # Step 3: Check for obstacles (other cars)
    for car in other_cars:
        if distance(car.position, ball_pos) < 500:  # threshold for blocking
            # Adjust path or plan a dodge
            pass
    # Step 4: Plan shot towards goal
    ball_to_goal = distance(ball_pos, goal_location)
    # Step 5: Choose action
    if path_to_ball < 2000 and ball_to_goal < 3000:
        action = "boost and shoot"
    else:
        action = "position for pass"
    return action

# Example usage
action = find_best_scoring_path(my_car, ball, other_cars, goal_location)
print("AI action:", action)
