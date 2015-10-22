# Calling AppleScript from Python without using osascript or appscript?
&gt;&gt;&gt; from Foundation import *
&gt;&gt;&gt; s = NSAppleScript.alloc().initWithSource_("tell app \"Finder\" to activate")
&gt;&gt;&gt; s.executeAndReturnError_(None)
