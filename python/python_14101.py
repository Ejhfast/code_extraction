# How to fix localflavor deprecation warning in django 1.5?
import warnings
warnings.filterwarnings('ignore', r"django.contrib.localflavor is deprecated")
