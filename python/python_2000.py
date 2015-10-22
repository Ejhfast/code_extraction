# importing same module more than once
from main.folderA.fileA import *   # absolute
from .fileA import *               # unambiguous-relative
from fileA import *                # ambiguous-relative
