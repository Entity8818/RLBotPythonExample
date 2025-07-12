def use_boost_if_needed(controller, my_car, target_pos):
    """
    Activates boost if the car is far from the target and has boost available.
    """
    car_pos = my_car.physics.location
    distance = math.sqrt((car_pos.x - target_pos.x)**2 + (car_pos.y - target_pos.y)**2)
    # Use boost if distance is large and car has boost
    if distance > 1000 and my_car.boost > 0:
        controller.boost = True
    else:
        controller.boost = False
    return controller

# Example usage in get_output:
controller_state = SimpleControllerState()
target_pos = ball.physics.location  # or wherever you want to go
controller_state = use_boost_if_needed(controller_state, my_car, target_pos)
