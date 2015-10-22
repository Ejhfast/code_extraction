# How to reload python module imported using "from module import *"
import X
reload( X )
from X import Y # or * for that matter
