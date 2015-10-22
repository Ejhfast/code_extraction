# AI projectile targeting, firing a rocket/bullet/etc. so that it intercepts a target
desired_vel = Vector2D( (target_pos.x + target_vel.x * t) - shooter.pos.x, (target_pos.y + target_vel.y*t) - shooter.pos.y ) * self.max_speed
