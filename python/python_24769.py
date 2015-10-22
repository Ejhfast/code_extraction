# Middleware redirect user to path if user is invalid
if not request.user.profile.is_valid_member():
