# Is there a way to know if a user changes the Default "Activity Privacy" for your FB app
SELECT name, value, description, allow, deny, networks, friends
FROM privacy_setting
WHERE name = 'default_stream_privacy'
