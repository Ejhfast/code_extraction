# Tools for implementing a watchdog timer in python
import pexpect
c=pexpect.spawn('your_command')
c.expect("expected_output_regular_expression", timeout=10)
