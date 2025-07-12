def can_aerial(my_car, ball):
    # Check if the ball is airborne and within reach
    return ball.position.z > 300 and my_car.boost > 20

def use_boost(my_car, target):
    # Use boost if not at max speed and boost is available
    if my_car.boost > 0 and my_car.speed < 2200:
        my_car.activate_boost()
    my_car.steer_towards(target)

def find_best_scoring_action(my_car, ball, other_cars, goal_location):
    my_pos = my_car.position
    ball_pos = ball.position

    if can_aerial(my_car, ball):
        use_boost(my_car, ball_pos)
        action = "perform aerial shot"
    elif my_car.boost > 0:
        use_boost(my_car, ball_pos)
        action = "boost towards ball"
    else:
        my_car.steer_towards(ball_pos)
        action = "drive towards ball"

    # Add logic for shooting at goal if close
    if distance(ball_pos, goal_location) < 3000:
        action += " and shoot at goal"

    return action

# Example usage
action = find_best_scoring_action(my_car, ball, other_cars, goal_location)
print("AI action:", action)
