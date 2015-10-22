# How to pass UniqueRequestToken to AWS mechanical turk using Boto
from mturkcore import MechanicalTurk
m = MechanicalTurk()
m.create_request("CreateHIT", {..."UniqueRequestToken":"..."})
