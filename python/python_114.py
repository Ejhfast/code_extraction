# How do I find userid by login (Python under *NIX)
import pwd
pw = pwd.getpwnam("nobody")
uid = pw.pw_uid
