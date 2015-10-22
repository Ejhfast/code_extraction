# Accessing a memory-mapped file using Python
s = struct.unpack('IL3f3f3f512s3f')
name = s[11].decode('utf-16')
camera_pos_x,camera_pos_y,camera_pos_z = s[12:15]
