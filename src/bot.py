[Bot]
name = Logical
team = 0
type = python
python_file = bot.py

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
import math

class MyBot(BaseAgent):
    def initialize_agent(self):
        # Initialization code here
        pass

    def get_output(self, packet):
        controller_state = SimpleControllerState()
        my_car = packet.game_cars[self.index]
        ball = packet.game_ball

        # Calculate 2D distance to ball
        car_pos = my_car.physics.location
        ball_pos = ball.physics.location
        distance = math.sqrt((car_pos.x - ball_pos.x)**2 + (car_pos.y - ball_pos.y)**2)

        # Steer towards ball
        angle = math.atan2(ball_pos.y - car_pos.y, ball_pos.x - car_pos.x)
        controller_state.steer = 1 if angle > 0 else -1

        # Use boost if far from ball and boost is available
        if distance > 1000 and my_car.boost > 0:
            controller_state.boost = True

        # Attempt aerial if ball is high and car has boost
        if ball_pos.z > 300 and my_car.boost > 20:
            controller_state.jump = True
            controller_state.boost = True

        # Drive forward
        controller_state.throttle = 1

        return controller_state
