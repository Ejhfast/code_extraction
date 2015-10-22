# Sorting a list using calculation from class definition
sorted(TheGame.turn, key=lambda user: user.distance_to_goal(TheGame.hole.goal_position))
