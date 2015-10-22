# Python crypt module -- what's the correct use of salts?
string_to_hash = user.stored_salt + entered_password
successful_login = (sha1(string_to_hash) == user.stored_password_hash)
