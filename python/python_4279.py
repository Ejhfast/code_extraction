# Why does python __file__ variable returns errorneous path when used in DJango?
import os
    os.path.abspath(os.path.dirname(__file__))
