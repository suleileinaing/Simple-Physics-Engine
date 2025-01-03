from vector import Vector
from balls import Ball
import constant as c

#reference : Lecture Week 12 practice code 

def wall_collision(ball : Ball, border_width):

    if ball.center.x - ball.radius < border_width :
        ball.center.x = border_width + ball.radius
        ball.velocity.x *= -1
       
    elif ball.center.x + ball.radius > 600 - border_width:
        ball.center.x = 600 - border_width - ball.radius
        ball.velocity.x *= -1
       
    if ball.center.y - ball.radius < border_width :
        ball.center.y = border_width + ball.radius
        ball.velocity.y *= -1
       
    elif ball.center.y + ball.radius > 600 - border_width:
        ball.center.y = 600 - border_width - ball.radius
        ball.velocity.y *= -1

def check_collision(ball1: Ball, ball2: Ball):
    distance = ball1.center.distance_to(ball2.center)

    if distance >= ball1.radius + ball2.radius:

        return None, None
    
    normal_vector = (ball1.center - ball2.center).normalize()

    penetration_depth  = ball1.radius + ball2.radius - distance
    return normal_vector, penetration_depth

def separate_bodies (ball1: Ball, ball2: Ball, normal, penetration_depth):
    overlap = normal * penetration_depth
    ball1.center -= overlap/2
    ball2.center += overlap/2

def collision(ball1: Ball, ball2: Ball):
    normal, depth = check_collision(ball1, ball2)
    if normal is None or depth is None:
        return
    collision_response(ball1, ball2, normal, depth)

def collision_response(ball1: Ball, ball2: Ball, normal_vector: Vector, penetration_depth: float):
    normal_vector *= -1
    separate_bodies(ball1, ball2, normal_vector, penetration_depth)

    relative_velocity = ball2.velocity - ball1.velocity

    penetration_velocity = relative_velocity.dot(normal_vector)

    if penetration_velocity > 0:
        return

    j = -(1+ball1.bounce)* penetration_velocity

    impulse = normal_vector * j

    impulse_per_mass = impulse / (1 / ball1.mass + 1 / ball2.mass)
    ball1.velocity -= impulse_per_mass / ball1.mass
    ball2.velocity += impulse_per_mass / ball2.mass
