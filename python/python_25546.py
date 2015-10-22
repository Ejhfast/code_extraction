# Overriding SCons Cache Copy Function
import SCons.Environment
SCons.Environment.Environment._copy_from_cache = link_or_copy_file
SCons.Environment.Environment._copy2_from_cache = link_or_copy_file
