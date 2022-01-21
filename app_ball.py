from vector import Vector
from ball import Ball
""" 
    Build and collect the data in the value.
    In the value pos, vel and acc need to use .split(",") used to split a coordinate pair into two numbers.
    Build the value to collect Ball(parameter) and decide data each parameter are the float number 
    and used round() function to mitigate this problem.
    Thus, I used while that I make the condition is time <= limit + step 
    and used .update(parameter) to update every value.
"""
# implement your ball simulation application here
time = 0.00
step = float(input("Enter the time step in seconds: "))
limit = float(input("Enter the time limit in seconds: "))
pos = input("Enter the ball's initial position vector (x,y): ").split(",")
vel = input("Enter the ball's initial velocity vector (x,y): ").split(",")
acc = input("Enter the ball's acceleration vector (x,y): ").split(",")
b = Ball(Vector(round(float(pos[0])), round(float(pos[1]))), Vector(round(float(vel[0])), round(float(vel[1]))),
         Vector(round(float(acc[0])), round(float(acc[1]))))
while time <= limit + step:
    print(f"Time={time:.2f} sec, pos=({b.pos.x:.2f},{b.pos.y:.2f}), vel={b.vel.y:.2f}")
    b.update(step)
    time = time + step