# Unexpected behavior with the IF function in Blender Game Engine
acceleration = -0.05 if braking else 0.05
speed = max(0, min(max_speed, speed + acceleration))
