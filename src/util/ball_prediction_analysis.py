from typing import Callable

import math

def distance_2d(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def analyze_ball_prediction(ball_prediction, my_car, goal_location):
    """
    Analyzes ball prediction slices to find the best opportunity to score.
    Returns the target position and time to intercept.
    """
    best_slice = None
    min_distance = float('inf')
    intercept_time = None

    # Loop through prediction slices
    for slice in ball_prediction.slices:
        ball_pos = slice.physics.location
        time = slice.game_seconds

        # Check if ball is heading towards goal
        if abs(ball_pos.y - goal_location.y) < 1000:
            # Calculate distance from car to ball
            car_to_ball = distance_2d(my_car.physics.location, ball_pos)
            if car_to_ball < min_distance:
                min_distance = car_to_ball
                best_slice = ball_pos
                intercept_time = time

    return best_slice, intercept_time

def get_intercept_action(my_car, target_pos, intercept_time):
    """
    Returns controller actions to intercept the ball at the target position.
    """
    controller = SimpleControllerState()
    car_pos = my_car.physics.location

    # Steer towards target
    angle = math.atan2(target_pos.y - car_pos.y, target_pos.x - car_pos.x)
    controller.steer = 1 if angle > 0 else -1

    # Use boost if far away or need to reach quickly
    if distance_2d(car_pos, target_pos) > 1000 and my_car.boost > 0:
        controller.boost = True

    # Jump for aerial if ball is high
    if target_pos.z > 300 and my_car.boost > 20:
        controller.jump = True

    return controller

# Example usage in your bot:
# best_pos, intercept_time = analyze_ball_prediction(ball_prediction, my_car, goal_location)
# controller_state = get_intercept_action(my_car, best_pos, intercept_time)

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
