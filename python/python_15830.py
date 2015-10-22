# Calculating a half vector from eye/camera vector and surface normal
light_vect = light_position - face_center_position
cam_vect = cam_position - face_center_position
halfangle_vect = (light_vect.normal() + cam_vect.normal()).normal()
