# Robot Framework: access robot's global variables from python library code?
from robot.libraries.BuiltIn import BuiltIn
results_path = BuiltIn().get_variable_value("${RESULTS_PATH}")
