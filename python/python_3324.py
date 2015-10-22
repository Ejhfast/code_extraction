# Check if passwordless access has been setup
ssh -oNumberOfPasswordPrompts=0 &lt;host&gt; "echo hello"
